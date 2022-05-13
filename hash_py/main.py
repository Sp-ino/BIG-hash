"""
A python implementation of SHA-256

Copyright (c) 2022 Valerio Spinogatti
Licensed under GNU license
"""


import functions as f 


INPUT = "hello world"

def main():
    chunks = f.preprocess(INPUT)
    print(chunks)


if __name__ == "__main__":
    main()