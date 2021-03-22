import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)

    max_value = 0
    min_value = 987654321

    for i in range(N-M+1):
        # 합 구하기
        sum_value = 0
        for j in range(M):
            sum_value += arr[i+j]
        # 최댓값, 최솟값 구하기
        if sum_value > max_value:
            max_value = sum_value
        if sum_value < min_value:
            min_value = sum_value

    print('#{} {}'.format(tc, max_value - min_value))