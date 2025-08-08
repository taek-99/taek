# 참고 문서
# https://pypi.org/project/python-dotenv/

# 필요한 모듈 임포트
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 접근
API_KEY = os.getenv('API_KEY')
MY_DATABASE_URL = os.getenv('DATABASE_URL')
DEBUG_MODE = os.getenv('DEBUG_MODE', 'False')  # 환경 변수가 없을 시 기본값 'False' 설정

# 환경 변수 사용 예시
print(f"API Key: {API_KEY}")
print(f"Database URL: {MY_DATABASE_URL}")
print(f"Debug Mode: {DEBUG_MODE}")

# 환경 변수를 활용한 조건문 예시
if DEBUG_MODE.lower() == 'true':
    print("디버그 모드가 활성화되었습니다.")
else:
    print("디버그 모드가 비활성화되었습니다.")

