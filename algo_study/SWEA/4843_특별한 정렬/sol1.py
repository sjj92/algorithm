import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    numbers = list(map(int, input().split()))
    new_num = len(numbers)

    # print(numbers)
    # sort 함수 이용해서 정렬
    numbers.sort()
    # print(numbers)

    result = []
    big = []
    small = []
    for i in range(new_num):
        if i < new_num//2:
            small.append(numbers[i])
        elif i > (new_num//2) -1:
            big.append(numbers[i])
    big.sort(reverse=True)

    for j in range(5):
        result.append(big[j])
        result.append(small[j])

    # print('#{} {}'.format(tc, result))
    # list에서 바꾸는 것 기억!
    print('#{} {}'.format(tc, " ".join(map(str, result))))

# 33분
