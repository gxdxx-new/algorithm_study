import sys

X = int(sys.stdin.readline())

i = 1
count = 0
while True:
    if(X > (i*(i+1))/2):
        i += 1
    else:
        break

count = X - (i*(i-1))/2
a = i - count + 1
if(i%2 == 0):
    print(str(int(count)) + '/' + str(int(a)))
if(i%2 != 0):
    print(str(int(a)) + '/' + str(int(count)))