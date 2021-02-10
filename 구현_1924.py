x, y = map(int, input().split())

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sumDate = 0

for i in range(x-1):
    sumDate += date[i]
sumDate += y
result = sumDate % 7

print(day[result])