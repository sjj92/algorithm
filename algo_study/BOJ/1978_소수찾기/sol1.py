import sys

sys.stdin = open('input.txt')

T = int(input())
# for tc in range(T):
N = map(int, input().split())
# 소수 갯수 카운트
total = 0
for i in N:
    cnt = 0
    # if i == 1:
    #     continue
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        total += 1

print(total)
