import numpy

if __name__ == '__main__':
    r, c = map(int, input().split())
    a1, a2 = [], []
    for i in range(r):
        a1.append(input().split())
    for i in range(r):
        a2.append(input().split())
    print(a1, a2)
    a1 = numpy.array(a1, dtype=numpy.int)
    a2 = numpy.array(a2, dtype=numpy.int)
    print(a1+a2, a1-a2, a1*a2, a1//a2, a1%a2, a1**a2, sep='\n')
