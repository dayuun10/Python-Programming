# 함수 2

# ===========================================================
# 1. 지역변수와 전역변수
# ===========================================================
# 함수 안에서 만든 변수는 지역변수로, 함수 밖에서는 사용할 수 없다.
# 함수 밖에서 선언된 변수는 전역변수이며, 함수 안에서는 기본적으로
# "읽기"만 가능하고, 값을 바꾸려면 global 키워드가 필요하다.

a = 1 # 전역변수

def fun():
    global a
    a = 10 # 지역변수 -> 전역변수
    print("함수 안:", a)

fun()
print("함수 밖:", a)

# ===========================================================
#  2. 함수 인자 전달 방식
# ===========================================================
#? 1) call-by-value: 값 자체가 복사되어 전달, 원본과 별도의 메모리 공간을 할당, 함수 내부에서 수정 시 원본 불변
#? 2) call-by-reference: 변수의 주소가 전달, 원본과 같은 메모리 공간을 가리킴, 함수 내부에서 수정 시 원본 변경
#? 3) call-by-assignment: 파이썬은 객체를 가리키는 참조 전달, 원본과 같은 객체를 가리킴(재할당 전까지)
#                        immutable 객체인 경우 call-by-value처럼 동작 -> 함수 내부에서 수정 시 원본 불변
#                        mutable 객체인 경우 call-by-reference처럼 동작 -> 함수 내부에서 수정 시 원본 변경
#                        mutable 객체라도 재할당을 하면 원본과 연결이 끊기고 새로운 객체 할당

def swap(a, b): # 매개변수 a, b가 참조값을 전달받음
    a, b = b, a
    print(id(a),id(b)) 
    print(a, b) # 함수 종료 시 a, b 값이 유효하지 않게 됨. 

a, b = 1, 2 
print(id(a),id(b)) 
swap(a,b) # 2 1
print(a,b) # 1 2


def append_item(num):
    num.append(2)

num = [1]
append_item(num)
print(num)


def swap2(num):
    num[0], num[1] = num[1], num[0]
    print(num)

swap2(num)
print(num) #드디어 바꼈다


def assign(num):
    num = [10]
    print(num)

assign(num) #[2, 1]
print(num)
 
# ===========================================================
# 3. 재귀함수
# ===========================================================

# 팩토리얼 계산하기 (1, 1, 2, 6, 24, ..)
# 점화식: 1 if n <= 1 else f(n) = n * f(n - 1)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))
    
# 피보나치 계산하기 (0, 1, 1, 2, 3, 5, 8, ..)
def fibo(n): 
    return n if n <= 1 else fibo(n - 1) + fibo(n -2)

print(fibo(5))
print([fibo(i) for i in range(11)])

# ===========================================================
# 4. 람다함수
# ===========================================================

# 람다함수 : 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda a, b, ...: 표현식

add = lambda a, b: a + b
print(add)
print(add(3, 4))

students = [
    {"name": "뽀로로", "score": 85},
    {"name": "크롱", "score": 92},
    {"name": "포비", "score": 78},
]

# 이름 순으로 정렬
# print(sorted(students)) #! 딕셔너리라서 비교가 안됨
print(sorted(students, key=lambda s: s["name"])) #TODO 와우
print(sorted(students, key=lambda s: s["score"])) #TODO 와우

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ n이 짝수면 True, 홀수면 False를 반환하는 함수 작성하기
def is_even(n):
    return True if n % 2 == 0 else False
# is_even = lambda x: not x % 2


print(is_even(4))                           # ✅ True
print(is_even(7))                           # ✅ False


# 2️⃣ 가변 인자로 여러 숫자를 받아 (최소값, 최대값, 합계, 평균) 튜플 리턴하기
def num_info(*args):
    tot = sum(args) #? 재사용하자
    return(min(args), max(args), tot, tot / len(args))

print(num_info(4, 8, 1, 9, 3))              # ✅ (1, 9, 25, 5.0)


# 3️⃣ 이름과 키워드 가변 인자로 받은 정보로 아래와 같이 문자열을 만들어 리턴하기

def introduce(name, **kwargs):
    info = [f"{k}: {v}" for k, v in kwargs.items()] #! 우와
    return " / ".join([name] + info)


print(introduce("카리나", age=26, team="에스파", hometown="수원"))
# # ✅ 카리나 / age: 26 / team: 에스파 / hometown: 수원

print(introduce("장원영", age=22, team="아이브", bloodtype="O형"))
# # ✅ 장원영 / age: 22 / team: 아이브 / bloodtype: O형

print(introduce("성현", age=17, team="코르티스"))
# # ✅ 성현 / age: 17 / team: 코르티스


# 4️⃣ 5부터 카운트다운하여 로켓 발사시키기 (재귀함수)
# time.sleep(1)                     # 1초 동안 stop

import time
def countdown(n):
    time.sleep(1)
    print(n)
    if n == "로켓 발사":
        return 0
    return countdown(n - 1) if n > 1 else countdown("로켓 발사")



countdown(5) #5 -> 4 -> 3 -> 2 -> 1 -> 로켓 발사

# 