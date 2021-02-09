memo = list(input())
result = []

for i in range(len(memo)):
    if(str(memo[i]).isupper()): #isupper() : str만 가능
        result.append(memo[i])

for j in range(len(result)):
    print(result[j], end='')