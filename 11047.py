N,K=map(int,input().split())

array=[0]*N
count=0

for i in range(0,N):
    array[i]=int(input())

array.reverse()

for j in array:
    count += K//j
    K = K%j

print(count)