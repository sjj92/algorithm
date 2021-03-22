import sys
from pandas import DataFrame
sys.stdin = open('input.txt')


for tc in range(1, 11):
    length = int(input())
    rec_list = [list(map(str, input().split())) for _ in range(8)]
    # print(length)
    # print(DataFrame(rec_list))
    tip = length //2
    count = 0

    # 가로순회
    for row in range(8):
        for col in range(tip):
            # 홀수 부터

            if length % 2 == 1:
                if rec_list[col][row] == rec_list[-col-1][row]:
                    count += 1
            else:
                if rec_list[col][row] == rec_list[-col - 1][row]:
                    count += 1

    print('#{} {}'.format(tc, count))