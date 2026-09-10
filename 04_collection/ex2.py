# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

langs.append("go")# 끝에 추가
print(langs) #//['c', 'c++', 'java', 'python', 'go']

langs.insert(2, "c#")               # 인덱스 2에 "c#" 추가
print(langs) #// ['c', 'c++', 'c#', 'java', 'python', 'go']

langs[3] = "javascript"             # 인덱스 3을 "javascript"로 변경
print(langs) #// ['c', 'c++', 'c#', 'javascript', 'python', 'go']

langs.remove("c++")                 # "c++" 삭제 (첫번째 데이터만 삭제)
print(langs) #// ['c', 'c#', 'javascript', 'python', 'go']

langs.pop(1)                         # 인덱스 1 삭제
print(langs) #// ['c', 'javascript', 'python', 'go']

langs.pop()                         # 인덱스 생략 시 #?마지막 항목 삭제
print(langs) #// ['c', 'javascript', 'python']

print(langs.index("python"))        # "python" 인덱스 찾기, #! value가 없으면 에러
#// 2

langs.reverse()                     # 리스트 순서를 거꾸로 뒤집기
print(langs) #// ['python', 'javascript', 'c']

langs.sort()                        # 오름차순 정렬
print(langs) #// ['c', 'javascript', 'python']

langs.sort(reverse = True)            # 내림차순 정렬
print(langs) #// ['python', 'javascript', 'c']

langs.clear()                       # 모든 item 삭제
print(langs) #? [] >>빈 리스트만 남음

# 리스트 복사
ori = [1, 2, 3]

result = ori.copy()
result.append(10)

print(ori, result) #// [1, 2, 3] [1, 2, 3, 10]

# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]

result = ori.copy()
result[0].append(10)
print(ori, result) #// [[1, 2, 10], [3, 4]] [[1, 2, 10], [3, 4]]


# 깊은 복사를 하려면?
import copy
result2 = copy.deepcopy(ori)
result2[0].append(100)



# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1][1][0])         # x 출력하기
print(nested_list[1][2])            # b 출력하기
print(nested_list[2])               # 2 출력하기

# 리스트 언패킹
nums = [1, 2, 3, 4]

print(*nums) #// 1 2 3 4

a, b, c, d = nums
print(a, b, c, d) #// 1 2 3 4

a, *b, c = nums
print(a, b, c) #// 1 [2, 3] 4

nums2 = [5, 6]
print(nums + nums2) #// [1, 2, 3, 4, 5, 6]
print([*nums, *nums2]) #// [1, 2, 3, 4, 5, 6]

# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어"]
scores = [80, 90, 95]


a, b, c = (zip(subjects, scores)) # >> 튜플 형태로
print(a, b, c) #// ('국어', 80) ('수학', 90) ('영어', 95)

print(list(zip(subjects, scores))) #? 대괄호로 묶으면 튜플을 그대로 리스트로 만듦

for subject, score in zip(subjects, scores):
    print(f"{subject}: {score}점")
#// 국어: 80점
#// 수학: 90점
#// 영어: 95점

# ===========================================================
#  List Comprehension #? 미영쌤이 사랑하는 기능
#? 가독성도 좋고 속도도 좋고 코드 길이도 짧다
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
result = []
for x in range(1, 11):
    result.append(x ** 2)
print(result)

result = [x ** 2 for x in range(1, 11)] #? 가독성이 좋다 + 실행속도
print(result)

# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)
result = [x ** 2 for x in range(1, 11) if x % 2 == 0] #!if 하나만 있으면 for 뒤에
print(result)

# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기
result = ["짝" if x % 2 == 0 else "홀" for x in range(1, 11)] #! else 있으면 for 앞에, elif는 안됨
print(result)

# 각 이름의 길이로 이루어진 리스트 만들기
names = ["pororo", "crong", "poby", "eddy"]
result = [len(i) for i in names]
print(result)

# 길이가 5 이상인 이름만 뽑기
result = [x for x in names if len(x) >= 5]
print(result)

# 중첩 for문도 가능
# x = 0.12        
# y = 0.12
result = [x * y for x in range(3) for y in range(3)]
print(result)

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
scores = [85, 42, 73, 55, 90, 68, 35, 100]

result = [x for x in scores if x >= 60]
print(result)                       # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
result = ["합격" if score >= 60 else "불합격"]
print(result)                       # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
result = [x for x in range(0, 100) if x % 3 == 0 or x % 5 == 0]
result = [x for x in range(0, 100) if not x % 3 or not x % 5]
print(sum(result))                       # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
words = ["apple", "banana", "kiwi", "mango"]

result = [w for w in words if "n" in w] #! 몰랏다
result = [w for w in words if w.find("n")] 
result = [w for w in words if w.count("n")] 
print(result)                       # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
scores = [
    [90, 80, 70],       # 학생 1
    [100, 90, 80],      # 학생 2
    [80, 70, 60],       # 학생 3
]

std1 = scores[0] 
std2 = scores[1]
std3 = scores[2]                                                                                                                                                                                                                                                                
esult = [round(sum(score) / len(score), 2) for score in zip(std1, std2, std3)] #? round(수, 반올림할 자릿수)
esult = [round(sum(score) / len(score), 2) for score in zip(*scores)]
print(result)                       # ✅ [90.0, 80.0, 70.0]


# + 오차를 상쇠하는 round
print(round(0.5)) # 0
print(round(1.5)) # 2
print(round(2.5)) # 2
print(round(3.5)) # 4