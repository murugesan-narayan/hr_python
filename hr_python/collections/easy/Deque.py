from collections import deque
if __name__ == '__main__':
    dq = deque()
    for i in range(int(input())):
        ma = input().split()
        if len(ma) > 1:
            eval(f'dq.{ma[0]}({ma[1]})')
        else:
            eval(f'dq.{ma[0]}()')
    for i in dq:
        print(i, end=" ")
