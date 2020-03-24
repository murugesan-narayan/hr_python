import numpy

if __name__ == '__main__':
    nl = input().split()
    a = numpy.array(nl, int)
    a.shape = (3, 3)
    print(a)
