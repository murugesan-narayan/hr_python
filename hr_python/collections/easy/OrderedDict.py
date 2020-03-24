from collections import OrderedDict
if __name__ == '__main__':
    od = OrderedDict()
    for i in range(int(input())):
        name, space, price = input().rpartition(" ")
        od[name] = od.get(name, 0) + int(price)
    for k, v in od.items():
        print(k, v)
