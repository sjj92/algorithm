import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = input()
    # print(N)
    cnt = 0
    find_number = '0'

    for i in range(len(N)):
        if N[i] != find_number:
            cnt += 1
            find_number = N[i]


    # find_number = '1'

    # for i in range(len(N)):
    #     if N[i] == find_number:
    #         cnt += 1

    print('#{} {}'.format(tc, cnt))
