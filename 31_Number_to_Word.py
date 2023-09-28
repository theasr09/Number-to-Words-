
digit_words = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

teen_words = {
    '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
    '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
    '19': 'nineteen'
}

tens_words = {
    '10': 'ten', '20': 'twenty', '30': 'thirty', '40': 'forty',
    '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'
}

def number_to_words(number):
    if number in digit_words:
        return digit_words[number]

    if number in teen_words:
        return teen_words[number]

    if number in tens_words:
        return tens_words[number]

    if len(number) == 2:
        ten_digit = tens_words[number[0] + '0']
        one_digit = digit_words[number[1]]
        return ten_digit + '-' + one_digit

    if len(number) == 3:
        hundred_digit = digit_words[number[0]]
        remaining_digits = number_to_words(number[1:])
        return hundred_digit + ' hundred and ' + remaining_digits

    if len(number) == 4:
        thousand_digit = digit_words[number[0]]
        remaining_digits = number_to_words(number[1:])
        return thousand_digit + ' thousand ' + remaining_digits

    return "Invalid input"

def main():
    number = input("Enter a number (up to four digits): ")
    try:
        int(number)
        if 0 <= int(number) <= 9999:
            words = number_to_words(number)
            print(f"{number} in words: {words}")
        else:
            print("Please enter a number between 0 and 9999.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
