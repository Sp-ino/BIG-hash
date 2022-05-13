
from utils import *

def preprocess(message):
    # From string to bits
    bits = get_bits(message)
    lenght = len(bits)

    # 64 bits that representing the lenght of the message
    L = [int(b) for b in bin(lenght)[2:].zfill(64)]

    # Append the single 1
    bits.append(1)
    # if lenght is less then 512 - 64 then fill up to 512 - 64
    if lenght < 448:
        # add zeros    
        bits = fillzeros(bits, 448)
        # add L
    # else if lenght less then 512 and greater then 448 fill up to 1024 - 64
    elif 448 <= lenght <= 512:
        # add zeroes
        bits = fillzeros(bits, 960)

    # else fill up until len + 64 is multiple of 512
    else:
        while(len(bits)+64) % 512 != 0:
            bits.append(0)

    # Add L to message
    bits+= L
    # Returns it in 512 chunks
    return chunker(bits, 512)