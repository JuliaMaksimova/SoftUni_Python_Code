number_of_names = int(input())

all_names = set()

for _ in range (number_of_names):
    name = input()
    all_names.add(name)

[print(item) for item in all_names]