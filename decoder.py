# convert binary to number


def decode(digits: str):
    result = 0

    s = 1

    for i in range(len(digits) - 1, -1, -1):

        if digits[i] == "1":
            result += s

        s *= 2

    return result
