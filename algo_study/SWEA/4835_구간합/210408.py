import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    numbers = list(map(int, input().split()))
    # print(numbers)

    max_value = 0
    min_value = 987654321
    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += numbers[i+j]

        if max_value < total:
            max_value = total
        if min_value > total:
            min_value = total

    print('#{} {}'.format(tc, max_value - min_value))