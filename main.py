from decoder import decode
from encoder import encode

from datetime import date

birth_date = date(2005, 6, 20)


def loop():
    inp = input("::> ")

    if inp.split(' ')[0] == "today":
        today = date.today()
        difference = today - birth_date

        days_between = difference.days
        print(days_between)
        l = encode(days_between)

        t = ""
        for i in range(len(l) - 1, -1, -1):
            if l[i]:
                t += "1"
            else:
                t += "0"
        print(t)

    elif inp.split(' ')[0] == "e":
        l = encode(inp.split(' ')[1])
        print(l)
        t = ""
        for i in range(len(l) - 1, -1, -1):
            s = l[i]
            if s:
                t += "1"
            else:
                t += "0"
        print(t)
    elif inp.split(' ')[0] == "d":
        print(decode(inp.split(' ')[1]))
    else:
        print("not found")


def main():
    while True:
        loop()


if __name__ == "__main__":
    main()
