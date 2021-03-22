import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    # print(N, M)
    print('#{}'.format(tc))

    if M == 1:
        for i in range(N):
            for j in range(i+1):
                print('*', end="")
            print()

    elif M == 2:
        for i in range(N):
            for j in range(N - i):
                print('*', end="")
            print()

    elif M == 3:
        for i in range(N):
            # 공백
            for j in range(N - i - 1):
                print(' ', end="")
            for j in range((i+1)*2-1):
                print('*', end="")
            print()







    # for i in range(1, N+1):
    #     if M == 1:
    #         print('*'* i)
    #
    # for i in range(N, 0, -1):
    #     if M == 2:
    #         print('*'* i)
    #
    # for i in range(N):kse
    #     # if M == 3:
    #     for j in range(0, N-i-1):
    #         print(' ')
    #     for j in range(0, (2*i+1)):
    #         print('*')
    #
    #
    #
    #
    # # print('#{} {}'.format(tc, max_value))
