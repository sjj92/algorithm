import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 데이터 입력 받기
    N = float(input())
    # N = input()
    # print(N)


    # 그리디처럼 해도 될 것 같기도 했음, 거스름돈처럼
    for i in range(-1, -13, -1):
        if N % 2 == 0:




    print('#{} {}'.format(tc, result))