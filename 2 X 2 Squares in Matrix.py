row, col = [int(i) for i in input().split()]

matrix = []

for i in range(row):
    colum = input().split()
    matrix.append(colum)

count = 0

for i in range((len(matrix))-1):
    for j in range((len(matrix[0]))-1):
        if matrix[i][j] == matrix[i+1][j] == matrix[i][j+1] == matrix[i+1][j+1]:
            count += 1


print(count)