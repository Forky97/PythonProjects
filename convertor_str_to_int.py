def parse_int(string):
    numbers = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90
    }

    words = string.replace('-', ' ').split()

    curent_number = 0
    result = 0

    for word in words:
        if word in numbers:
            curent_number += numbers[word]
        elif word == 'hundred':
            curent_number *= 100
        elif word == 'thousand':
            result = curent_number * 1000
            curent_number = 0
        elif word == 'million':
            result = curent_number * 1000000
            curent_number = 0
    result += curent_number
    return result

print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))