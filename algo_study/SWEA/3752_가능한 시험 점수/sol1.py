# 풀이법
# 1. 경우의 수를 어떻게 표현할지가 문제!
# 2. 간단할 수도 있고, 중복되는 경우는 제외하고 출력!
# 3. 0점은 cnt에서 +1을 하면서 해결!
# 4. 경우의 수 순열이나 팩토리얼로 해결 안되고 일일히 더해서 갯수 구현하는게 제일 빠를 듯 - 시간 초과 주의!


# 1. 데이터 입력 받기 - 0
# 2. 입력받은 데이터를 서로 더해서 total list에 넣는 방식으로 진행
# 3.  이후 total list에서 len으로 갯수 구하기 +1(0점일 경우)

# 이거 문제 이해는 쉬운데 정말 어려움을 겪음... 참고해서 겨우 타이핑함.

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # data 입력
    N = int(input())
    score = list(map(int, input().split()))

    total = [1] + [0]* (sum(score))
    save = [0]

    for i in score:
        for j in range(len(save)):
            if not total[i+save[j]]:
                total[i+save[j]] = 1
                save.append(i + save[j])

    print('#{} {}'.format(tc, len(save)))