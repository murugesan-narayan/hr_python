from itertools import combinations
if __name__ == '__main__':
    i, s = input().split()
    i = sorted(i)
    for lc in range(1, int(s)+1):
        print(sep="\n", *[''.join(a) for a in combinations(i, int(lc))])
