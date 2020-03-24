import re


if __name__ == '__main__':
    for i in range(int(input())):
        line = input()
        m = re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', line)
        print('Valid' if m else 'Invalid')
