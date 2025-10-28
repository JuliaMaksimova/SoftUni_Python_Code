row, col = [int(i) for i in input().split(", ")]

matrix = []

for rows in range (row):
    matrix.append([int(i) for i in input().split()])
print(matrix)

for colums in range(col):
    current_sum = 0
    for rows in range(row):
        current_sum += (matrix[rows][colums])
    print(current_sum)





