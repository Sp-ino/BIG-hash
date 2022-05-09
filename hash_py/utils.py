def debug_print_chunks(chunks: list) -> None:
    for idx, byte in enumerate(chunks):
        if idx % 8 == 0:
            print("\n")
        if idx % 512 == 0:
            print(f"\n\nChunk {idx//512}:") 

        print(f"{hex(byte.value)}\t", end="")

