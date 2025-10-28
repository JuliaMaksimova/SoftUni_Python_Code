row, col = [int(i)for i in input().split(", ")]

matrix = []
total_sum = 0

for i in range (row):
    matrix.append([int(i)for i in input().split(", ")])
    total_sum += sum(matrix[i])

print(total_sum)
print(matrix)
