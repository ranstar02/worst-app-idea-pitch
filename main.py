"""Worst app idea ever pitched: SockSync."""

ENTRY = (
    "SockSync alerts you the instant one sock in a pair starts feeling "
    "emotionally distant, so you can schedule a reconciliation walk before "
    "laundry day destroys the relationship forever."
)


def main():
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    try:
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        path = "./output/entry.txt"
        import os

        os.makedirs("./output", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"written to: {path}")


if __name__ == "__main__":
    main()
