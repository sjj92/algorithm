import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N)
    # data 양이 많다.
    # print(numbers)

    total = 0
    max_number = numbers[-1]

    # 거꾸로 순회하기
    for i in range(len(numbers)-1, -1, -1):
        if max_number > numbers[i]:
            total += max_number - numbers[i]
        else:
            max_number = numbers[i]

    print('#{} {}'.format(tc, total))