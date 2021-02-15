N = int(input())

array = []

for i in range(N):
    array.append(int(input()))

array.sort()

for j in range(N):
    print(array[j])