N = int(input())
count = 2 * N -1
star = count

for i in range(N):
    print(' ' * ((count - star) // 2) + '*' * star)
    star -= 2
star += 2
for j in range(N-1):
    star += 2
    if(j == N-2):
        print(' ' * ((count - star) // 2) + '*' * star, end='')
    else:
        print(' ' * ((count - star) // 2) + '*' * star)