def multiply(*numbers):
    current_sum = 1
    for el in numbers:
        current_sum *= el
    return current_sum


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))