from torch import chunk
from utils import debug_print_chunks
import numpy as np



# Parameters
CHUNK_LEN = 512
CHUNK_LEN_BYTES = CHUNK_LEN//8

# Hash constants
HCONSTANTS = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

# Round constants
RCONSTANTS = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
              0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
              0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
              0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
              0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
              0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
              0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
              0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]




def preprocess(input: bytes):
    """
    This function takes a bytes object
    as input and performs the necessary
    preprocessing on it. Returns a list
    containing an n X 64 dim numpy array
    and the final number of chunks.
    """

    # Convert input to list of uint8
    input_bytes = []
    input_bytes = np.array(input)
    input_bytes = np.array(bytearray(input_bytes))

    #Append a 0x80 byte
    input_bytes = np.concatenate((input_bytes, np.array([0x80], dtype=np.uint8)), axis=0)

    # Compute number of 0x00 bytes to append and append them
    input_bytes_len = len(input_bytes)
    input_bytes_original_len = input_bytes_len - 1
    n_padding_zeros = CHUNK_LEN_BYTES - (input_bytes_len + 8) % CHUNK_LEN_BYTES
    for idx in range(n_padding_zeros):
        input_bytes = np.concatenate((input_bytes, np.array([0x00], dtype=np.uint8)), axis=0)

    # Append length of original input as an unsigned long int (8 bytes) to input_bytes
    for idx in range(8):
        byte_to_append = input_bytes_original_len >> 8*(7 - idx)
        byte_to_append = np.array([byte_to_append], dtype=np.uint8)
        input_bytes = np.concatenate((input_bytes, byte_to_append), axis=0)

    # Create a list containing chunks as separate numpy arrays
    n_chunks = len(input_bytes)//CHUNK_LEN_BYTES

    chunks = np.expand_dims(input_bytes[0:CHUNK_LEN_BYTES], axis=0)

    for idx in range(1,n_chunks):
        start = idx * CHUNK_LEN_BYTES
        end = (idx + 1) * CHUNK_LEN_BYTES
        chunk = np.expand_dims(input_bytes[start:end], axis=0)
        chunks = np.concatenate((chunks, chunk), axis=0)

    print(chunks)

    return n_chunks, chunks



def create_message_schedule(chunks: list, n_chunks: int) -> np.array:
    pass