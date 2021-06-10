import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split())
# print(A, B, C)

cnt = 0
if B >= C:
    cnt = -1
else:
    cnt = (A // (C-B)) + 1

print(cnt)



A, B = map(int, input().split())

print(A + B)