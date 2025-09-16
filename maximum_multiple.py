devisor = int(input())
boundary = int(input())

for i in range(boundary, 0, -1):

    if i % devisor == 0:
        print(i)
        break
