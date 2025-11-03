courses = {}

while True:
    command = input()

    if command == "end":
        break

    elements = command.split(" : ")
    course, student = elements[0], elements[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for course_name, info in courses.items():
    registered_students = len(info)
    print(f"{course_name}: {registered_students}")
    for student_name in info:
        print(f"-- {student_name}")
