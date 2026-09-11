# 연산자 .

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # 나머지
print(a // b) # 몫
print(a ** b) # 거듭 제곱

# 복합 대입 연산자
a = 0
a += 4
print(a)

# 증감 연산자
# a++   --> 안됨

# 비교 연산자
print(3 == 3.0) # type은 달라도 값만 같으면 True
print(3 != 4)
print("apple" < "apble")
print(1 < 2 < 3) # 1 < 2 and 2 < 3
print(1 < 3 < 2)

# 논리 연산자 (and, or, not)
a = True
b = False
print(a and b)
print(a or b)
print(not b)

# Short-circuit 테스트
a = 10
b = 0

# print(a/b) # ZeroDivisionError

# Short-Circuit O
if a > 0 or a / b :
    print("yes")
else :
    print("no")
    