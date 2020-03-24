import math
if __name__ == '__main__':
    ab, bc = map(int, [input(), input()])
    print(str(round(math.degrees(math.atan2(ab, bc))))+'°')