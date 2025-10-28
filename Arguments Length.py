def args_length(*args):
    counter = 0
    for el in args:
        counter+=1
    return counter

def concatenate(*args):
    leters = []
    for el in args:
        leters.append(el)
    return ("".join(leters))

print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))

print(concatenate("Soft", "Uni", "Is", "Great", "!"))