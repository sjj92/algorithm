import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

def calc(x, y):

    sum_value = 0
    for i in range(M):
        for j in range(M):
            sum_value += arr[x + i][y + j]

    return sum_value


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(DataFrame(arr))
    max_value = 0

    # 2차원 행렬의 시작점 순회
    for x in range(N - M +1):
        for y in range(N - M +1):
            # 작은 정사각형(파리채)의 합 구하기
            sum_value = calc(x, y)
            # 최댓값 구하기
            if max_value < sum_value:
                max_value = sum_value

    print('#{} {}'.format(tc, max_value))