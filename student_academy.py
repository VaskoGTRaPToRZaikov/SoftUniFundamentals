number_of_students = int(input())
student_dictionary = {}

for _ in range(number_of_students):
    student_name = input()
    grade = float(input())

    if student_name not in student_dictionary:
        student_dictionary[student_name] = []
    student_dictionary[student_name].append(grade)
for_remove = []

for name, grades in student_dictionary.items():
    if len(grades) > 1:
        average_grade = sum(grades) / 2
    else:
        average_grade = grades[0]

    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
    else:
        for_remove.append(name)

for student in for_remove:
    del student_dictionary[student]

