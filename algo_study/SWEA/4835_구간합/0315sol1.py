import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    # print(N, M)
    # print(N_list)
    max_value = -1
    min_value = 987654321

    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += N_list[i+j]
        if total > max_value:
            max_value = total
        if total < min_value:
            min_value = total


    print('#{} {}'.format(tc, max_value - min_value))