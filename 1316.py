T = int(input())

count = 0
for _ in range(T):
    word = list(input())
    for i in range(len(word)):
        if (i == (len(word) - 1)):
            count += 1
            break
        if(word[i] != word[i + 1]):
            if(word[i] in word[i + 1:]):
                break
print(count)