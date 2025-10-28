numbers = [int(el) for el in input().split()]

print(list(filter(lambda x: x % 2 == 0, numbers)))
print(sorted(numbers, reverse=False))
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum is {sum(numbers)}")
