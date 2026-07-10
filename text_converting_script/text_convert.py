import re
from pathlib import Path

INPUT_FILE = Path("text_converting_script\input.txt")
OUTPUT_FILE = Path("text_converting_script\converted.txt")

# ==========================================================


NARRATION_PATTERN = re.compile(
    r'^"(?:[^"\\]|\\.)*"\s*$'
)

DIALOGUE_PATTERN = re.compile(
    r'^[A-Za-z_]\w*(?:\s+[@A-Za-z_][\w.-]*)*\s+"(?:[^"\\]|\\.)*"\s*$'
)


def is_dialogue_or_narration(line: str) -> bool:
    return (
        bool(NARRATION_PATTERN.fullmatch(line))
        or bool(DIALOGUE_PATTERN.fullmatch(line))
    )


def clean_renpy_text(text: str) -> str:
    cleaned = []

    for raw_line in text.splitlines():
        line = raw_line.lstrip()

        if NARRATION_PATTERN.fullmatch(line):
            # Remove the surrounding quotes.
            cleaned.append(line[1:-1])

        elif DIALOGUE_PATTERN.fullmatch(line):
            # Keep dialogue exactly as-is.
            cleaned.append(line)

    return "\n".join(cleaned)


def main():
    text = INPUT_FILE.read_text(encoding="utf-8")

    cleaned = clean_renpy_text(text)

    OUTPUT_FILE.write_text(cleaned, encoding="utf-8")

    print(f"Extracted {len(cleaned.splitlines())} lines.")


if __name__ == "__main__":
    main()