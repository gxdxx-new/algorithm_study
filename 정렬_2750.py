N = int(input())

array=[0]*N

for i in range(0,N):
    array[i]=int(input())

array.sort()

for j in range(0,N):
    print(array[j])