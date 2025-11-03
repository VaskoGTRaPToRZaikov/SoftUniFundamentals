contest_pass_dictionary = {}


while True:
    contest_input = input().split(":")

    if len(contest_input) == 1:
        break

    contest, password = contest_input

    contest_pass_dictionary[contest] = password

ranking_dictionary = {}

while True:
    submissions_input = input().split("=>")

    if len(submissions_input) == 1:
        break

    current_contest, current_password, username, points = (
        submissions_input[0], submissions_input[1], submissions_input[2], int(submissions_input[3]))

    if current_contest not in contest_pass_dictionary.keys():
        continue
    if contest_pass_dictionary[current_contest] != current_password:
        continue

    if username not in ranking_dictionary.keys():
        ranking_dictionary[username] = {}

    if current_contest not in ranking_dictionary[username]:
        ranking_dictionary[username][current_contest] = points

    else:
        if points > ranking_dictionary[username][current_contest]:
            ranking_dictionary[username][current_contest] = points

best_student = ""
max_points = 0

for user, user_contest in ranking_dictionary.items():
    total_points = sum(user_contest.values())
    if total_points > max_points:
        max_points = total_points
        best_student = user

print(f"Best candidate is {best_student} with total {max_points} points.")
print("Ranking:")
sorted_students = sorted(ranking_dictionary.items())

for name, contests in sorted_students:
    print(name)
    sorted_contests = sorted(contests.items(), key=lambda x: -x[1])
    for sort_contest, sort_points in sorted_contests:
        print(f"#  {sort_contest} -> {sort_points}")