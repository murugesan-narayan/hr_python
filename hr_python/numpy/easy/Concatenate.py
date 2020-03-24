import numpy

if __name__ == '__main__':
    na, ma = [], []
    n, m, p = input().split()
    [na.append(input().split()) for _ in range(int(n))]
    [ma.append(input().split()) for _ in range(int(m))]
    na = numpy.array(na, int)
    ma = numpy.array(ma, int)
    print(numpy.concatenate((na, ma), axis=0))
