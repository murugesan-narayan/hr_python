import re


if __name__ == '__main__':
    for i in range(int(input())):
        f = input()
        print(re.match(r"^[+-]?\d*\.\d+$", f) is not None)
