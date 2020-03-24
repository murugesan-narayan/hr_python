import numpy

if __name__ == '__main__':
    nl = [input().split() for i in range(int(input()))]
    a = numpy.array(nl, float)
    r = numpy.flip(a)
    print(r[1])
