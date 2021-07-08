import sys

sys.stdin = open('input.txt')

# test case는 10개라고 문제에서 나옴
for tc in range(1, 11):
    T = int(input())
    # print((T))
    N, M = map(int, input().split())
    # print(N, M) - 입력 완료
    answer = N ** M


    print('#{} {}'.format(tc, answer))