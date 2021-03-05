N = int(input())

count = 0

def number(n):
    N = n
    sum = 0

    if(1<= N <= 99):
        sum+=1
    elif(100<= N <= 999):
        if((N%10)-((N//10)%10) == ((N//10)%10)-(N//100)):
            sum+=1

    return sum

for i in range(1,N+1):
    count += number(i)
print(count)