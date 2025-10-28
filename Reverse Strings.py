# words = input()
# words_list = list(words)
# words_reversed = []
#
# while len(words_list)>0:
#     words_reversed.append(words_list.pop())
#
# print(f'Here is the result, using stack: {"".join(words_reversed)}')


numbers = input().split()
reverced_numbers = []

while len(numbers)>0:
    reverced_numbers.append(numbers.pop())

print(" ".join(reverced_numbers))
