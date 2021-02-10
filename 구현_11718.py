#몇 번의 입력이 들어올지 몰라서 try except 구문 사용
while True:
    try:
        print(input())
    except EOFError:
        break