import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(input())
    # print(N_list)

    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if N_list[i] == '1' and N_list[i+1] == '1':
            cnt += 1
        else:
            cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc, max_cnt+1))