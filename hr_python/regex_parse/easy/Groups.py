import re


if __name__ == '__main__':
    """m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'username@hackerrank.com')
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.group(1,2))
    print(m.groups())
    print(m.groupdict())"""
    m = re.search(r'([a-zA-Z0-9])\1+', input())
    print(-1 if m is None else m.group(1))
