import sys
sys.stdin = open('input.txt')


def solution(S):
    # write your code in Python 3.6
    # total = 0
    for tc in range(len(S)):
        # first condition check - backup files
        if S[2][-1] == '~':
            # third condition check - date and year files
            if S[1] > '1990-01-31':
                # To find minimum length initial value
                total = 0
                # second condition check - size check
                if S[0][-1] == 'K' or S[0][-1] == 'G' and S[0][:-1] <= 14:
                    # To find minimum length - all condition satisfy
                    new = S[2].split('.')
                    if len(new[0]) < total:
                        total = len(new[0])
                    return total

        # condition is not satisfy
        else:
            return 'NO FILES'


S = list(input().split())

print(solution(S))








# new = S[2].split('.')
# print(len(new[0]))
# print(N)
# print(N[0][-1])
# print(N[2][-1])
# print(N[1])
# print(N[0][:-1])

# 날짜 테스트 완료
# if N[1] > '1990-01-31':
#     # print(N[1])
#     print(1)
# else:
#     print(0)
#
#
#  날짜 테스트 완료
# if N[0][-1] == 'K' or N[0][-1] == 'G' and N[0][:-1] <= 14:
#     # print(N[1])
#     print(1)
# else:
#     print(0)

# # second condition check - size check
# if N[0][-1] == 'K':
#
# elif N[0][-1] == 'G' and N[0][:-1] <= 14: