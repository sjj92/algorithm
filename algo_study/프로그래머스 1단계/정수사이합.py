def solution(a, b):
    answer = 0
    if a != b and abs(a-b) == 2:      
        answer = a + b + ((a+b) / 2)
        print(answer)
    elif a == b:
        print(a)
