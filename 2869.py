# A : 하루 오르는 높이, B : 하루 떨어지는 높이, V = 나무의 높이
A, B, V = map(int, input().split())

result = 0
result = (V - B) // (A - B)
if((V - B) % (A - B) != 0):
    result += 1
print(int(result))