def morse_code_translator(text):
    decrypted_text = []

    morse_code_dictionary = {
        '..-.': 'F', '-..-': 'X', '.--.': 'P', '-': 'T',
        '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
        '---': 'O', '-.-': 'K', '..': 'I', '.-..': 'L',
        '-.--': 'Y', '.--': 'W', '....': 'H', '-.': 'N',
        '.-.': 'R', '-...': 'B', '--..': 'Z', '-..': 'D',
        '--.-': 'Q', '--.': 'G', '--': 'M', '..-': 'U',
        '.-': 'A', '...': 'S'
    }

    for word in text:
        for letter in word.split(" "):
            if letter in morse_code_dictionary.keys():
                decrypted_text.append(morse_code_dictionary[letter])
        decrypted_text.append(" ")
    return ''.join(decrypted_text)

words = input().split(" | ")

print(morse_code_translator(words))




