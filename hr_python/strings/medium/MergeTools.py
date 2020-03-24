from collections import OrderedDict


def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        p = s[i:i+k]
        print("".join(OrderedDict.fromkeys(p)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)