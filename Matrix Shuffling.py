row,collum = [int(i) for i in input().split()]

matrix = []

for j in range(row):
    matrix.append([int(i) for i in input().split()])

for element in matrix:
    print(" ".join(map(str, element)))

matrix_new = matrix
command = input()
valid = True


while not command == "END":
    command = command.split()
    command_digits = [int(i) for i in command[1:]]
    r1, c1, r2, c2 = command_digits
    for i in range(0, len(command_digits), 2):
        if not (0 <= command_digits[i] < row and 0 <= command_digits[i + 1] < collum):
            valid = False
            break
    if command[0] == "swap" and valid:
        matrix[r1][c1],matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        for element in matrix:
            print(" ".join(map(str, element)))
    elif command != "swap" or valid == False:
        print("Invalid input")

    valid = True
    command = input()
