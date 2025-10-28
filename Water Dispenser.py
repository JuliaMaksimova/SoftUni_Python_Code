from collections import deque

qantity_wather = int(input())
name = input()

people = deque()

while not name == "Start":
    people.append(name)
    name = input()

command = input()

while not command =="End":
    if command.startswith("refill"):
        qantity_wather+=int(command[-1])
    else:
        water = int(command)
        if qantity_wather>= water:
            qantity_wather -= water
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

    command = input()

print(f"{qantity_wather} liters left.")




