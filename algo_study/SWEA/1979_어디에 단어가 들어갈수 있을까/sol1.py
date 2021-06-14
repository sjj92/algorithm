# 풀이법
# 가로순회, 세로순회하기 / 대각선은 안해도 됨
# 


import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # [0] 추가 잊지말기!
    square = [list(map(int, input().split()))+[0] for _ in range(N)]
    square.append([0]*(N+1))
    # print(N, K)
    # print(DataFrame(square))

    result = 0
    # # 가로 순회
    for i in range(N):
        cnt = 0
        for j in range(N+1):
            if square[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

    # 세로 순회
        for j in range(N+1):
            if square[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

    print('#{} {}'.format(tc, result))



    # for j in range(N - K + 1):
    #     for i in range(K):
    #         # if square[j][i] == 1 and square[j+1][i] == 1:
    #         if square[j][i] == 1 and square[j + 1][i] == 1:
    #             cnt += 1
    #
    # print('#{} {}'.format(tc, cnt))
