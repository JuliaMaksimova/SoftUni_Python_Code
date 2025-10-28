from collections import deque

names = deque(input().split())
tosses = int(input())


while len(names)>1:
    names.rotate(-tosses)
    print(f"Removed {names.pop()}")

print(f"Last is {names.pop()}")
