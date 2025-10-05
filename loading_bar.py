def loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    percents_count = some_number // 10
    points_count = 10 - percents_count
    return (f"{some_number}% [{'%' * percents_count}{'.' * points_count}]\n"
            f"Still loading...")




number = int(input())
print(loading_bar(number))