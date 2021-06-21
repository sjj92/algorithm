import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T =int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    # print(N, K)
    # print(K)
    display = [[0]*N for _ in range(4)]
    # print(DataFrame(display))

    cnt = 0
    for i in range(4):
        for j in range(N):
            # k 배수가 되면 switch가 됨
            for k in range(1, K+1):
                if (i+j+1) % k == 0:
                    if display[i][j] == 1:
                        display[i][j] = 0
                        cnt -= 1
                    elif display[i][j] == 0:
                        display[i][j] = 1
                        # 0에서 1로 바뀐 것들만 count 한 것
                        # if display[i][j] == 1:
                        cnt += 1

    result = cnt

    print('#{} {}'.format(tc, result))

















    # cnt = 0
    # for i in range(4):
    #     for j in range(N):
    #         # k 배수가 되면 switch가 됨
    #
    #         if (i+j+1) % K == 0:
    #             if display[i][j] == 1:
    #                 display[i][j] = 0
    #             elif display[i][j] == 0:
    #                 display[i][j] = 1
    #                 # 0에서 1로 바뀐 것들만 count 한 것
    #                 # if display[i][j] == 1:
    #                 cnt += 1
    #
    #         # 배수가 아닌경우
    #         else:
    #             if display[i][j] == 1:
    #                 cnt += 1
    # result = cnt
    #
    # print('#{} {}'.format(tc, result))











# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     # print(N, K)
#     display = [[0] * N for _ in range(4)]
#     # print(DataFrame(display))
#
#     cnt = 0
#     for i in range(4):
#         for j in range(N):
#             if (i + j + 1) % K == 0:
#                 # k 배수가 되면 switch가 됨
#                 if display[i][j] == 1:
#                     display[i][j] = 0
#                     # if display[i][j] == 1:
#                     #     cnt += 1
#                 elif display[i][j] == 0:
#                     display[i][j] = 1
#                     # 0에서 1로 바뀐 것들만 count 한 것
#                     # if display[i][j] == 1:
#                     cnt += 1
#             # 배수가 아닌경우
#             else:
#                 if display[i][j] == 1:
#                     cnt += 1

# 다시 돌아보는 방법
# for a in range(4):
#     for b in range(N):
#         if display[i][j] == 1:
#             cnt += 1
#
#     print('#{} {}'.format(tc, cnt))











    # # cnt = 0
    # for i in range(4):
    #     for j in range(N):
    #         # if (i + j + 1) % K == 0:
    #             # k 배수가 되면 switch가 됨
    #         if display[i][j] == 1:
    #             if (i + j + 1) % K == 0:
    #                 display[i][j] = 0
    #         elif display[i][j] == 0:
    #             if (i + j + 1) % K == 0:
    #                 display[i][j] = 1
    #         cnt = 0
    #         if display[i][j] == 1:
    #             cnt += 1
    
    
    
    
    
    
    ##################
    # 1차 제출

# T =int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     # print(N, K)
#     display = [[0]*N for _ in range(4)]
#     # print(DataFrame(display))
# 
#     cnt = 0
#     for i in range(4):
#         for j in range(N):
#             # if (i + j + 1) % K == 0:
#                 # k 배수가 되면 switch가 됨
#             if display[i][j] == 1:
#                 if (i + j + 1) % K == 0:
#                     display[i][j] = 0
#             elif display[i][j] == 0:
#                 if (i + j + 1) % K == 0:
#                     display[i][j] = 1
# 
#             if display[i][j] == 1:
#                 cnt += 1
#             # cnt = display[i][j].count(1)
# 
# 
#     print('#{} {}'.format(tc, cnt))


#
# cnt = 0
    # for i in range(4):
    #     for j in range(N):
    #         if 1 in display[i][j]:
    #             cnt += 1
    #
    # print('#{} {}'.format(tc, cnt))


    #
    #
    # cnt = 0
    # for i in range(4):
    #     for j in range(N):
    #         # k 배수가 되면 switch가 됨
    #         for k in range(1, K+1):
    #             if (i+j+1) % k == 0:
    #                 if display[i][j] == 1:
    #                     display[i][j] = 0
    #                     cnt -= 1
    #                 elif display[i][j] == 0:
    #                     display[i][j] = 1
    #                     # 0에서 1로 바뀐 것들만 count 한 것
    #                     # if display[i][j] == 1:
    #                     cnt += 1
    #
    #             # 배수가 아닌경우 - 신경 안써도 될 듯 초기 1으로 하면
    #             else:
    #                 if display[i][j] == 1:
    #                     cnt += 1
    # result = cnt