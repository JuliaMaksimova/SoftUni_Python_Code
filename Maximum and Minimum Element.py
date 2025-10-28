number = int(input())
stack = []

for sequence in range(number):
    query = input()
    if query.startswith("1"):
        query = query.split()
        stack.append(query[-1])
    elif query == "2":
        if len(stack)>0:
            stack.pop()
        pass
    elif query == "3":
        print(f"Min is {min(stack)}")
    elif query == "4":
        print(f"Max is {max(stack)}")

stack = stack[::-1]
print(" ".join(stack))