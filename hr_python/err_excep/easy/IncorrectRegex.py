import re
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        p = input()
        try:
            re.compile(p)
            print(True)
        except:
            print(False)
