import numpy as np
import string
import random



def debug_print_chunks(chunks: np.ndarray) -> None:
    """
    Utility function for debug.
    Prints each chunk in a nice
    way.
    """

    for _, chunk in enumerate(chunks):
        for byte in chunk:
            print(f"{hex(byte)}\t", end="")
        
        print("\n")


    
def debug_print_h(h: np.ndarray) -> None:
    """
    Utility function for debugging.
    Prints the final 8 hash values
    nicely."""

    print(f"index\tvalue")
    
    for idx, val in enumerate(h):
        print(f"{idx}\t{hex(val)}")



def string_generator():
    """
    Utility function for testing.
    Generates random strings to
    be fed to the function that
    computes the hash.
    """

    # Random len
    lenght = random.randint(1, 20)
    # Generate string with random printable chars
    s = ''.join(random.choices(string.printable, k = lenght))
    return s



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



def rightrotate(a: np.uint32, amount: int) -> int:
    """
    Rotates the input bitwise toward
    the right. The input must be a
    uint32 value.
    """
    
    if amount > 32:
        raise OSError("amount must be <= 32")
    
    temp1 = a >> amount
    temp2 = a << (32 - amount)
    out = temp1 + temp2

    return out



def add_mod_2tothe32(*args) -> int:
    """
    Performs the addition modulo 2^32
    of an arbitrary number of inputs,
    modulo 2^32.
    """

    modulus = pow(2,32)
    sum = 0

    for arg in args:
        sum += int(arg)

    sum = sum % modulus

    return sum 


