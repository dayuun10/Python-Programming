# __init__.py 파일 (패키지 초기화 파일)
# 빈 파일이라도 패키지 만들 땐 만드는게 예의

# 1. 패키지를 import할 때 실행되는 초기화 코드 작성 가능
print("__init__")

# 2. 패키지 메타데이터 설정 (버전 정보, 작성자 등)
VERSION = "1.0.0"

# 패키지 re-export

from mypackage.mymath import add # 절대 import 방식
from .mymath import add # tkdeo dlavhxm
