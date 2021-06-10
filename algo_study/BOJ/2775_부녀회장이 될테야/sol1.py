### 단순 수학적인 문제가 아니라 각 호실을 계산 및 갱신 2중 for문 및 리스트

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    N = int(input())
    # 변수를 0층~ 1호부터 담음
    human = [i for i in range(1, N+1)]
    # 0층 부터 시작
    for x in range(K):
        # 1호부터 시작
        for y in range(1, N):
            human[y] += human[y-1]

    print(human[-1])


