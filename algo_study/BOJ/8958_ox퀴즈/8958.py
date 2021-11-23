import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    qustion = input()
    total = 0
    score = 0
    for j in qustion:
        if j == 'O':
            score += 1
            # total 부분 기억하기
            total += score
        else:
            score = 0
    print(total)
