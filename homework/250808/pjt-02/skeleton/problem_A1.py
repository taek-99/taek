import os                       # 운영 체제와 상호작용하기 위한 라이브러리
import requests                 # HTTP 요청을 보내기 위한 라이브러리
from dotenv import load_dotenv  # .env 파일을 읽기 위한 라이브러리


load_dotenv()  # .env 파일을 읽어 환경 변수로 설정합니다.

# 1. [ dotenv를 활용하여 알라딘 API 키 가져오기 ]
MY_TTBKEY = os.getenv('MY_TTBKEY')
# 2. [ 공식 문서를 참고하여 알라딘 API 검색 URL 설정하기 ]
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

# 3. 도서 데이터를 가져오는 함수 정의
def fetch_books(keyword):       # keyword: 검색할 키워드
    url = ALADIN_SEARCH_URL     # 검색 API URL
    params = {
        'TTBKey': MY_TTBKEY,    # API 키 정보
        'Query': keyword,       # 검색할 키워드 정보
        'Output': 'js',         # 응답 형식 (JSON)
        'Version': '20131101',  # API 버전
    }
    # 3.1 [ requests 문서를 참고하여 HTTP GET 요청 보내는 코드 작성하기 ]
    data = requests.get(url, params=params)

    # 3.2 [ requests 문서를 참고하여 응답 데이터를  python의 dict 타입으로 변환하여 data 변수에 저장 ]
    data = data.json()

    return data


# '펭귄' 키워드를 사용하여 도서 검색 데이터를 가져옵니다.
result = fetch_books('펭귄')
# 결과에서 도서 목록을 가져옵니다.
books = result.get('item', [])

# 4. [ 각 도서를 순회하며 넘버링과 제목을 출력하기 ]
# ex) 1. 펭귄이 살아갑니다.
#     2. 펭귄의 ...
for i, v in enumerate(books):
    print (f"{i+1}. {v['title']}")

pass