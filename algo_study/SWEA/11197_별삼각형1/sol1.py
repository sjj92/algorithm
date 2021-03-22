import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)

    for i in range(1, N+1):
        if M == 1:
            print('*'* i)

    for i in range(N, 0, -1):
        if M == 2:
            print('*'* i)

    for i in range(N):kse
        # if M == 3:
        for j in range(0, N-i-1):
            print(' ')
        for j in range(0, (2*i+1)):
            print('*')




    # print('#{} {}'.format(tc, max_value))




    # # 2차원 행렬의 시작점 순회
    # for x in range(N - M +1):
    #     for y in range(N - M +1):
    #         # 작은 정사각형(파리채)의 합 구하기
    #         sum_value = calc(x, y)
    #         # 최댓값 구하기
    #         if max_value < sum_value:
    #             max_value = sum_value