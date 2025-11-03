users_dictionary = {}
submissions_dictionary = {}

while True:
    command = input().split("-")
    name = command[0]

    if len(command) == 1:
        break

    elif len(command) == 2:
        del users_dictionary[name]

    else:
        language = command[1]
        points = int(command[2])

        if name not in users_dictionary.keys():
         users_dictionary[name] = 0
        if points > users_dictionary[name]:
         users_dictionary[name] = points

        if language not in submissions_dictionary.keys():
            submissions_dictionary[language] = 0
        submissions_dictionary[language] += 1

print("Results:")
for user, score in users_dictionary.items():
    print(f"{user} | {score}")
print("Submissions:")
for submission, count in submissions_dictionary.items():
    print(f"{submission} - {count}")