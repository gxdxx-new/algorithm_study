word = input()

count = len(word) // 10

#10자 미만, 단어 길이가 10의 배수가 아닐 경우도 고려해서 출력
for i in range(count):
    print(word[i*10: (i+1)*10])
print(word[count*10:])