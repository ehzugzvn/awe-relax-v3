"""Entry for make-the-ai-judge-feel-awe: a short meditation on tide and moon."""

import os

TEXT = "Twice a day the sea lays itself along the shore and rests there, breathing out. The moon pulls; the water answers slowly, as it has since before there was anyone to watch. The beach keeps nothing. Everything is given back."


def main():
    # Self-check: the entry text must stay within the 1-280 code point limit.
    assert 1 <= len(TEXT) <= 280, f"TEXT length out of range: {len(TEXT)}"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
