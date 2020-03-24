import re


if __name__ == '__main__':
    for i in range(int(input())):
        line = input()
        if line.startswith("#"):
            continue
        lst = re.findall(r'([#a-f0-9]{7}|[#a-f0-9]{4})', line, re.I)
        for m in lst:
            print(m)
