import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    # print(N_list)

    total = sum(N_list)
    # print(total)
    min_value = 987654321
    a = 0
    b = 0
    cnt = 0
    for i in range(N):
        a += N_list[i]
        b = total - a
        if abs(a-b) < min_value:
            min_value = abs(a-b)
            # cnt 부분을 잘 생각 못함 기억하기
            cnt = i

    print('#{} {} {}'.format(tc, cnt+1, min_value))