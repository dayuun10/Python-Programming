# 변수
a = 2
b = 3

print(a, end="")  # 엔터키 x
print(b)
print(
    a, b, sep=""
)  # a, b 쓰면 자동으로 스페이스 키가 눌리는데 주고 싶은 seperator을 적어주면 그에 맞게 출력 됨

# a = 2, b = 3 한 줄로 바로 선언하는 것 안됨 - 저렇게 쓰면 a = (2, b) = 3와 같이 튜플로 묶이기 때문에 안됨 (튜플에다가 3넣으라는 말이 되기 때문)
# 한 줄에 다 쓰고 싶으면 ; 으로 구분할 수 있긴 함 - 권장 x
# a = 2; b = 3

a, b = 2, 3  # 주로 이렇게 씀, 튜플 언패킹
# a, b = (2, 3) 자동으로 튜플로 묶이고 알아서 묶인 튜플을 a, b로 나누는? unpacking 작업이 됨

a = b = c = 0  # 연쇄 대입 가능

# 값 swap - temp 변수 써도 되긴 하지만 python에선 아래와 같은 코드로 swap 할 수 있음
a, b = 2, 3
b, a = a, b
print(a, b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어는 사용 불가

# snake_case
# camelCase

# name! = "pororo" 안됨
# 2name = "pororo" 안됨
# class = "test"
# Python에선 변수명 한국어로 쓸 수 있긴 하지만 권장 X
