from collections import deque

petrol_pumps = int(input())
information_distance_liters = deque()

for i in range(petrol_pumps):
    information = [int(a) for a in input().split()]
    information_distance_liters.append(information)


for station in range(petrol_pumps):
    truck_fuel = 0
    completed = True
    for information in information_distance_liters:
        distance = information[1]
        fuel = information[0]
        truck_fuel +=fuel
        if distance>truck_fuel:
            completed = False
            break
    if completed:
        print(station)
        break
    else:
        information_distance_liters.append(information_distance_liters.popleft())