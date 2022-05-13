"""
A python implementation of SHA-256

Copyright (c) 2022 Valerio Spinogatti
Licensed under GNU license
"""


import functions as f 


INPUT = b"ciaozziadoivnraonisifjfffffffffffffffffffffffffffffffffffffffffffffffffffff"

def main():
    n_chunks, chunks = f.preprocess(INPUT)


if __name__ == "__main__":
    main()