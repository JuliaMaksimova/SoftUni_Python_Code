sqare_len = int(input())

matrix = []

for row in range(sqare_len):
    matrix.append([int(i) for i in input().split()])

total_sum = 0

for i in range(sqare_len):
    total_sum += matrix[i][i]

print(total_sum)


