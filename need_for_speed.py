def drive(my_cars, some_car, some_distance, some_fuel):
    if some_fuel <= my_cars[some_car]["fuel"]:
        my_cars[some_car]["mileage"] += some_distance
        my_cars[some_car]["fuel"] -= some_fuel
        return (f"{some_car} driven for {some_distance} kilometers. "
                f"{some_fuel} liters of fuel consumed.")
    return "Not enough fuel to make that ride"

def refuel(my_cars, some_car, some_fuel):
    max_fuel = 75
    tank_free_space = max_fuel - my_cars[some_car]["fuel"]

    if tank_free_space >= some_fuel:
        refiled_fuel = some_fuel
        my_cars[some_car]["fuel"] += some_fuel
        return f"{some_car} refueled with {refiled_fuel} liters"

    refiled_fuel = tank_free_space
    my_cars[some_car]["fuel"] += refiled_fuel
    return f"{some_car} refueled with {refiled_fuel} liters"

def revert(my_cars, some_car, some_kilometers):
    my_cars[some_car]["mileage"] -= some_kilometers
    if my_cars[some_car]["mileage"] < 10000:
        my_cars[some_car]["mileage"] = 10000
        return "less than 10000"
    return f"{some_car} mileage decreased by {some_kilometers} kilometers"

number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    car_info = input().split("|")
    car, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])

    cars[car] = {}
    cars[car]= {"mileage": mileage, "fuel": fuel}

while True:
    command = input()

    if command == "Stop":
        break

    parts = command.split(" : ")
    action, car = parts[0], parts[1]

    if action == "Drive":
        distance = int(parts[2])
        fuel = int(parts[3])
        result = drive(cars, car, distance, fuel)
        print(result)
        if cars[car]["mileage"] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")

    elif action == "Refuel":
        fuel = int(parts[2])
        result = refuel(cars, car, fuel)
        print(result)

    elif action == "Revert":
        kilometers = int(parts[2])
        result = revert(cars, car, kilometers)
        if result != "less than 10000":
            print(result)

for car, info in cars.items():
    mileage = info["mileage"]
    fuel = info["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")