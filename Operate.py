from functools import reduce

def operate(operator, *numbers):
    if operator == "+":
        result = sum(numbers)
    elif operator == "-":
        result = reduce(lambda x,y: x-y, numbers)
    elif operator == "*":
        result = reduce(lambda x,y: x*y, numbers)
    else:
        result = reduce(lambda x,y: x/y, numbers)

    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))