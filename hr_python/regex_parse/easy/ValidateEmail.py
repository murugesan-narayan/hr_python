import re
from email.utils import parseaddr, formataddr

if __name__ == '__main__':
    for i in range(int(input())):
        name, email = parseaddr(input())
        m = re.match(r'^[a-z](\w|-|\.|_)+@[a-z]+\.[a-z]{1,3}$', email, re.I)
        if m:
            print(formataddr((name, email)))
