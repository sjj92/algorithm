T = int(input())
for tc in range(1, T + 1):
    N, S = input().split()
    ten = int('0x' + S, 16)  # 16진수를 10진수로 바꾸기
    # print(ten)
    b = format(ten, 'b')  # 10진수를 2진수로 바꾸기
    if len(b) < int(N) * 4:  # 첫자리가 0인경우는 안보이니 계산해서 붙여주기
        b = '0' + b

    print('#{} {}'.format(tc, b))