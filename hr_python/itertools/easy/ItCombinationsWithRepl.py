from itertools import combinations_with_replacement
if __name__ == '__main__':
    i, s = input().split()
    i = sorted(i)
    print(sep="\n", *[''.join(a) for a in combinations_with_replacement(i, int(s))])
