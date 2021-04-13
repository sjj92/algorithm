import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    codes = []
    for _ in range(N):
        codes += list(input())
    pwd = [0, 0, 0, 0, 0, 0, 0, 0]  # 8자리의 암호코드
    pattern = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    idx = N * M - 1
    while True:
        if codes[idx] == '1':
            for i in range(8):
                pwd[7 - i] = pattern[''.join(codes[idx - 6:idx + 1])]
                idx -= 7
            break

        else:
            idx -= 1

    answer = 0
    if not ((pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3 + (pwd[1] + pwd[3] + pwd[5]) + pwd[
        7]) % 10:
        answer = sum(pwd)

    print('#{} {}'.format(tc, answer))