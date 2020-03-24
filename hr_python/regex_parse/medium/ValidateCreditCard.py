import re


if __name__ == '__main__':
    TESTER = re.compile(
        r"^"
        r"(?!.*(\d)(-?\1){3})"
        r"[456]\d{3}"
        r"(\d{12}|(-\d{4}){3})"
        r"$")
    for i in range(int(input())):
        print('Valid' if TESTER.match(input()) else 'Invalid')
