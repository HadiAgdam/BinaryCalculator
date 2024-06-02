# convert numer to binary

def get_digits(number: int):
    i = 1
    s = 0

    digits = []

    while s < number:
        s += i
        digits.append(i)
        i = i * 2

    return digits


def encode(number):
    number = int(number)

    digits = get_digits(number)

    s = 0
    for i in range(len(digits) - 1, -1, -1):
        if s + digits[i] <= number:
            s += digits[i]
            digits[i] = True
        else:
            digits[i] = False

    return digits
