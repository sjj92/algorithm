# 조건문

# 1. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드

n = 10
if n % 2 == 1:
    print("홀수")
else:
    print("짝수")

# 반복문
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 리스트의 원소중에서 홀수만 찾아 그 값을 ~ 는 홀수입니다. 라고 출력하시오.

# while numbers % 2 == 1:
#     print('{numbers}는 홀수입니다. ') 풀다 못 품 while이 부적합한 문제
    
for number in numbers:
    if number % 2 == 1:
        print(f'{number}는 홀수입니다.')