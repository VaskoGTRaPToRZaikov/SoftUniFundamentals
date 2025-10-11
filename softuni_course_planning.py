def add(lesson):
    if lesson not in schedule_lessons:
        schedule_lessons.append(lesson)

    return schedule_lessons

def insert(lesson, insert_index):
    if lesson not in schedule_lessons:
        schedule_lessons.insert(insert_index, lesson)

    return schedule_lessons

def remove(lesson):
    lesson_exercise = f"{lesson}-Exercise"
    if lesson in schedule_lessons:
        if lesson_exercise in schedule_lessons:
            schedule_lessons.remove(lesson_exercise)
            schedule_lessons.remove(lesson)
        else:
            schedule_lessons.remove(lesson)

    return schedule_lessons

def swap(first_lesson, second_lesson):
    if first_lesson in schedule_lessons and second_lesson in schedule_lessons:
        first_index = schedule_lessons.index(first_lesson)
        second_index = schedule_lessons.index(second_lesson)

        first_lesson_exercise = f"{first_lesson}-Exercise"
        second_lesson_exercise = f"{second_lesson}-Exercise"

        schedule_lessons[first_index], schedule_lessons[second_index] = \
            schedule_lessons[second_index], schedule_lessons[first_index]

        first_ex_exists = first_lesson_exercise in schedule_lessons
        second_ex_exists = second_lesson_exercise in schedule_lessons

        if first_ex_exists:
            schedule_lessons.remove(first_lesson_exercise)
        if second_ex_exists:
            schedule_lessons.remove(second_lesson_exercise)

        if first_ex_exists:
            new_first_index = schedule_lessons.index(first_lesson)
            schedule_lessons.insert(new_first_index + 1, first_lesson_exercise)

        if second_ex_exists:
            new_second_index = schedule_lessons.index(second_lesson)
            schedule_lessons.insert(new_second_index + 1, second_lesson_exercise)


    return schedule_lessons

def exercise(lesson):
    lesson_exercise = f"{lesson}-Exercise"
    if lesson in schedule_lessons:
        if lesson_exercise not in schedule_lessons:
            insert_index = schedule_lessons.index(lesson)
            schedule_lessons.insert(insert_index + 1, lesson_exercise)
    else:
        schedule_lessons.append(lesson)
        schedule_lessons.append(lesson_exercise)

    return schedule_lessons

schedule_lessons = input().split(", ")

while True:
    command = input()

    if command == 'course start':
        break

    instructions = command.split(":")
    action = instructions[0]
    lesson_title = instructions[1]

    if action == "Add":
        schedule_lessons = add(lesson_title)

    elif action == "Insert":
        index = int(instructions[2])
        schedule_lessons = insert(lesson_title, index)

    elif action == "Remove":
        schedule_lessons = remove(lesson_title)

    elif action == "Swap":
        lesson_for_swap = instructions[2]
        schedule_lessons = swap(lesson_title, lesson_for_swap)

    elif action == "Exercise":
        schedule_lessons = exercise(lesson_title)

for i in range(1, len(schedule_lessons) + 1):
    print(f"{i}.{schedule_lessons[i - 1]}")
