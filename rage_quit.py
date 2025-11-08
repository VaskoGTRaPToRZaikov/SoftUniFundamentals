text = input()

count_symbols = ""
symbols_for_convert = ""
final_text = ""
index = 0

while index < len(text):
    if text[index].isdigit():

        repeat_count = int(text[index:index +2]) if (index + 1 < len(text)
                and text[index + 1].isdigit()) else int(text[index])
        index += 2 if repeat_count >= 10 else 1

        final_text += symbols_for_convert * repeat_count
        symbols_for_convert = ""

    else:
        symbols_for_convert += text[index].upper()
        count_symbols += text[index].upper()
        index += 1

number_of_symbols = len(set(count_symbols))

print(f"Unique symbols used: {number_of_symbols}")
print(final_text)

