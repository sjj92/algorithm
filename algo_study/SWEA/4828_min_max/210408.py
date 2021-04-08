import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(numbers)

    max_value = -1
    min_value = 987654321
    for i in range(N):
        for j in range(N):
            if max_value < numbers[i]:
                max_value = numbers[i]
            if min_value > numbers[i]:
                min_value = numbers[i]

    print('#{} {}'.format(tc, max_value - min_value))