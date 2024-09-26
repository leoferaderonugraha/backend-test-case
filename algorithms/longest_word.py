import sys
import typing as t


def longest(arg: t.List[str]) -> t.Optional[str]:
    max_len = float('-inf')
    longest_word = None

    for word in arg:
        # nitpick: potentially save a fraction of ms
        word_length = len(word)

        if word_length > max_len:
            max_len = word_length
            longest_word = word

    return longest_word


if len(sys.argv) < 2:
    file_name = sys.argv[0]
    print(f'Usage: {file_name} "string"')
    print(f'Example: python3 {file_name} "a ab c def g hijkl"')
    exit(0)


arg = sys.argv[1]

longest_word = longest(arg.split())
if longest_word is not None:
    print('The longest word is:', longest_word)
