import os


def main():
    # Emit the one-line alibi to the output file with no trailing newline.
    entry = "I skipped the dust under your bed. My sensors counted 38 socks and classified it as a drawer."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(entry)


if __name__ == "__main__":
    main()
