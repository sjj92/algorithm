import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    # print(N, K)
    # print(submit)
    result = []

    for i in range(1, N+1):
        if i not in submit:
            result.append(i)

    # print('#{} {}'.format(tc, *result))

    print('#{} {}'.format(tc, ' '.join(map(str, result))))



    # for i in range(1, N+1):
    #     result += str(i)
    #     if submit in range(len(result)):
    #         result -= submit
    #
    # print(result, end='')



