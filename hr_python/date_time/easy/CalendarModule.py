import calendar
if __name__ == '__main__':
    m, d, y = map(int, input().split())
    wd = calendar.weekday(y, m, d)
    print(calendar.day_name[wd].upper())
