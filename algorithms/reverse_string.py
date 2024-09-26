import sys
import re


def reverse(arg: str) -> str:
    alphabets = re.search(r"^[a-zA-Z]+", arg)
    digits = re.search(r"\d+$", arg)
    result = ''  # to satisfy type checker

    if alphabets is not None:
        result += alphabets.group()[::-1]

    if digits is not None:
        result += digits.group()

    return result


if len(sys.argv) < 2:
    file_name = sys.argv[0]
    print(f'Usage: {sys.argv[0]} <string>')
    print(f'Example: python3 {file_name} NEGIE1')
    exit(0)


arg = sys.argv[1]
print(f"{arg} -> {reverse(arg)}")
