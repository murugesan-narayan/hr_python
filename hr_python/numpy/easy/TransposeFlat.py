import numpy

if __name__ == '__main__':
    a = []
    for i in range(int(input().split()[0])):
        ai = input().split()
        a.append(ai)
    a = numpy.array(a, int)
    print(numpy.transpose(a))
    print(a.flatten())
