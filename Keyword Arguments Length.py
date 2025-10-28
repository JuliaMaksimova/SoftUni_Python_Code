# def kwargs_length(**kwargs):
#     return (len(kwargs))
#
# dictionary = {'name': 'Peter', 'age': 25}
#
# print(kwargs_length(**dictionary))

def age_assignment(*args,**kwargs):
    new_dictionary = {}
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            new_dictionary[name] = kwargs[first_letter]

    return new_dictionary


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))