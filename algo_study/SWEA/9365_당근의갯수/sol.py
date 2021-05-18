import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    # print(max(C))

    result = 0
    for i in range(N):
        if C[i] == max(C):
            result = i+1

    print('#{} {} {}'.format(tc, result, max(C)))