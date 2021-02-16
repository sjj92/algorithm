def solution(s):
#     answer = ''
#     s = list(map(int, s.split()))
#     max_value = 0
#     min_value = 0

#     for i in range(s):
#         for j in range(s):
#             if s[j] < s[j + 1]:
#                 s[j], s[j + 1] = s[j + 1], s[j]
#                 answer.append(s)
#                 max_value = answer[-1]
#                 min_value = answer[0]

#     return max_value, min_value
    s = list(map(int, s.split()))

    return '{} {}'.format(min(s), max(s))
    # 함수의 효과가 엄청남