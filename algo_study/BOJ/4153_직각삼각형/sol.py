import sys

sys.stdin = open('input.txt')

while True:
    # a, b, c = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break
    b = max(a)
    a.remove(b)
    # print(a, b, c)
    if a[0] ** 2 + a[1] ** 2 == b ** 2:
        print('right')
    else:
        print('wrong')
