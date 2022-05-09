from ctypes import c_uint8 as uint8
from ctypes import c_uint32 as uint32
from utils import debug_print_chunks


CHUNK_LEN = 512

def preprocess(input: bytes) -> list:
    """
    This function takes a bytes object
    as input and performs the necessary
    preprocessing on it.
    """

    # Convert input to list of uint8
    input_bytes = []
    input = bytearray(input)
    for byte in input:
        input_bytes.append(uint8(byte))

    #Append a 0x80 byte
    input_bytes.append(uint8(0x80))
    debug_print_chunks(input_bytes)

    # Compute number of 0x00 bytes to append and append them
    input_bytes_len = len(input_bytes)
    input_bytes_original_len = input_bytes_len - 1
    n_padding_zeros = CHUNK_LEN - (input_bytes_len + 64) % CHUNK_LEN
    for idx in range(n_padding_zeros):
        input_bytes.append(uint8(0x00))

    debug_print_chunks(input_bytes)
    print(len(input_bytes))

    # Append length of original input as an unsigned long int (8 bytes) to input_bytes
    for idx in range(8):
        pass
     
