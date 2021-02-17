N = int(input())
numList = []

for i in range(N):
    x, y = list(map(int, input().split()))
    numList.append((x,y))

sortedNumList = sorted(numList)

for j in range(N):
    print(sortedNumList[j][0], sortedNumList[j][1])

# a = [(4,0), (4,3), (4,2), (3,2), (2,1), (1,0)]

# 인자 없이 sorted()를 사용하면 리스트 아이템의 각 요소 순서대로 정렬
# 첫 번째 요소가 같으면 두 번째 요소로 비교
# b = sorted(a)
# print(b)    # [(1, 0), (2, 1), (3, 2), (4, 0), (4, 2), (4, 3)]

# key인자에 lambda 함수를 넘겨주면 반환값을 가지고 비교해 정렬
# 이 때, key로 전달되지 않은 요소에 대해선 정렬하지 않음
# c = sorted(a, key=lambda x : x[0])
# print(c)    # [(1, 0), (2, 1), (3, 2), (4, 0), (4, 3), (4, 2)]
# d = sorted(a, key=lambda x : x[1])
# print(d)    # [(4, 0), (1, 0), (2, 1), (4, 2), (3, 2), (4, 3)]

# 정렬 기준으로 다중 조건을 넘겨줄 수도 있다
# 첫 번째 인자를 기준으로 오름차순 정렬을 먼저 한다.
# 그 결과를 가지고 두 번째 인자를 기준으로 내림차순 정렬(-를 붙이면 내림차순 정렬)
# e = sorted(a, key = lambda x : (x[0], -x[1]))
# print(e)    # [(1, 0), (2, 1), (3, 2), (4, 3), (4, 2), (4, 0)]