T = int(input())
for test_case in range(1, 1 + T):
    num = float(input())
    result = ''
    for i in range(1, 13):
        num *= 2
        result += str(int(num) % 2) # 1의 자리
        if num % 1 == 0: # 소수점
            break
    else:
        result = 'overflow' # 12번 동안 탈출하지 못했을 때
    print('#{} {}'.format(test_case, result))