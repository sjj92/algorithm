def solution(s):
    # s = list(input().split())
    check = 0
    left = '('
    right = ')'
    for str in s:
        if check < 0:
            return False
        if str is left:
            check += 1
        else:
            check -= 1
    return check == 0















    # # 괄호 갯수가 다를 경우 false 나옴
    # if left in s:
    #     left_count = s.count(left)
    #     right_count = len(s) - left_count
    #     if left_count // 2 != 0 and right_count // 2 != 0:
    #         return False
    #
    # # 문자 시작이 ) or 마지막이 (면 false
    # if s[0] == right or s[-1] == left:
    #     return False
    #
    # return True
