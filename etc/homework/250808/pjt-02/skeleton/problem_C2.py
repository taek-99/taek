import os
import requests
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# 1. [ 환경 변수 로드 ]


# 2. OpenAI API 클라이언트 초기화
client = OpenAI(api_key=OPENAI_API_KEY)


# 3. [ 최대 100개까지 주제별 도서 데이터를 가져오는 함수 정의 ]
def fetch_books_by_topic(topic, max_results=100):
    pass


# 4. 책 데이터를 ChatGPT로 분류하는 함수 정의 (습관, 시간관리, 독서법, 기타)
def classify_books_with_gpt(books):
    # 4.1 [ 분류할 책 제목들을 전달하기 편한 문자열로 취합 ]
    pass

    # 4.2 [ ChatGPT 대화 메시지 설정 (프롬프트 작성) ]
    # 습관, 시간관리, 독서법, 기타 로 분류
    conversation_history = [
        {"role": "system", "content": ""},      # 페르소나 작성
        {"role": "user", "content": ""}         # 요청 프롬프트 작성
    ]

    # 4.3 [ 생성형 AI에 분류 요청 보내기 ]
    # client.chat.completions.create() 호출 (example 코드 참고)
    pass  

    # 4.4 [ ChatGPT의 응답을 가져와 JSON 으로 추출 ]
    # ! 주의. JSON 형태로 프롬프팅을 하지 못하면 파싱에서 에러가 발생할 수 있습니다.
    pass  # 응답에서 JSON 데이터를 추출하고 파싱

    return classification   # 분류 정보 반환


# 5. [ 데이터를 JSON 파일로 저장하는 함수 정의 ]
def save_to_json(data, filename):
    pass


# 6. '독서' 도서 데이터를 처리하는 함수 정의
def process_reading_books():
    # 6.1 [ '독서'와 관련된 도서 검색 (100개) ]
    pass  # fetch_books_by_topic() 호출

    # 6.2 [ 생성형 AI를 이용해 책 분류 ]
    pass  # classify_books_with_gpt() 호출

    # 6.3 [ 분류된 책 정보를 JSON 파일로 저장 ]
    # output/reading_habits.json 으로 저장하기
    pass  # save_to_json() 호출

    # 완료 메시지 출력
    print("'output/reading_habits.json' 파일이 생성되었습니다.")


# 함수 실행
if __name__ == '__main__':
    process_reading_books()
