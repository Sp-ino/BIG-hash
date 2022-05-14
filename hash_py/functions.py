
from utils import *

def preprocess(message):
    # From string to bits
    bits = get_bits(message)
    lenght = len(bits)

    # 64 bits that representing the lenght of the message
    L = [int(b) for b in bin(lenght)[2:].zfill(64)]

    while(len(bits)+64) % 512 != 0:
        bits.append(0)

    # Add L to message
    bits+= L
    # Returns it in 512 chunks
    return chunker(bits, 512)