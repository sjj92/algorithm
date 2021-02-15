def solution(s):
    answer = True
    # for i in s:
    s = s.lower()
    if s.count('p') != s.count('y'):
        return False    
    else:
        return True
        
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')