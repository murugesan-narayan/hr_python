from collections import defaultdict
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    n_dict = defaultdict(list)
    for i in range(1, n+1):
        n_dict[input()].append(str(i))
    for i in range(m):
        word = str(input())
        if word in n_dict:
            print(' '.join(n_dict[word]))
        else:
            print('-1')