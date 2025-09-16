number_of_msg = int(input())

for _ in range(number_of_msg):
    message = int(input())

    if message == 88:
        print("Hello")

    elif message == 86:
        print("How are you?")

    elif message < 88:
        print("GREAT!")

    else:
        print("Bye.")