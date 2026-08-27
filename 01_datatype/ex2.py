# 파이썬 자료형
# 1. 기본 자료형 : 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형 : 리스트, 튜플, 딕셔너리, 집합

# 숫자형(정수형)
# int

a = 10
print(a, type(a))

# 2진수, 8진수, 10진수
print(bin(a), oct(a), hex(a))
# 0b, 0o, 0x가 붙는 건 2진수, 8진수, 10진수 임을 알려주기 위함임
print(ord("A"), chr(65))  # 아스키 코드 알려주는 거

# 정수형의 데이터 표현 범위
# int 자료형의 표현 범위는 제한 없음
# 더 큰 값이 들어오면 그때마다 크기를 늘려 저장하기 때문 (c - 배열)

x = 10**100
print(x)

# 오버 플로우 x
a = 2**31 - 1
a = a + 1
print(a)

# 실수형(float)
b = 3.14
print(b, type(b))

# 실수형의 표현 범위 - 무한 소수가 있기 때문에 정확하게 표현이 안되기 때문에 표현 범위에 제한이 있음
# 부동 소수점 방식 : 64비트 = 부호(1비트) + 지수부(11비트) + 가수부(52비트)

import sys

print(sys.float_info.min)
print(sys.float_info.max)

print(-sys.float_info.min)
print(-sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b)
# inf가 출력됨

# 실수의 오차
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
# sys.float_info.epsilon

# 형 변환
print(float(10))
print(int(3.14))
print(int("100"))
print(float("3.14"))
# print("3.14") 안됨
