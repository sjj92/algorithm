import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]

    # 밑에서 부터 순회하고 2인지점을 찾기 거기서 올라가기
    goal = 0
    for i in range(100):
        if numbers[99][i] == 2:
            goal = i  # 2가 있는 위치 찾음
            break

    x = goal
    step = 98

    while step > 0:
        right = left = True

        if x - 1 < 0:
            right = True
            left = False
        if x + 1 > 99:
            left = True
            right = False

        if left and numbers[step][x-1]:
            x -= 1
            while not numbers[step-1][x]:
                x -= 1
        elif right and numbers[step][x+1]:
            x += 1
            while not numbers[step-1][x]:
                x += 1

        step -= 1

    print('#{} {}'.format(tc, x))

    # matrix = [[][]]
    #
    # print(DataFrame(matrix))
