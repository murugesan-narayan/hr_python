from datetime import datetime
if __name__ == '__main__':
    fmt = '%a %d %b %Y %H:%M:%S %z'
    for t in range(int(input())):
        d1 = datetime.strptime(input(), fmt)
        d2 = datetime.strptime(input(), fmt)
        print(int(abs((d2 - d1).total_seconds())))
