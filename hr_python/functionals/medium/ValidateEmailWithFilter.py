import re

if __name__ == '__main__':
    el = []
    for _ in range(int(input())):
        el.append(input())
    print(sorted(filter(lambda email: re.match(r'^(\w|-)+@[a-z0-9]+\.[a-z]{1,3}$', email, re.I) is not None, el)))
