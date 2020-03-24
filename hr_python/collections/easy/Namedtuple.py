from collections import namedtuple
if __name__ == '__main__':
    n, h, tm = int(input()), input().split(), 0
    Student = namedtuple('Student', ' '.join(h))
    for i in range(n):
        st1 = Student(*input().split())
        tm += int(st1.MARKS)
    print(tm/n)
