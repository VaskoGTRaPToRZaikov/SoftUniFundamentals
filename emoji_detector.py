import re
import math

text = input()

pattern_emoji = r"(::|\*\*)([A-Z][a-z]{2,})\1"
digits_pattern = r"\d"
cool_threshold = 0

threshold_matches = re.findall(digits_pattern, text)
if threshold_matches:
    cool_threshold = math.prod(map(int, threshold_matches))
    print(f"Cool threshold: {cool_threshold}")

emoji_matches = re.findall(pattern_emoji, text)
if emoji_matches:
    print(f"{len(emoji_matches)} emojis found in the text. The cool ones are:")
    for match in emoji_matches:
        emoji = match[1]
        emoji_for_print = match[0]+match[1]+match[0]
        emoji_threshold = sum(ord(char) for char in emoji)

        if emoji_threshold >= cool_threshold:
            print(emoji_for_print)
