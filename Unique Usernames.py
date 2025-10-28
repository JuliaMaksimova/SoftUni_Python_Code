number_of_entries = int(input())

collection_usernames = set()

for _ in range (number_of_entries):
    username = input()
    collection_usernames.add(username)


[print(user) for user in collection_usernames]