import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 정사각형의 길이
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 배열이 붙어있으면 split()안해도 된다.
    # print(N)
    # print(arr)

    start = end = mid = N //2
    total = 0
    for i in range(N):
        for j in range(start, end+1):
            total += arr[i][j]
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print('#{} {}'.format(tc, total))