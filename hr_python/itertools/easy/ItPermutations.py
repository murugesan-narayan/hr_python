from itertools import permutations
if __name__ == '__main__':
    i, s = input().split()
    print(sep="\n", *sorted([''.join(a) for a in permutations(i, int(s))]))
