row, col = [int(i) for i in input().split()]

matrix = []

for i in range(row):
    colum = [int(i) for i in input().split()]
    matrix.append(colum)

print(matrix)
maximum_sum = 0


for i in range(len(matrix)-2):
    for j in range(len(matrix[0])-2):
        current_sum = matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1]+ matrix[i][j+2] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if current_sum >= maximum_sum:
            maximum_sum = current_sum
            new_row = i
            new_col = j


print(f"The maximum sum is: {maximum_sum}.")


for r in range(3):
    for c in range(3):
        print(matrix[new_row+r][new_col+c], end='')
    print()







