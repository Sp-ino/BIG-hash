import numpy as np



def rightrotate(a: np.uint32, amount: int) -> np.uint32:
    
    if amount > 32:
        raise OSError("amount must be <= 32")
    
    temp1 = a >> amount
    temp2 = a << (32 - amount)
    out = temp1 + temp2

    return out



def add_mod_2tothe32(*args) -> np.uint32:
    modulus = pow(2,32)
    sum = 0

    for arg in args:
        sum += int(arg)

    sum = sum % modulus

    return sum 



def debug_print_chunks(chunks: np.ndarray) -> None:
    for idx, byte in enumerate(chunks):
        if idx % 512 == 0:
            print(f"\n\nChunk {idx//512}:") 
        if idx % 8 == 0:
            print(f"\nRow {idx//8} ")

        print(f"{hex(byte)}\t", end="")

    
def debug_print_h(h: np.ndarray) -> None:
    print(f"index\tvalue")
    
    for idx, val in enumerate(h):
        print(f"{idx}\t{hex(val)}")