# file = open('test.txt')

# try:
#     second_file = open("test.txt")
#     print("The file is found")
# except FileNotFoundError:
#     print("The file 'text.txt' is not found")
# finally:
#     print("Exit")
#
# print(second_file.read())

numbers = open('numbers.txt', 'w')

for number in range(1,6):
    numbers.write(f"{number}\n")
numbers.close()

numbers = open("numbers.txt")

sum = 0
for number in numbers:
    sum+=int(number)
print(sum)



