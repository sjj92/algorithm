import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)

    # for i in range(1, N+1):
    #     if M == 1:
    #         print('*'* i)
    #
    # for i in range(N, 0, -1):
    #     if M == 2:
    #         print('*'* i)
    #
    # for i in range(N):
    #     # if M == 3:
    #     for j in range(0, N-i-1):
    #         print(' ')
    #     for j in range(0, (2*i+1)):
    #         print('*')


    for i in range(N):
        for j in range(N+1):
            print('*'*i)

    for i in range(N):
        for j in range(N-i):
            print('*'*i)

    for i in range(N):
        for j in range(N-1-i):
            print('*'*i)