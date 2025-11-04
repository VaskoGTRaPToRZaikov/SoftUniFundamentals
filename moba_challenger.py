overall_skills = {}
players_pool = {}

while True:
    command = input()

    if command == "Season end":
        break

    elif " vs " in command:
        players = command.split(" vs ")
        first_player, second_player = players
        if first_player in players_pool and second_player in players_pool:
            common_positions = set(players_pool[first_player].keys()) & set(players_pool[second_player].keys())
            if common_positions:
                if overall_skills[first_player] > overall_skills[second_player]:
                    del players_pool[second_player]
                    del overall_skills[second_player]
                elif overall_skills[first_player] < overall_skills[second_player]:
                    del players_pool[first_player]
                    del overall_skills[first_player]

    else:
        statistics = command.split(" -> ")
        name = statistics[0]
        position = statistics[1]
        skill = int(statistics[2])

        if name not in players_pool.keys():
            players_pool[name] = {}
            overall_skills[name] = 0

        if position not in players_pool[name]:
            players_pool[name][position] = skill
            overall_skills[name] += skill
        else:
            if skill > players_pool[name][position]:
                difference = skill - players_pool[name][position]
                players_pool[name][position] = skill
                overall_skills[name] += difference

sorted_players = sorted(overall_skills.items(), key=lambda x: (-x[1], x[0]))

for name, score in sorted_players:
    print(f"{name}: {score} skill")

    sorted_positions = sorted(players_pool[name].items(), key=lambda x: (-x[1], x[0]))
    for positions, scores in sorted_positions:
        print(f"- {positions} <::> {scores}")





