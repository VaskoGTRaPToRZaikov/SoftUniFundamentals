peoples = input().split()
persons = int(input())

executed = []
current_index = 0
no_more_peoples = False

while True:
    if len(peoples) <= 0:
        no_more_peoples = True
        break

    else:
        current_index = (current_index + persons - 1) % len(peoples)
        executed.append(peoples.pop(current_index))

        if current_index == len(peoples):
            current_index = 0

print("[" + ",".join(executed) + "]")
