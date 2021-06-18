import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # print(N)
    # print(T)
    # 2차원 리스트 만들어서 빈리스트 생성?
    matrix = [[0]*N for _ in range(N)]
    # matrix = [[N] for _ in range(N)]
    # print(DataFrame(matrix))

    # matrix[0][0] = (1,0)
    # 처음 자리 1 고정
    for i in range(N):
        matrix[i][0] = 1

    # 범위 조정(1부터 시작) - 위에서 1 생성 시키니까
    for row in range(1, N):
        for col in range(1, N):
            matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]
            # col += 1

    print('#{}'.format(tc))
    # print('{}'.format(matrix))

    for j in range(tc):
        print(*matrix[j][:j+1])





    #
    # for row in range(1, N):
    #     for col in range(1, N):
    #         # 맨처음이랑 맨 마지막은 1 만들어줌
    #         # if 0 <= row < N and 0 <= col < N:
    #         #     if col == 0 or col == row:
    #                 # matrix[row][col] == 1
    #                 matrix[row][col] = matrix[row-1][col-1]