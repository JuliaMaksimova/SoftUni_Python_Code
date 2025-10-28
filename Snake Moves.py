from collections import deque

def create_matrix(len_row, len_col):
    matrix = []
    for _ in range(len_row):
        row = []
        for _ in range(len_col):
            row.append("_")
        matrix.append(row)
    return matrix

row, col = [int(i) for i in input().split()]

matrix = create_matrix(row,col)

text = deque(input())

for r in range(row):
    if r % 2 == 0:
        for c in range(col):
            char = text.popleft()
            matrix[r][c] = char
            text.append(char)
    else:
        for c in range(col-1, -1, -1):
            char = text.popleft()
            matrix[r][c] = char
            text.append(char)

for r in range(row):
    print(''.join(matrix[r]))

