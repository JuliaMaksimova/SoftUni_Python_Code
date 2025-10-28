number_of_guests = int(input())

invited_guests = set()
arrived_guests = set()

for _ in range(number_of_guests):
    guest = input()
    invited_guests.add(guest)

arrived = input()
while not arrived == "END":
    arrived_guests.add(arrived)
    arrived = input()

did_not_come = list(invited_guests - arrived_guests)
sorted_list = sorted(did_not_come, key=lambda x: (not x[0].isdigit(), x))

print(len(sorted_list))
[print(element) for element in sorted_list]



