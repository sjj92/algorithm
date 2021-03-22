import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = [0] * (N+1)
    student = list(map(int, input().split()))

    # 카운팅
    for i in range(K):
        count[student[i]] = 1

    # 0인 인덱스번호 찍기
    print('#{}'.format(tc), end=" ")
    for i in range(1, N+1):
        if count[i] ==0:
            print(i, end = " ")
    print()





