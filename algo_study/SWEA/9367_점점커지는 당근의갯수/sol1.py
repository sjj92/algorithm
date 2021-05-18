import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    # print(N_list)

    max_value = 0
    cnt = 0
    for i in range(N-1):
        if N_list[i] + 1 == N_list[i+1]:
            cnt += 1
        else:
            cnt = 0
        if max_value < cnt:
            max_value = cnt

    print('#{} {}'.format(tc, max_value+1))