# s길이 : 4 or 6 , 숫자로만 구성됨
# 


def solution(s):   
#     if len(s) == 4 or len(s) == 6:
#         for i in s:
#             if i in range(len(s)):
#                 answer = True
#             else:
#                 answer = False    
    
#     return answer

    if (len(s) == 4 or len(s) == 6) and s.isdigit(): # len or때 ()를 한번 더 확실하게 씌어주자
        return True
    else:
        return False