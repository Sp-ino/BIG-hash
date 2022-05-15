import operator
import string
import random
##-------------------- Utils Functions to handle string and bits --------------------## 

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

##--------------------  Logic funcionts for array of bits --------------------## 

#and - both arguments need to be true
def AND(i, j): return [ia and ja for ia, ja in zip(i,j)] 

#simply negates argument
def NOT(i): return [int(not x) for x in i]

#retrun true if either i or j is true but not both at the same time
def XOR(i, j): return [operator.xor(ia, ja) for ia, ja in zip(i, j)]

def XORXOR(i, j, l): return [operator.xor(ia, operator.xor(ja, la)) for ia, ja, la, in zip(i, j, l)]

# rotate right
def rotr(x, n): return x[-n:] + x[:-n]
# shift right
def shr(x, n): return n * [0] + x[:-n]

# Full adder
def add(i, j):
  #takes to lists of binaries and adds them
  sums = list(range(len(i)))
  #initial input needs an carry over bit as 0
  c = 0
  for x in range(len(i)-1,-1,-1):
    #add the inout bits with a double xor gate
    sums[x] = operator.xor(i[x], operator.xor(j[x], c)) 
    #carry over bit is equal the most represented, e.g., output = 0,1,0 
    # then 0 is the carry over bit
    c = max([i[x], j[x],], key=[i[x],j[x],c].count)

  #returns list of bits 
  return sums


##--------------------  Function for testing --------------------## 

def stringGenerator():
    lenght = random.randint(1, 20)
    s = ''.join(random.choices(string.ascii_letters + string.digits, k = lenght))
    return s