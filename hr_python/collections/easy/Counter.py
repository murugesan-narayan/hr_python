from collections import Counter
if __name__ == '__main__':
    input()
    s = input().split()
    c = Counter(s)
    n = int(input())
    total = 0
    for i in range(n):
        si, cost = input().split()
        cost = int(cost)
        if c[si] > 0:
            total += cost
            c[si] = c[si] - 1
    print(total)
