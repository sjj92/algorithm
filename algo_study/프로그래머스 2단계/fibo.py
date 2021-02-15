# 피보나치 구하기
# 그 다음에 


def solution(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
        answer = a % 1234567
    return answer


# 나머지 풀이는 런타임 에러가 너무 많이 나서 이 풀이 암기하자
    