from collections import deque

names = input()
queue = deque()

while not names == "End":
    if names != "Paid":
        queue.append(names)
    elif names == "Paid":
        while len(queue)>0:
            print(queue.popleft())

    names = input()

print(len(queue))