expression = input()
collection = []

for index in range (0, len(expression), 1):
    if expression[index] == "(":
        collection.append(index)
    elif expression[index] == ")":
        start_index = collection.pop()
        print(expression[start_index:index+1])
