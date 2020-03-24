from collections import Counter

if __name__ == '__main__':
    c = Counter(sorted(list(input())))
    for k, v in c.most_common(3):
        print(k, v)

