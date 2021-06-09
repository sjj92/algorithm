import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    red = []
    blue = []

    # 입력받기
    for i in range(N):
        r1, r2, c1, c2, color = map(int, input().split())

        # test 출력
        # print(r1, r2, c1, c2, color)

        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                if color == 1:
                    red.append((j, k))
                else:
                    blue.append((j, k))
            # print(blue)

        # 겹치는 구간 있으면 넣기위해서 result 빈 list 만들기
        # red or blue list를 비교해가면서 겹치는 구간 result list에 넣기
        result = []
        # for 문이 아니라 if문으로 in 비교!!!! 주의! 헤맴
        # for j in red:

        if len(red) > len(blue):
            for i in blue:
                if i in red:
                    result.append(i)

        if len(blue) > len(red):
            for i in red:
                if i in blue:
                    result.append(i)

    print('#{} {}'.format(tc, len(result)))



# 기억해야 할 유형!
#37분 46초