number_of_commands = int(input())

cars = set()

for _ in range (number_of_commands):
    command, car_number = input().split(", ")
    if command == "IN":
        cars.add(car_number)
    else:
        cars.remove(car_number)

if len(cars)>0:
    [print(item) for item in cars]
else:
    print("Parking Lot is Empty")