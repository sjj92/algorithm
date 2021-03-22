import sys
from pandas import DataFrame

sys.stdin = open('input.txt')

#
# # 단조 확인
# def check(num):
#     temp = num % 10 # 3
#     num = num // 10 # 12
#     while num:
#         if num % 10 > temp: # 2 > 3
#             return False
#         temp = num % 10 # 2
#         num = num // 10 # 1
#     return True

def check2(num):
    a = str(num)
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(N)
    # print(arr)
    ans = -1
    #조합
    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            if check2(num):
                if ans < num:
                    ans = num


    print('#{} {}'.format(tc, ans))