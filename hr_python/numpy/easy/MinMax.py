import numpy

if __name__ == '__main__':
    a = []
    for i in range(int(input().split()[0])):
        a.append(input().split())
    a = numpy.array(a, numpy.int)
    m = numpy.min(a, axis=1)
    print(numpy.max(m))

