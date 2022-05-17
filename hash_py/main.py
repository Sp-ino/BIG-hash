"""
A python implementation of SHA-256

Copyright (c) 2022 Valerio Spinogatti
Licensed under GNU license
"""

from hash_steps.hash_steps import compress, preprocess, create_message_schedule


INPUT = b"ciaozzi"

def main():
    input_bytes = preprocess(INPUT)
    chunks, n_chunks = create_message_schedule(input_bytes)
    accumulated_values = compress(chunks, n_chunks)

if __name__ == "__main__":
    main()