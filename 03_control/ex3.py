# for문

# for i in iterable 객체:
#     ... 

for i in range(5):
    print(i, end=" ")

# 5, 4, 3, 2, 1 rjRNfh
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print(total)

s = "HI12!@한글🥹"

for c in s:
    print(c, end=" ")

print('\n' + str(len(s))) # 문자열 길이

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j :<5d}", end = "")
    print()