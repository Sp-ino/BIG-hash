import numpy as np



def debug_print_chunks(chunks: list) -> None:
    for idx, byte in enumerate(chunks):
        if idx % 512 == 0:
            print(f"\n\nChunk {idx//512}:") 
        if idx % 8 == 0:
            print(f"\nRow {idx//8} ")

        print(f"{hex(byte)}\t", end="")



def append_bytes(arr: np.ndarray, n: int) -> np.ndarray:
    """
    Append to arr a 0x80 and then n 0x00
    """

    #Append a 0x80 byte
    arr = np.concatenate((arr, np.array([0x80], dtype=np.uint8)), axis=0)

    # Append 0x00 bytes
    to_append = np.zeros((n), dtype=np.uint8)
    arr = np.concatenate((arr, to_append), axis=0)

    return arr



def append_ulong(arr: np.ndarray, num: int) -> np.ndarray:
    """
    Append num as an unsigned 
    long int (8 bytes) to arr
    """
    
    for idx in range(8):
        byte_to_append = num >> 8*(7 - idx)
        byte_to_append = np.array([byte_to_append], dtype=np.uint8)
        arr = np.concatenate((arr, byte_to_append), axis=0)

    return arr



def uint8_to_uint32(arr: np.ndarray) -> np.ndarray:
    """
    Takes a numpy array of uint8 of length 4
    and reorganizes it into an array of uint32.
    """

    if arr.shape[0] != 4:
        raise OSError("arr must be a np.ndarray of shape (4,)")

    out = np.array([0], dtype=np.uint32)
    for idx, byte in enumerate(arr):
        partial = np.uint32(byte)
        partial = partial << 8 * (3 - idx)
        out += np.array([partial], dtype=np.uint32)

    # print(hex(out[0]))
    
    return out