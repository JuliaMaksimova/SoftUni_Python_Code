# char = input()
# vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
#
# no_vowels = [element for element in char if element not in vowels]
# print("".join(no_vowels))

# def no_vowels(charecters):
#     if charecters.lower() not in "aeiou":
#         return True
#     return False
#
#
# print("".join([element for element in input() if no_vowels(element)]))


no_vowels = [element for element in input() if element not in "aeiouAEIOU"]
print("".join(no_vowels))gi