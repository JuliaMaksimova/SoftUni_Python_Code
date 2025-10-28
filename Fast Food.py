from collections import deque

amount_of_food = int(input())
quantity_of_orders = deque(int(i) for i in input().split())
enought_orders = True

print(max(quantity_of_orders))

for orders in range(len(quantity_of_orders)):
    first_order = quantity_of_orders.popleft()
    amount_of_food = amount_of_food - first_order
    if amount_of_food<0:
        print(f"Orders left: {first_order} {' '.join(map(str, quantity_of_orders))}")
        enought_orders=False
        break

if enought_orders:
    print("Orders complete")



