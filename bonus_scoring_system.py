number_of_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
higher_attendance = 0

for _ in range(number_of_students):
    attendances = int(input())
    if higher_attendance < attendances:
        higher_attendance = attendances

    current_bonus = attendances / number_of_the_lectures * (5 + additional_bonus)

    if max_bonus < current_bonus:
        max_bonus = current_bonus

    current_bonus = 0

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {higher_attendance} lectures.")