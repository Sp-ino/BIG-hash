"""
A python implementation of SHA-256

Copyright (c) 2022 Valerio Spinogatti
Licensed under GNU license
"""

import functions as f 


INPUT = b"ciaozzi"

def main():
    input_bytes = f.preprocess(INPUT)
    chunks, n_chunks = f.create_message_schedule(input_bytes)



if __name__ == "__main__":
    main()