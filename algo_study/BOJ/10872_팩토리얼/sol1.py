import sys

sys.stdin = open('input.txt')


# def facto(N):
#     while N < 1:
#         if N <= 1:
#             return 1
#         else:
#             return N * facto(N - 1)


def factorial(N):
    answer = 1

    if N > 0:
        answer = N * factorial(N - 1)
    return answer


N = int(input())
# print(N)

print(factorial(N))
