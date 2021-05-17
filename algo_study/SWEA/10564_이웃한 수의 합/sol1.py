import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    # print(N_list)
    total = []
    # max_value = -1
    # min_value = 987654321
    for i in range(N-1):
        total.append(sum(N_list[i:i+2]))

        # if max_value < total:
        #     max_value = total
        # if min_value > total:
        #     min_value = total

    print('#{} {} {}'.format(tc, max(total), min(total)))

