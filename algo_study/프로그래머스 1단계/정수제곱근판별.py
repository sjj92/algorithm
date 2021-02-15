def solution(n):
    answer = n**(1/2)
    if answer %1 == 0:
        answer = (answer + 1)**2
        return answer
    else:
        return -1