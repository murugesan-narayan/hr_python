from collections import OrderedDict

if __name__ == '__main__':
    od = OrderedDict()
    for i in range(int(input())):
        w = input()
        od[w] = od.get(w, 0) + 1
    print(len(od))
    print(*od.values())
