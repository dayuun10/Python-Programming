# 1. 모듈

# 자주 사용하는 기능을 모아놓은 파이썬 #! 파일 한 개
# 모듈에는 함수, 클래스, 변수를 정의할 수 있다.

# 모듈(패키지)의 종류
# 1. 표준 라이브러리 모듈(패키지): 파이썬 제공
# 2. 써드 파티 모듈(패키지): 외부에서 만들어서 배포
# 3. 사용자 정의 모듈(패키지)

# =====================================================================
# 1. 파이썬 표준 라이브러리 불러오기 (https://docs.python.org/3/library)
#  - import 모듈명
#  - from 모듈명 import 함수명
#  - from 패키지명 import 모듈명 (from 가져올 위치 import 가져올 대상)
# =====================================================================

# math 모듈: 수학 계산에 필요한 함수와 상수를 제공하는 표준 라이브러리
import math
print(dir(math))
# print(math.sprt(16))
print(math.pi)
from math import sqrt, pi

print(sqrt(16))
print(pi)

# 별칭 만들기



# 모듈명 없이 바로 함수명으로 불러오기



# 여러 함수 불러오기



# sys 모듈: 파이썬 인터프리터의 실행 환경과 관련된 정보를 제공하는 표준 라이브러리
import sys

                  # 현재 실행 중인 파이썬 인터프리터의 버전
                 # 현재 실행 중인 운영체제 플랫폼 식별자
                     # 파이썬 라이브러리 검색 디렉토리 목록

# 표준 라이브러리 설치 경로: C:\Users\<user_name>\AppData\Local\Programs\Python\Python314\Lib
# 써드 파티 설치 경로: C:\Users\<user_name>\AppData\Local\Programs\Python\Python314\Lib\site-packages


# ===========================================================
# 2. 써드 파티 모듈 불러오기 (https://pypi.org/)
#  - 패키지 목록 보기: pip list
#  - 패키지 설치 하기: pip install 패키지명
# ===========================================================

# requests 모듈: HTTP 요청과 응답을 처리하기 위한 써드 파티 모듈

import requests

url = "https://httpbin.org/get?user_id=crong" # 물음표 다음에 키와 벨류, 구글에 검색해봐도 나옴, text의 args에 나옴

response = requests.get(url)

print(response.status_code) # 응답코드, 200: 정상, 404: 에러
print(response.text)
print(type(response.text)) #. 엥 스트링? >> 딕셔너리 변환 필요

# 직렬화와 역직렬화
# - 직렬과(Serialization): 메모리 상의 객체를 파일 저장 or 전송이 가능한 형태로 변한
# - 역직렬화 Deserialization): 저장된 파일 또는 or 전송을 받은 데이터를 원래의 객체로 복원
# - 대에터 직렬화 방식: XML, JSON, YAML

# 객체 변한
d = response.json() # 역직렬화, 서버가 응답한 JSON 형식의 문자열을 Python 객체로 변환 

print(type(d)) # 와우 딕셔너리

print(d["args"]["user_id"]) # 우와 크롱 잘 나와요
print(d["headers"]["Host"])
 
# ===========================================================
# 3. 사용자 정의 모듈 만들기
# ===========================================================

import mymath # 같은 디렉토리에 있어서 잘 보임, 임포트만 했는데도 실행이 됨. __name__ 은 mymath라고 나옴. 
from mymath import PI, add

print(mymath.PI)
print(mymath.add(20, 30))

print(PI)
print(add(40, 50))

#? __pycache__ 디렉토리란?
#? Python이 실행 속도를 높이기 위해 컴파일된 바이트코드(.pyc)를 캐시로 저장하는 디렉터리
#? 모듈을 import할 때만 생성되고, 직접 실행할 때에는 바이트코드까지만 생성하고 저장하지는 않음


#? Python 모듈 실행 방식
#? 1. CPython에 있는 컴파일러가 Python 소스 코드를 **바이트코드(.pyc)**로 컴파일
#? 2. Python 가상 머신(PVM)이 바이트코드를 실행
#? 3. 다음 실행 시에는 .pyc를 바로 읽어 실행
#? 4. 모듈이 변경된 경우 .pyc 파일을 재생성하여 실행