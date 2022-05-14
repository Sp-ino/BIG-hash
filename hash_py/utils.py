## String to array of bit

def get_bits(m):
    unicode = [ord(c) for c in m]
    bytes = []
    bits = []
    for char in unicode:
        bytes.append(bin(char)[2:].zfill(8))

    for byte in bytes:
        for bit in byte:
            bits.append(int(bit))
    
    return bits

# split in chunks
def chunker (bits, chunk_lenght):
    chunked = []
    for b in range(0, len(bits), chunk_lenght):
        chunked.append(bits[b:b+chunk_lenght])
    
    return chunked

