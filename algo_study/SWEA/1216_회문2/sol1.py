# 풀이법
# brute force가 유용할 수도 있겠다. or 이전에 기억하는 방법인 kmp??? 맞나?
# 1. 앞뒤비교(가장 길이가 긴 곳부터?)
# 2. 글자비교해서 회문이면 len해서 max_value와 비교해서 갱신하는 방법

#
# import sys
#
# sys.stdin = open('input.txt')


# def miro(N):
#     for i in range(len(N) // 2):
#         if N[i] != N[-i - 1]:
#             return False
#     return True


# for tc in range(1, 11):
#     T = int(input())
#     A = [list(input()) for _ in range(100)]
#     B = list(zip(*A))
#     # print(A)
#     max_value = -1
#
#     for row in range(100, 1, -1):
#         if max_value >= row:
#             break
#         for i in range(100-row+1):
#             if max_value == row:
#                 break
#             for x, y in zip(A, B):
#                 if miro(x[i:i+row]) or miro(y[i:i+row]):
#                     max_value = row
#                     break
#
#     print('#{} {}'.format(tc, max_value))

# 이 방법이 안됨
# # 가로 순회
# for row in range(100):
#     for col in range(100):
#         if A[col][row] == A[col][row[-1::-1]]:
#             if max_value < len(A[col][row]):
#                 max_value = len(A[col][row])
# # 세로 순회
# for col in range(100):
#     for row in range(100):
#         if A[col][row] == A[col][-1::-1][row]:
#             if max_value < len(A[col][row]):
#                 max_value = len(A[col][row])


#######################################################

import sys
from datetime import datetime

sys.stdin = open('input.txt')


def solution(s):
    for i in range(len(N) // 2):
        if N[i] != N[-i - 1]:
            return False
        return len(N)

def sol(N):
    max_value = -1
    for row in range(N, 1, -1):
        if max_value >= row:
            return max_value
        for i in range(N - row + 1):
            if max_value == row:
                break
            for x, y in zip(A, B):
                if miro(x[i:i + row]) or miro(y[i:i + row]):
                    max_value = row
            return max_value


T = int(input())
for tc in range(1, T + 1):
    start = datetime.now()
    solution(input())
    end = datetime.now()
    print('#{} {}'.format(10 * 10 ** tc, end - start))

# for tc in range(1, 11):
#     T = int(input())
#     A = [list(input()) for _ in range(100)]
#     B = list(zip(*A))
#     #     # print(A)
#
#     print('#{} {}'.format(tc, miro(A)))
