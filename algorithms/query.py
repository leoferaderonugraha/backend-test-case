import sys
import typing as t


# just a simple implementation for the requirements
def count(source: t.List[object], target: object) -> int:
    counter = 0

    for s in source:
        if s == target:
            counter += 1

    return counter


def query(source: t.List[str], targets: t.List[str]) -> t.List[int]:
    return [
        source.count(target)  # used the builtin function; for efficiency
        for target in targets
    ]


if len(sys.argv) < 3:
    file_name = sys.argv[0]
    print(f'Usage: {file_name} "source" ')
    print(f"Example: python3 {file_name} "
          '"xc dz bbb dz" "bbb ac dz"')
    exit(0)


source = sys.argv[1]
targets = sys.argv[2]

result = query(source.split(), targets.split())

print('result:', result)
