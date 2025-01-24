#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0

    roman_number = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    number = 0
    prev_value = 0

    # Iterate over the string from right to left
    for char in reversed(roman_string):
        current_value = roman_number.get(char, 0)

        if current_value < prev_value:
            number -= current_value
        else:
            number += current_value

        prev_value = current_value

    return number
