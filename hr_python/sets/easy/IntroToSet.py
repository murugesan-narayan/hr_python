def average(array):
    # your code goes here
    s = set(array)
    a = sum(s)/len(s)
    return a


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)