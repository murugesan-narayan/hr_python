import re

if __name__ == '__main__':
    # mi = re.finditer(r'\w','http://www.hackerrank.com/')
    # for m in re.finditer(r'\w','http://www.hackerrank.com/'):
    #     print(m.group())
    c = '[qwrtypsdfghjklzxcvbnm]'
    v = '[aeiou]{2,}'
    m_itr = re.findall(rf'(?<={c})({v}){c}', input(), re.I)
    print('\n'.join(m_itr or ['-1']))
