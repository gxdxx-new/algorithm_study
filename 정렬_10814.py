members = []
for _ in range(int(input())):
    age, name = map(str, input().split())
    age = int(age)
    members.append((age, name))

members.sort(key=lambda x : (x[0]))

for member in members:
    print(member[0], member[1])