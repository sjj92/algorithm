def solution(n):
    answer = []
    number = str(n)
    for i in range(len(number)):
        answer.append(int(number[len(number)-1-i]))
    
    
    return answer