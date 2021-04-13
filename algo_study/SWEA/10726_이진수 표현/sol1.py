# 풀이법
# 1. M을 이진수로 변환하기!
# 2. 슬라이싱으로 마지막 N개 '1'인지 for문으로 확인

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # data 입력
    N, M = map(int, input().split())
    # print(N, M)

    # 내장함수를 이용해서 10진수 -> 2진수 변환
    b = bin(M)
    # print(b)

    result = ''
    cnt = 0
    for i in b[-N:]:
        if i == '1':
            cnt += 1

    if cnt == N:
        result = 'ON'
    else:
        result = 'OFF'

    print('#{} {}'.format(tc, result))