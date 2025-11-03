company_users = {}

while True:
    command = input()

    if command == "End":
        break

    elements = command.split(" -> ")
    company_name = elements[0]
    employee_id = elements[1]

    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

for name, employees in company_users.items():
    print(name)
    for employee in employees:
        print(f"-- {employee}")
