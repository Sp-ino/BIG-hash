import numpy as np



def rightrotate(a: np.uint32, amount: int) -> int:
    
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
    for _, chunk in enumerate(chunks):
        for byte in chunk:
            print(f"{hex(byte)}\t", end="")
        
        print("\n")


    
def debug_print_h(h: np.ndarray) -> None:
    print(f"index\tvalue")
    
    for idx, val in enumerate(h):
        print(f"{idx}\t{hex(val)}")