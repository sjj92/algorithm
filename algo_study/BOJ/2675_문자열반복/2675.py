import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    P = ''
    for j in S:
        # print(j)
        P += R * j
    print(P)

