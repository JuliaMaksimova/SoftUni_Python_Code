with open('words.txt', 'w') as f:
    f.write("-I was quick to judge him, but it wasn't his fault.\n"
            "-Is this some kind of joke?! Is it? -Quick, hide here…It is safer.\n"
            "-Is this some kind of joke?! Is it? -Quick, hide here…It is safer.\n")

with open('words.txt') as file:
    text = file.read()
    print(text)

file_by_word = text.split()

find_words = input().split() # some kind


for element in find_words:
    count = 0
    for words in file_by_word:
        if element == words:
            count +=1
    with open("words.txt", 'a') as f:
        f.write(f"{count} {element}\n")


with open('words.txt') as file:
    text = file.read()
    print(text)



