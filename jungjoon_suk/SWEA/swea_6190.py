import sys
from pandas import DataFrame

sys.stdin = open('input.txt')


# 단조 확인
def check(number):
    temp = str(number)
    for i in range(len(temp)-1):
        if temp[i] > temp[i+1]:
            return False
    return True

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(N)
    # print(arr)
    max_value = 0

    for i in range(N-1):
        for j in range(i+1, N):
            result = arr[i] * arr[j]
            if check(result):
                max_value = max(result, max_value)

            if max_value == 0:
                max_value = -1

    print('#{} {}'.format(tc, max_value))




