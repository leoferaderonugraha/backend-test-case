import ast
import sys
import typing as t


def matrix_diagonal_sum(matrix: t.List[t.List[int]]) -> int:
    left_to_right = 0
    right_to_left = len(matrix) - 1

    diagonal_left_sum = 0
    diagonal_right_sum = 0

    for i in range(len(matrix)):
        diagonal_left_sum += matrix[i][left_to_right]
        left_to_right += 1
        diagonal_right_sum += matrix[i][right_to_left]
        right_to_left -= 1

    return diagonal_left_sum - diagonal_right_sum


if len(sys.argv) < 2:
    file_name = sys.argv[0]
    print(f'Usage: {file_name} "matrix" ')
    print(f'Example: python3 {file_name} "[[1, 2, 0], [4, 5, 6], [7, 8, 9]]"')

    exit(0)

matrix = ast.literal_eval(sys.argv[1])

print('diagonal sum:', matrix_diagonal_sum(matrix))
