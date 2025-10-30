students = {}
while True:
    information = input()

    if ":" not in information:
        name_of_course = information.split("_")
        course_to_find = ' '.join(name_of_course)
        break

    name, student_id, course = information.split(":")
    students[name] = {"student_id": student_id, "course": course}

for names, info in students.items():
    if info["course"] == course_to_find:
        print(f"{names} - {info['student_id']}")