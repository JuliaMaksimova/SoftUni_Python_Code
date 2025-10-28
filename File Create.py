import os

file = open('my_first_file.txt', 'w')
file.write('I just created my first file!')
file.close()

file = open('my_first_file.txt')
print(file.read())
file.close()

try:
    os.remove('my_first_file.txt')
    print("file deleted")
except:
    print("'File already deleted!'.")
