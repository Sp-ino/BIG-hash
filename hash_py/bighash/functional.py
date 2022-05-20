"""
A python implementation of SHA-256

Copyright (c) 2022 Luca Azzinari, Daniele De Menna and Valerio Spinogatti
Licensed under GNU license
"""

from bighash.steps import preprocess, create_message_schedule, compress, hexdigest
from bighash.utils import debug_print_h



def big_sha256(message: str) -> str:
    """
    Compute the hash of the
    input string according
    to SHA-256 algorithm.
    """
    
    input_bytes = preprocess(message)
    chunks, n_chunks = create_message_schedule(input_bytes)
    hash_values = compress(chunks, n_chunks)
    # debug_print_h(hash_values)
    out = hexdigest(hash_values)

    return out



