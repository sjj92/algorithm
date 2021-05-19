import sys
sys.stdin = open('input.txt')


for i in range(1, 11):
    T = int(input())
    height = list(map(int, input().split())) # 빌딩높이
    total = 0 # 조망권 가능 총 합
    idx = 2
    for idx in range(2, T-2):
        left_2 = height[idx] - height[idx-2]
        left_1 = height[idx] - height[idx-1]
        right_1 = height[idx] - height[idx+1]
        right_2 = height[idx] - height[idx+2]

        if left_2 > 0 and left_1 > 0 and right_1 > 0 and right_2 > 0:
            total += min(left_2, left_1, right_1, right_2)

    print('#{} {}'.format(i, total))











# 풀이 참고

# for tc in range(1, 11):
#     T = int(input())
#     building = list(map(int, input().split()))
#     view = 0
#
#     for i in range(2, T - 2):
#         l_2 = building[i] - building[i - 2]
#         l_1 = building[i] - building[i - 1]
#         r_1 = building[i] - building[i + 1]
#         r_2 = building[i] - building[i + 2]
#         if l_2 > 0 and l_1 > 0 and r_1 > 0 and r_2 > 0:
#             view += min(l_2, l_1, r_1, r_2)
#
#     print("#{} {}".format(tc, view))


        #
        # if height[idx] > height[idx+1] and height[idx-1] < height[idx] and height[]:
        #     total = height[i] - height[i+1] + height[i] - height[i-1]


    # while idx < T-2:
    #     if height[idx] <= height[idx-2] or height[idx] <= height[idx-1] or height[idx] <= height[idx+1]:
    #         idx += 1
    #
    #     elif height[idx] <= height[idx+2]:
    #         idx += 2
    #
    #     else:
    #         total += height[idx] - max(height[idx-2], height[idx-1], height[idx+1], height[idx+2])
    #         idx += 3