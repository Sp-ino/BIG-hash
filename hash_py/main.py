"""
A python implementation of SHA-256

Copyright (c) 2022 Valerio Spinogatti
Licensed under GNU license
"""

from hash_steps.steps import compress, preprocess, create_message_schedule
from hash_steps.utils import debug_print_h



INPUT = b"hello world"

def main():
    input_bytes = preprocess(INPUT)
    chunks, n_chunks = create_message_schedule(input_bytes)
    hash_values = compress(chunks, n_chunks)
    debug_print_h(hash_values)



if __name__ == "__main__":
    main()