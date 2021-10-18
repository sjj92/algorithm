import sys
sys.stdin = open('input.txt')


T = list(map(int, input().split()))
# print(T)

answer = 0
for i in range(len(T)):
    answer += T[i] ** 2
print(answer%10)
