import sys
sys.stdin = open('input.txt')

# 이 풀이 다시 고쳐서 실행시켜보자 output이 안 맞음
# for tc in range(1, 11):
#     Dump = int(input()) # dump 횟수
#     width = 100 # 가로는 항상 100으로 고정
#     heights = list(map(int, input().split())) # input 받음
#     # Dump count를 새로 생성해야 하나?
#
#     while Dump:
#         high_temp = heights[0]
#         low_temp = heights[0]
#         for idx in range(1, 100):
#             if high_temp < heights[idx]:
#                 high_temp = heights[idx]
#                 idx += 1
#             elif low_temp > heights[idx]: # 가장 낮은 층 찾기
#                 low_temp = heights[idx]
#                 idx += 1
#             elif (high_temp - low_temp) <= 1:
#                 break
#
#             high_temp -= 1
#             low_temp += 1
#
#         Dump -= 1
#
#     print('#{} {}'.format(tc, (high_temp - low_temp)))



#     Dump = int(input())
#     heights = list(map(int, input().split()))
#
#     for idx in ragne(heights):
#         heights[] -= 1
#         heights[] += 1
#
#
#     print('#{} {}'.format(tc, (high_temp - low_temp)))
#

for tc in range(1, 11):
    dump = int(input())
    num_list = list(map(int, input().split()))

    while dump > 0:
        num_max = num_list[0]
        num_min = num_list[0]

        for num in num_list:
            if num > num_max:
                num_max = num
            if num < num_min:
                num_min = num

        for j in range(len(num_list)): # 가로 길이 100
            if num_list[j] == num_max:
                num_list[j] -= 1
                for i in range(len(num_list)):
                    if num_list[i] == num_min:
                        num_list[i] += 1
                        break
                break
        dump -= 1
    # num_max = num_list[0]
    # num_min = num_list[0]
    # for num in num_list:
    #     if num >= num_max:
    #         num_max = num
    #     if num <= num_min:
    #         num_min = num
    result = num_max - num_min
    print('#{} {}'.format(tc, result))

    # for tc in range(1, 11):
    #     dump = int(input())
    #     num_list = list(map(int, input().split()))
    #     # 덤프 횟수를 모두 소진해 0이 될 때까지 반복.
    #     while dump > 0:
    #         # 박스 높이의 최댓값과 최솟값을 첫 줄의 박스 높이로 초기설정
    #         num_max = num_list[0]
    #         num_min = num_list[0]
    #         # 모든 박스 높이를 대조해 최댓값과 최솟값 갱신
    #         for num in num_list:
    #             if num > num_max:
    #                 num_max = num
    #             if num < num_min:
    #                 num_min = num
    #         # 가로길이는 항상 100
    #         for j in range(len(num_list)):
    #             # 반복문 중 박스 높이가 최댓값과 같다면 그 줄의 상자를 하나 제거
    #             if num_list[j] == num_max:
    #                 num_list[j] -= 1
    #                 # 그 때, 다시 박스 높이가 최솟값과 같은 줄을 찾아 상자를 하나 추가
    #                 for i in range(len(num_list)):
    #                     if num_list[i] == num_min:
    #                         num_list[i] += 1
    #                         # 2중 for 반복문을 모두 break 하여 같은 높이의 다른 줄에는 영향 X
    #                         break
    #                 break
    #         # 상자가 이동했으므로 덤프 횟수 1 소진
    #         dump -= 1
    #     # 옮겨진 상자 더미의 높이 최솟값과 최댓값을 다시 첫번째 줄 높이로 초기화
    #     num_max = num_list[0]
    #     num_min = num_list[0]
    #     # 모든 줄의 상자 높이를 탐색해 최댓값과 최솟값 갱신
    #     for num in num_list:
    #         if num >= num_max:
    #             num_max = num
    #         if num <= num_min:
    #             num_min = num
    #     # 최댓값과 최솟값의 차를 result 로 정했음
    #     result = num_max - num_min
    #     # 출력
    #     print('#{} {}'.format(tc, result))