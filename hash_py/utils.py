def debug_print_chunks(chunks: list) -> None:
    for idx, byte in enumerate(chunks):
        if idx % 512 == 0:
            print(f"\n\nChunk {idx//512}:") 
        if idx % 8 == 0:
            print(f"\nRow {idx//8} ")

        print(f"{hex(byte)}\t", end="")

