days = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())

total_plunder = 0
daily_plunder = plunder_per_day

for day in range(1, days + 1):

    total_plunder += daily_plunder

    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5

    if day % 5 == 0:
        total_plunder *= 0.70





if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_gather = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage_gather:.2f}% of the plunder.")