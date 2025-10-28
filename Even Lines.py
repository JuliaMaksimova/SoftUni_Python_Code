import string

even_words = []

with open('even.txt') as file:  #-I was quick to judge him, but it wasn't his fault. -Is this some kind of joke?! Is it? -Quick, hide here. It is safer.
    text = file.read()
    text_by_word = text.split()
    with open('new_file.txt', 'w') as f:
        for word in text_by_word:
            clean_word = word.strip(string.punctuation)
            if len(clean_word) % 2 == 0:
                even_words.append(clean_word)

print(even_words[::-1])
