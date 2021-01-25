def solution(n):
    answer = 0
    i = 1 # i = 1 이라는 조건을 줘야 실행된다 zerodivision error 예방 
    for i in range(1, n+1): 
        if n % i == 0:    
            answer = answer + i       
            i = i + 1  # i 증가하는 것 입력!
    return answer