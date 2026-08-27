# 문자열
# "", ''

a = "python"
print(a, type(a))

# I'll be back
print("I'll be back")
print("I'll be back")

multiline = """
Life is short
You need Python
"""
print(multiline)


# docstring
def func():
    # a = 1
    """이 함수는 테스틀용입니다."""
    pass


print(
    func.__doc__
)  # 함수의 첫 번째 줄에 나오는 문자열을 doc string이라고 하는데 이를 출력, 첫 번째 줄에 없으면 None 출력

# 문자열 연결
print("Hello " + "Python")

# 문자열 반복
print("Hello" * 10)
print("*" * 50)
# print("Hello" + 10) 안됨
print("Hello" + str(10))

print("10" + "2")  # 102
print(int("10") + int("2"))

# 문자열 포맷팅 (f-string)
name = "pororo"
age = 23

print(f"이름: {name}")
print(f"나이: {age}살")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")  # 천 단위 콤마
print(f"{num:15d}")
print(f"{num:15,d}")
print(f"{num:<15d}")  # <숫자 d - 왼쪽 (숫자) 칸 만큼 띄우기
print(f"{num:015d}")
