import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    max_total = -987654321
    # 아래 코드는 0~3까지 이므로 다 더하게 됨

    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    total += square[nr][nc]

            if total > max_total:
                max_total = total

    # print('#{} {}'.format(tc, max_total))
    print(f'#{tc} {max_total}')

### 30분