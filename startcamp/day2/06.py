# 함수
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야한다. 중요!

# 함수 정의
# def funcname(parameter_list):
#     """
#     docstring # 설명서 함수의 역할
#     """
#     pass


def sum(a, b):
    result = a + b
    return result # 없으면 None 출력 return 이후는 함수 종료
    
# 함수 실행(호출)
sum(1, 2)
print(sum(1, 2))

# 함수 실행 결과(return) 값 변수에 할당
result = sum(1, 2)
print(result)

# 미니 실습 주어진 양수 n

print(help(len))
