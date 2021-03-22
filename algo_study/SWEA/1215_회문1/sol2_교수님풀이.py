import sys
from pandas import DataFrame
sys.stdin = open('input.txt')


def rowCount(arr):
    global cnt

    for i in range(N):
        for j in range(N- M +1):
            # 회문 찾기, 길이의 반만 반복
            flag = True
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = False
                    break
            if flag:
                cnt += 1


def colCount(arr):
    global cnt

    for i in range(N):
        for j in range(N- M +1):
            # 회문 찾기, 길이의 반만 반복
            flag = True
            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    flag = False
                    break
            if flag:
                cnt += 1


T = 10
N = 8
for tc in range(1, T + 1):
    # 회문의 크기
    M = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    # arr = [input() for _ in range(N)]

    cnt = 0

    rowCount(arr)
    colCount(arr)

    print('#{} {}'.format(tc, cnt))