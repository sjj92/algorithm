def solution(n):
    answer = ''
    
    for i in range(n):  # i = 0 부터 시작하니까 
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    
    return answer