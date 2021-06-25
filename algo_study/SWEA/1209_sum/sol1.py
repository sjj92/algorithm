import sys
sys.stdin = open('input.txt')

for tc in range(10):
    rec_list = [] # 배열의 크기 / 열 나눠서는 빈리스트 다시 바꿔야 하나? 수업내용 참고하기
    N = int(input())
    for i in range(100):
        rec_list.append(list(map(int, input().split())))

    total = 0 # 최댓값을 비교해서 변수를 줄이자.

    # 가로로 순회
    for row in range(len(rec_list)):
        row_sum = 0
        for col in range(len(rec_list)):
            row_sum += rec_list[col][row]
            if total < row_sum:
                total = row_sum

    # 세로로 순회
    for col in range(len(rec_list)):
        col_sum = 0
        for row in range(len(rec_list)):
            col_sum += rec_list[col][row]
            if total < col_sum:
                total = col_sum

    # 가로 세로 순회하면 대각선 값들도 다 구해지니까 안해도 되지 않을까?
    # 대각선 합 구하기
    for row in range(len(rec_list)):
        rec_sum = 0
        for col in range(len(rec_list)):
            if row == col:
                rec_sum += rec_list[col][row]
                if total < rec_sum:
                    total = rec_sum

    # 대각선 반대 방향 합 구하기
    for row in range(len(rec_list)):
        div_sum = 0
        for col in range(len(rec_list)):
            if row == len(rec_list)-col:
                div_sum += rec_list[col][row]
                if total < rec_sum:
                    total = rec_sum

    print('#{} {}'.format(tc+1, total))









