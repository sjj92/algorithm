import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    square = [list(map(int, input().split())) for _ in range(N)]

    # test 출력 - ok
    # print(DataFrame(square))

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    total = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    if square[i][j] > square[nr][nc]:
                        cnt += 1
            # 아래부분 들여쓰기 주의!
            if cnt >=4:
                total += 1

    print('#{} {}'.format(tc, total))
    
    
    # 20분