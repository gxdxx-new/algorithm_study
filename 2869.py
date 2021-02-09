# A : 하루 오르는 높이, B : 하루 떨어지는 높이, V = 나무의 높이
A, B, V = map(int, input().split())

result = (V - A) // (A - B) + 1
if((V - A) % (A - B) == 0):
    print(result)
else:
    print(result + 1)