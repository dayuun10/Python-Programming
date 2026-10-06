# 사용자 정의 모듈
print("start:", __name__) # 모듈의 이름을 가져옴, 직접 실행하면 __main__으로 나오고, 다른 데에서 호출하면 달라짐
PI = 3.14

def add(a, b):
    return a + b

print(PI)
print(add(10, 20))