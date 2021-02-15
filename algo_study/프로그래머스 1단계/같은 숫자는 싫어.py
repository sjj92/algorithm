def solution(arr):
    answer = [arr[0]]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)
    return answer

# def solution(numbers):
#     result = [numbers[0]]  # 첫 번재 값으로 비교하기 위해서
#     for num in numbers:
#         if result[-1] != num: # 끝 값을 비교하면 되기 때문에 비교하는 것!
#             result.append(num)
    
#     return result