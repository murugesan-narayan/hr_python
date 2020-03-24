import re

if __name__ == '__main__':
    S, k = input(), input()
    p = re.compile(rf'{k}')
    m = p.search(S)
    if not m:
        print((-1, -1))
    while m:
        print((m.start(), m.end()-1))
        m = p.search(S, m.start()+1)
