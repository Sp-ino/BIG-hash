"""
A python implementation of SHA-256

Copyright (c) 2022 Valerio Spinogatti
Licensed under GNU license
"""

import functions as f 
from hashlib import sha256
import string
import random

##--------------------  Function for testing --------------------## 

def stringGenerator():
    # Random len
    lenght = random.randint(1, 20)
    # Generate string with random printable chars
    s = ''.join(random.choices(string.printable, k = lenght))
    return s
        


def test():
    # counter for wrong hashes
    print("[*] Starting the BIG test")
    counter = 0
    wrong = []
    # Try to generate 100 hash from random string and compare them
    for i in range(100):
      
        print(f"\r[+] Testing: {i + 1}%", end='')
      
        # Generate a random string
        s = stringGenerator()
        # Compute hashlib hash
        originalSha= sha256(s.encode()).hexdigest()
        # Compute custom hash
        bigSha = f.sha256(s)
        
        # Check if they match
        if(originalSha != bigSha):
            #print("[-] Error, hash doesn't match on: {}\n Original sha256 {}\n Big sha256 {}\n".format(s, originalSha, bigSha))
            counter+=1
            wrong.append({"big": bigSha, "original": originalSha, "s": s})

    # Print result   
    if wrong == 0:
        print("\n[+] Success: all 100 hash match")

    else:
        print("\n[-] Error: {} hashes don't match".format(counter))
        for item in wrong:
            print("[-] Error in:\n Input string: {}\n Original sha256: {}\n Big sha256: {}".format(item.get("s"), item.get("original"), item.get("big")))

if __name__ == "__main__":
    test()