import sys
from pandas import DataFrame
sys.stdin = open('input.txt')


def check(M):

    max_value = 0

    for i in range(M):
        total = 0
        for j in range(M):
            total += miro[i + j]
        if max_value < total:
            max_value = total

    return max_value




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    miro = [list(map(int, input().split())) for _ in range(N)]

    # print(N, M)
    # print(DataFrame(miro))

    for i in range(N):
        for j in range(N - M + 1):
            ans = check(M)



    print('#{} {}'.format(tc, ans))