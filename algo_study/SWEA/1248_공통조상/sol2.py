import sys

sys.stdin = open("input.txt")


def searchAnce(n):
    s = tree[n][2]
    p = []
    while s != 0:
        p.append(s)
        s = tree[s][2]
    return p


def findA(p1, p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]
    return 0 # 공통조상 없을 때

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1  # root
        preorder(tree[node][0])  # 왼쪽
        preorder(tree[node][1])  # 오른쪽


T = int(input())
for tc in range(1, T + 1):
    # 정점수, 간선수, 노드 1, 노드 2
    V, E, n1, n2 = map(int, input().split())
    # print(V, E, n1, n2)

    # 3개 이유가 자식2 , 부모 넣기 위해서 3개
    tree = [[0] * 3 for _ in range(V + 1)]
    temp = list(map(int, input().split()))

    for i in range(E):
        p = temp[i * 2]
        c = temp[i * 2 + 1]
        if tree[p][0] == 0:  # 왼쪽자식이 없으면
            tree[p][0] = c  # 왼쪽 자식에 저장
        else:
            tree[p][1] = c  # 오른쪽 자식에 저장
        # 부모자리를 넣어줘야 되서
        tree[c][2] = p  # 부모노드로 저장

    # for i in tree:
    #     print(*i)

    p1 = []  # n1의 조상들 저장
    p2 = []  # n2의 조상들 저장
    p1 = searchAnce(n1)
    p2 = searchAnce(n2)
    CA = findA(p1, p2)
    cnt = 0
    preorder(CA)

    print('#{} {} {}'.format(tc, CA, cnt))
