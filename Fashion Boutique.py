from collections import deque

clothes = deque(map(int, input().split()))
max_rack_capacity = int(input())
rack_capacity = max_rack_capacity
number_of_racks = 1

for i in range(len(clothes)):
    current_peace = clothes.popleft()
    if rack_capacity >= current_peace:
        rack_capacity-=current_peace
    else:
        number_of_racks+=1
        rack_capacity= max_rack_capacity
        rack_capacity -= current_peace

print(number_of_racks)