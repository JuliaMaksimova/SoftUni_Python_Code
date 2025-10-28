numbers = tuple(float(n) for n in input().split())

count_numbers = {}

for element in numbers:
    if element not in count_numbers:
        count_numbers[element] = 1
    else:
        count_numbers[element] += 1


[print(f"{key} - {value} times") for key,value in count_numbers.items()]

