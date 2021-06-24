import sys

sys.stdin = open('input.txt')


# 풀이 1
# 가장 높은 상자를 찾고 가장 낮은 상자를 찾아서 덤프하는 것

# 최저 높이의 상자 인덱스 위치 반환
def min_search():
    # 초기화
    min_value = 101
    min_idx = -1

    # 최저 높이를 찾자.
    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i

        return min_idx


def max_search():
    # 초기화
    max_value = 0
    max_idx = -1

    # 최저 높이를 찾자.
    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i

        return max_idx


for tc in range(1, 11):
    # dump 횟수
    dump = int(input())
    # 박스들
    box = list(map(int, input().split()))

    # N번의 덤프하기
    for i in range(dump):
        # 최고 높이 상자 한칸 내리기
        box[max_search()] -= 1
        # 가장 낮은 상자 한칸 올리기
        box[min_search()] += 1

    print('#{} {}'.format(tc, box[max_search()] - box[min_search()]))


######################################################################
# N의 크기가 크지 않을 때 사용!
# 매번 정렬하면서 값을 뽑는 구조

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        bubble_sort(box)
        box[0] += 1
        box[-1] -= 1

    bubble_sort(box)

    print('#{} {}'.format(tc, box[-1] - box[0]))

#######################################################################
# 풀이 3.
# 정렬하면서 앞뒤 비교하면서 가는 구조


for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    # 누적 카운트
    h_cnt = [0] * 101

    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자.
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value - 1:
        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value - 1] += 1

        # 포인터를 변경하자
        if h_cnt[min_value] == 0:
            min_value += 1
        if h_cnt[max_value] == 0:
            max_value -= 1

        # 덤프 줄이기
        N -= 1

    print('#{} {}'.format(tc, max_value - min_value))


################################################################
# 풀이 4. 유태영 교수님 풀이
# 재귀함수 연습을 하기위해서
# 완성을 다 못한 듯

def solution(dump_limit, boxes):
    for _ in range(dump_limit):
         max_idx = min_idx = 0
        for idx in range(len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx

            elif boxes[idx] < boxes[min_idx]:
                min_idx = idx

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # dump 한 회차가 끝나고 확인하자
        diff = boxes[max_idx] - boxes[min_idx]
        if diff == 0:
            return 0
        elif diff == 1:
            return 1

    #dump_limit 만큼 종료
    max_idx = min_idx = 0
    for idx in range(len(boxes)):
        if boxes[idx] > boxes[max_idx]:
            max_idx = idx

        elif boxes[idx] < boxes[min_idx]:
            min_idx = idx
    return boxes[max_idx] - boxes[min_idx]



for tc in range(1, T + 1):
    dump_limit = int(input())
    boxes = list(map(int, input().split()))
    print('#{} {}'.format(tc, solution()))
