command = input()
numbers = [int(el) for el in input().split()]

odd = []
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if command == "Odd":
    print(f"The sum of all odd numbers is: {'+'.join(str(n) for n in odd) + ' =' } {sum(odd)} ")
    print(f"Multiply the sum: {sum(odd)}*{len(numbers)} = {sum(odd)*len(numbers)}")
elif command == "Even":
    print(f"The sum of all even numbers is: {'+'.join(str(n) for n in even) + '=' } {sum(even)} ")
    print(f"Multiply the sum: {sum(even)}*{len(numbers)} = {sum(even) * len(numbers)}")