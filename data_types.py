def data_types(some_type, some_input):
    if some_type == "int":
        return int(some_input) * 2
    elif some_type == "real":
        return f"{float(some_input) * 1.5:.2f}"
    return f"${some_input}$"

string = input()
number_or_text = input()

result = data_types(string, number_or_text)
print(result)