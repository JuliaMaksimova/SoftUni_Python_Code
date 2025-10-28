size = int(input())

matrix = []

for col in range(size):
    matrix.append(list(input()))

print(matrix)

symbol = input()
position = None

for row in range(size):
    for col in range(size):
        if matrix[row][col] == symbol:
            position = (row, col)
        break
    if position:
        break

print(position if position else f"'{symbol}'not found.")




