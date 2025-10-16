first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_of_students = int(input())

overall_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hour = 0
time_needed = 0

while number_of_students:
    hour += 1
    time_needed += 1

    if hour % 4 == 0:
        continue

    if number_of_students >= overall_efficiency:
        number_of_students -= overall_efficiency
    else:
        number_of_students = 0


print(f"Time needed: {time_needed}h.")