import re

if __name__ == '__main__':
    rr = r'(^(?=[789])(\d{10})$)'
    for i in range(int(input())):
        m = re.match(rr, input())
        print('YES' if m else 'NO')
