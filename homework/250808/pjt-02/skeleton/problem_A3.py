import os                       # 운영 체제와 상호작용하기 위한 라이브러리
import requests                 # HTTP 요청을 보내기 위한 라이브러리
from gtts import gTTS           # 텍스트를 음성으로 변환하기 위한 라이브러리
from dotenv import load_dotenv  # 환경 변수 로드를 위한 라이브러리


load_dotenv()  # .env 파일을 읽어 환경 변수로 설정합니다.

# 1. [ dotenv를 활용하여 알라딘 API 키 가져오기 ]
MY_TTBKEY = os.getenv('MY_TTBKEY')
# 2. [ 공식 문서를 참고하여 알라딘 API 검색 URL 설정하기 ]
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

# 3. 도서 제목 가져오는 함수 정의
def fetch_book_title(keyword):
    url = ALADIN_SEARCH_URL
    params = {
        "TTBKey": MY_TTBKEY,    # API 키
        "Query": keyword,       # 검색 키워드               
        "Version": "20131101",  # API 버전
    }

    # 3.1 [ requests 문서를 참고하여 HTTP GET 요청 보내는 코드 작성하기 ]
    data = requests.get(url, params=params)

    # 3.2 [ requests 문서를 참고하여 응답 데이터를  python의 dict 타입으로 변환하기 ]
    data = data.json()

    # 3.3 [ 첫 번째 도서 제목 추출하여 title 변수에 저장하기 ]
    title = data['title']

    return title


# 4. TTS 파일 생성 함수 정의
def create_tts_file(keyword, output_file):
    # 4.1 [ 첫 번째 도서 제목 가져오기 ]
    pass  # fetch_book_title 함수 호출로 도서 제목 가져오기
    title = fetch_book_title(keyword)

    if title:
        # 4.2 [ gTTS를 사용해 title의 내용으로 음성 파일 생성하기 ]
        tts = gTTS(title, lang='ko', slow=False)

        tts.save(output_file)  # 음성 파일 저장
        print(f"음성 파일이 {output_file}로 저장되었습니다.")
    else:
        print("도서 제목을 가져오는데 실패했습니다.")


# 함수 실행 (output 폴더가 없으면 생성 필요)
if __name__ == '__main__':
    create_tts_file("자격증", "output/book_title.mp3")
