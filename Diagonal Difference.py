square_len = int(input())

matrix = []

for row in range(square_len):
    matrix.append([int(i) for i in input().split()])

left_sum = 0
right_sum = 0

for row in range (square_len):
    left_sum += matrix[row][row]
    right_sum += matrix[row][square_len - row - 1]


print(f"{abs(left_sum - right_sum)}")
