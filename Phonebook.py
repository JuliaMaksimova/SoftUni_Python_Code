name_phone = input()
phonebook = {}
searched_names = set()

while not name_phone.isdigit():
    key, value = name_phone.split("-")
    phonebook[key] = value
    name_phone = input()

for _ in range (int(name_phone)):
    name = input()
    searched_names.add(name)

for name in searched_names:
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist")