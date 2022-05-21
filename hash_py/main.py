"""
Test script for our python implementation of SHA-256

Copyright (c) 2022 Luca Azzinari, Daniele De Menna and Valerio Spinogatti
Licensed under GNU license
"""

from bighash.functional import big_sha256
from bighash.utils import string_generator
from hashlib import sha256



def test():
    """
    Test function that verifies
    the proper functionality of
    our implementation of SHA-256,
    that is, the big_sha256 function.
    """

    # counter for wrong hashes
    print("[*] Starting the BIG test")
    counter = 0
    wrong = []
    # Try to generate 100 hash from random string and compare them
    for i in range(100):
      
        print(f"\r[+] Testing: {i + 1}%", end='')
      
        # Generate a random string
        s = string_generator()
        # Compute hashlib hash
        originalSha= sha256(s.encode()).hexdigest()
        # Compute custom hash
        bigSha = big_sha256(s)
        
        # Check if they match
        if(originalSha != bigSha):
            #print("[-] Error, hash doesn't match on: {}\n Original sha256 {}\n Big sha256 {}\n".format(s, originalSha, bigSha))
            counter+=1
            wrong.append({"big": bigSha, "original": originalSha, "s": s})

    # Print result   
    if counter == 0:
        print("\n[+] Success: all 100 hash match")

    else:
        print("\n[-] Error: {} hashes don't match".format(counter))
        for item in wrong:
            print("[-] Error in:\n Input string: {}\n Original sha256:\t{}\n Big sha256:\t\t{}".format(item.get("s"), item.get("original"), item.get("big")))



if __name__ == "__main__":
    test()