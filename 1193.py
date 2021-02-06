import sys

num = int(sys.stdin.readline())
count = 1
location = 0

while True:
    if(num > (count * (count + 1)) / 2):
        count += 1
    else:
        break

location1 = int(num - (count * (count - 1)) / 2)
location2 = int(count - location + 1)

if(count % 2 == 0):
    print(str(location1) + '/' + str(location2))

if(count % 2 != 0):
    print(str(location2) + '/' + str(location1))