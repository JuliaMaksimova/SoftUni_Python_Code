number_of_students = int(input())

record = {}

for _ in range(number_of_students):
    student, grade = input().split()
    grade = float(grade)
    if student not in record:
        record[student] = set()
    record[student].add(grade)


for key,value in record.items():
    average_grade = sum(value)/len(value)
    marks = ' '.join(str(n) for n in value)
    print(f"{key} -> {marks}, (avr: {average_grade:.2f})")