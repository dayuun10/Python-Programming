# 딕셔너리 기초

# ===========================================================
#?  딕셔너리 (dict): 키와 값 쌍으로 저장하는 변경 가능한 자료형
#  딕셔너리의 특징
#  1. mutalbe, 변경 가능
#  2. iterable, 반복 가능
#  3. sequence 자료형이 아니다. (인덱싱, 슬라이싱 불가)
#  4. 키는 중복 불가, 값은 중복 가능
# ===========================================================

# 딕셔너리 생성
a ={}
b = dict()
print(type(a), type(b))

d = {"id": 1328, "name": "한가윤", "age": 17}

# 키로 값 가져오기
print(d["name"])
# print(d["phone"]) # 에러

# 에러가 안나게 하려면?
if "phone" in d:
    print(d["phone"])
print(d.get("email")) # None
print(d.get("email", "없음")) # 없음

# ===========================================================
# 1. 딕셔너리는 mutable하다. (변경 가능)
# ===========================================================

d["age"] += 1
print(d) #// {'id': 1328, 'name': '한가윤', 'age': 18}

d["phone"] = "010-1234-5678" #? 추가
print(d) #// {'id': 1328, 'name': '한가윤', 'age': 18, 'phone': '010-1234-5678'}

del d["phone"] #? 삭제
print(d) #// {'id': 1328, 'name': '한가윤', 'age': 18}

d.pop("age") #? 메소드로 삭제
print(d) #// {'id': 1328, 'name': '한가윤'}

# ===========================================================
# 2. 딕셔너리는 iterable하다. (반복 가능)
# ===========================================================

# 딕셔너리 순회
for key in d:
    print(key, d[key])

for i, key in enumerate(d):
    print(i, key) #// 0 id

for value in d.values():
    print(value) #// 1328, 한가윤

for key, value in d.items():
    print(key, value) #// id 1328, name 한가윤


# ===========================================================
# 3. 딕셔너리는 sequence 객체가 아니다. (인덱싱, 슬라이싱 불가)
# ===========================================================

d[0] = "python"
print(d) #// {'id': 1328, 'name': '한가윤', 0: 'python'}



# ===========================================================
# 4. 딕셔너리는 키는 중복 불가, 값은 중복 가능하다.
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

d["kor"] = 100 #? 키가 중복되면 값이 덮어써짐
print(d) #// {'kor': 100, 'mat': 85, 'eng

d["sci"] = 980 #? 값은 중복 가능
print(d) #// {'kor': 100, 'mat': 85, 'eng': 80, 'sci': 980}

# d[[1, 2]] = 100 #? 리스트는 mutable이라 키로 불가
d[(1, 2)] = 100

# 키로 가능한 것 : immutable 타입 (숫자형, 불리언, 문자열, 튜플) -> hashable type
# 키로 안되는 것 : mutable 타입 (리스트, 딕셔너리, 집합) -> unhashable type
# 키는 해시 가능(hashable) + 프로그램 실행 동안 hash값이 변하지 않아야 함

print(hash(12345))
print(hash("python"))
print(hash((1, 2)))
# print(hash([1, 2])) #! 리스트는 mutable이라 hash값을 계산할 수 없음

print(hash(12345))
print(hash("python"))
print(hash((1, 2)))

# 딕셔너리가 저장되는 방식
# 1. 딕셔너리 데이터를 저장하기 위한 해시 테이블을 생성함
# 2. hash(key) 함수를 통해 hash값을 얻음
# 3. hash값을 테이블 크기로 압축하여 버킷 인덱스를 계산하고 해시 테이블에 저장함
# 4. key값으로 조회할 때에도 hash(key)로 hash값을 얻어낸 후(동일 hash값) 해당 인덱스로 가서 조회함

# 만약 key에 mutable 타입을 허용했다면?
# 1. hash(key) 함수로 hash값을 얻어 해시 테이블에 저장함
# 2. key 내용이 변경됨
# 3. 다시 hash(바뀐key)를 하면 새로운 hash값이 나옴
# 4. 새 hash값을 이용하여 버킷 인덱스를 계산하고 해시테이블에 조회를 하면 원래 데이터를 찾을 수 없음



# ===========================================================
#  파이썬 내장 함수
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

print(len(d)) #// 3 
#? 키 값
# print(sum(d)) #! 오류남
print(sum(d.values())) #// 255
print(min(d)) #// eng
print(max(d)) #// mat
print(max(d), max(d.values())) #// mat 90

print(sorted(d)) #// ['eng', 'kor', 'mat']
print(sorted(d.items())) #// [('eng', 80), ('kor', 90), ('mat', 85)] 
print(dict(sorted(d.items()))) #// {'eng': 80, 'kor': 90, 'mat': 85}

# value 기준 정렬하기
def key(x):
    return x[1]

print(dict(sorted(d.items(), key=key))) #// {'eng': 80, 'mat': 85, 'kor': 90}
print(dict(sorted(d.items(), key=key, reverse=True))) #// {'kor': 90, 'mat': 85, 'eng': 80}

# 정렬 기준 설정하기
# lambda: 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda 매개변수1, 매개변수2, ... : 표현식

print(dict(sorted(d.items(), key=lambda x: x[1]))) #// {'eng': 80, 'mat': 85, 'kor': 90}



# 딕셔너리 합치기
d2 = {"sci": 95, "prog": 100}
# print(d + d2) #! 오류 
d.update(d2)
print(d) #// {'kor': 90, 'mat': 85, 'eng': 80, 'sci': 95, 'prog': 100}

# 딕셔너리 반복하기
# print(d * 2) #! 오류

# 멤버십 연산자
print("kor" in d)
print("art" in d)
print(90 in d.values())