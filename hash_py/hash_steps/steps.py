import numpy as np
from hash_steps.substeps import append_bytes, append_num, fill_schedule_values, compression_step  
from hash_steps.utils import uint8_to_uint32, add_mod_2tothe32

# Parameters
CHUNK_LEN = 512
CHUNK_LEN_BYTES = CHUNK_LEN//8
CHUNK_LEN_UINT32 = CHUNK_LEN//32

# Hash constants
HASH_CONSTANTS = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

# Round constants
ROUND_CONSTANTS = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
              0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
              0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
              0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
              0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
              0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
              0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
              0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]



def preprocess(input: bytes) -> tuple[np.ndarray, int]:
    """
    This function takes a bytes object
    as input and performs the necessary
    preprocessing on it. Returns a list
    containing an n X 64 dim numpy array
    and the final number of chunks.
    """

    # Convert input to list of uint8 and save original length in bytes
    input_bytes = np.array(bytearray(input))
    input_bytes_len = input_bytes.shape[0]

    # Compute number of 0x00 bytes to append
    n_padding_zeros = CHUNK_LEN_BYTES - (input_bytes_len + 9) % CHUNK_LEN_BYTES
 
    # Append the necessary bytes
    input_bytes = append_bytes(input_bytes, n_padding_zeros)
    
    # Append length of original string in bits as uint64
    input_bits_len = input_bytes_len * 8
    input_bytes = append_num(input_bytes, input_bits_len)
 
    return input_bytes



def create_message_schedule(input_bytes: list) -> tuple[np.array, int]:
    """
    Creates the message schedule for SHA256.
    The function takes the input array of bytes
    and transforms it into a (n_chunk, 64)
    array of chunks containing uint32 values.
    """
    len = input_bytes.shape[0]
    new_len = len//4
    new_input_bytes = np.zeros((new_len), dtype=np.uint32)

    for idx in range(new_len):
        start = 4 * idx
        end = 4 * (idx+1)
        new_input_bytes[idx] = uint8_to_uint32(input_bytes[start:end])

    # Create a list containing chunks as separate numpy arrays
    n_chunks = new_input_bytes.shape[0]//CHUNK_LEN_UINT32
    chunks = np.expand_dims(new_input_bytes[0:CHUNK_LEN_UINT32], axis=0)

    for idx in range(1, n_chunks):
        start = CHUNK_LEN_UINT32 * idx
        end = CHUNK_LEN_UINT32 * (idx+1)
        chunk = np.expand_dims(new_input_bytes[start:end], axis=0)
        chunks = np.concatenate((chunks, chunk), axis=0)

    # Now add 48 word initialized to 0 to each chunk
    zeros = np.zeros((n_chunks, 48), dtype=np.uint32)
    chunks = np.concatenate((chunks, zeros), axis=1)

    for idx, chunk in enumerate(chunks):
        chunks[idx][:] = fill_schedule_values(chunk)

    return chunks, n_chunks



def compress(chunks: np.ndarray, n_chunks: int) -> np.ndarray:
    """
    This function executes the
    compression loop on the input,
    which must be a numpy array
    of shape (n_chunks, 64) containing
    uint32 values.
    """

    hash_values = np.array(HASH_CONSTANTS, dtype=np.uint32)
    round_constants = np.array(ROUND_CONSTANTS, dtype=np.uint32)

    for chunk in chunks:
        accumulator = np.array(HASH_CONSTANTS, dtype=np.uint32)
        accumulator = compression_step(h=accumulator, w=chunk, k=round_constants)

        for idx, (a, h) in enumerate(zip(accumulator, hash_values)):
            hash_values[idx] = add_mod_2tothe32(a, h)

    return hash_values
    

    
