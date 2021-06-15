import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N)
    # print(numbers)
    num_list = [0] * 101

    for i in numbers:
        num_list[i] += 1

    max_value = -1
    for i in range(len(num_list)):
        if num_list[i] >= num_list[max_value]:
            max_value = i

    print('#{} {}'.format(tc, max_value))

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     lst = list(map(int, input().split()))
#
#     max_cnt = 0
#     ans = 0
#
#     for i in range(100, 0, -1):
#         c = lst.count(i)
#
#         if max_cnt < c:
#             max_cnt = c
#             ans = i
#     print('#{} {}'.format(test_case, ans))
