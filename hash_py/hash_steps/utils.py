import numpy as np



def rightrotate(a: np.uint32, amount: int) -> np.uint32:
    
    if amount > 32:
        raise OSError("amount must be <= 32")
    
    temp1 = a >> amount
    temp2 = a << (32 - amount)
    out = temp1 + temp2

    return out



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

    if arr.shape[0] != 4 or len(arr.shape) != 1:
        raise OSError("arr must be a np.ndarray of shape (4,)")

    out = np.array([0], dtype=np.uint32)
    for idx, byte in enumerate(arr):
        partial = np.uint32(byte)
        partial = partial << 8 * (3 - idx)
        out += np.array([partial], dtype=np.uint32)
    
    return out



def fill_schedule_values(w: np.ndarray) -> np.ndarray:
    """
    Implements schedule loop
    on a chunk made of 64 uint32
    values.
    """

    if w.shape[0] != 64 or len(w.shape) != 1:
        raise OSError("Input size must be (64,)")

    for idx in range(16,64):
        s0 = rightrotate(w[idx-15], 7) ^ rightrotate(w[idx-15], 18) ^ (w[idx-15] >> 3)
        s1 = rightrotate(w[idx- 2], 17) ^ rightrotate(w[idx- 2], 19) ^ (w[idx- 2] >> 10)
        w[idx] = w[idx-16] + s0 + w[idx-7] + s1

    return w



def compression_step(h: np.ndarray, w: np.ndarray, k: np.ndarray) ->  np.ndarray:
    """
    Performs a step of the SHA256 compression
    loop. w represents the chunk and k is
    the message schedule.
    """

    if h.shape[0] != 8 or len(h.shape) != 1:
        raise OSError("Input size must be (64,)")


    if w.shape[0] != 64 or len(w.shape) != 1:
        raise OSError("Input size must be (64,)")

    if k.shape[0] != 64 or len(k.shape) != 1:
        raise OSError("Input size must be (64,)")

    for i in range(64):
        s1 = rightrotate(h[4], 6) ^ rightrotate(h[4], 11) ^ rightrotate(h[4], 25)
        ch = (h[4] & h[5]) ^ ((~ h[4]) & h[6])
        temp1 = h[7] + s1 + ch + k[i] + w[i]
        s2 = rightrotate(h[0], 2) ^ rightrotate(h[0], 13) ^ rightrotate(h[0], 22)
        maj = (h[0] & h[1]) ^ (h[0] & h[2]) ^ (h[1] & h[2])
        temp2 = s2 + maj
        h[7] = h[6]
        h[6] = h[5]
        h[5] = h[4]
        h[4] = h[3] + temp1
        h[3] = h[2]
        h[2] = h[1]
        h[1] = h[0]
        h[0] = temp1 + temp2

    