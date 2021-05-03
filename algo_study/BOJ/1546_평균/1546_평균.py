import sys
sys.stdin = open('input.txt')


# for tc in range(6):
#     N = input()
#     scores = list(map(int, input().split()))
#     # print(N)
#     # print(scores)
#
#     # max_value = 0
#     # for i in range(len(N)):
#     #     max_value = max(scores)
#     #     # print(max_value)
#     #     # new_scores = []
#     #     # new_scores.append((scores[i] / max_value) * 100)
#     #     # print(new_scores)
#     #
#     #     avg = 0
#     #     avg = ((scores[i]/max_value) / len(N)) * 100
#     #
#     # print(avg)
#
#     max_value = 0
#     for i in range(len(N)):
#         max_value = max(scores)
#         avg = (sum(scores[i]/max_value) * 100) / len(N)
#
#     print(avg)



N = int(input())
scores = list(map(int, input().split()))
max_value = max(scores)

new_list = []
for i in scores:
    new_list.append(i/max_value *100)
avg = sum(new_list)/N

print(avg)