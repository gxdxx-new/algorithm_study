A, B, C = map(int, input().split())
result = 0

if(B <= A <= C):
    result = A
if(C <= A <= B):
    result = A
if(A <= B <= C):
    result = B
if(C <= B <= A):
    result = B
if(A <= C <= B):
    result = C
if(B <= C <= A):
    result = C
print(result)