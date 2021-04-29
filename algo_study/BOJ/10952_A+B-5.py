import sys
sys.stdin = open('input.txt')

# for i in range(5):
#     A, B = map(int, input().split())
#     # print(A, B)
#
#     if A != 0 and B != 0:
#         result = A + B
#     print(result)


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)