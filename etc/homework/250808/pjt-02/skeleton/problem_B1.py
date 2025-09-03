import os  # 운영 체제와 상호작용하기 위한 라이브러리
import requests  # HTTP 요청을 보내기 위한 라이브러리
from dotenv import load_dotenv  # .env 파일에서 환경 변수를 로드하기 위한 라이브러리


load_dotenv()  # .env 파일을 읽어 환경 변수로 설정합니다.

# 1. [ dotenv를 활용하여 알라딘 API 키 가져오기 ]
MY_TTBKEY = os.getenv('MY_TTBKEY')
# 2. [ 공식 문서를 참고하여 알라딘 API 검색 URL 설정하기 ]
ALADIN_SEARCH_URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

# 3. 주제별 도서 데이터를 가져오는 함수 정의
def fetch_books_by_topic(topic, max_results=30):
    url = ALADIN_SEARCH_URL
    # 3.1 [ API 요청에 필요한 파라미터 설정 (문서 참고하여 작성해보기) ]
    params = {
        "TTBKey": MY_TTBKEY,    
        "Query": topic,      
        'output': 'js', 
        "Version": "20131101", 
        'MaxResults': max_results
    
    }
    # 3.2 [ HTTP 요청 보내고 응답 데이터를 JSON 형식으로 반환하기 ]
    data = requests.get(url, params=params)
    data = data.json()
  
    return data

# 4. 도서 데이터를 수집하고 분석하는 함수 정의
def collect_and_analyze_books():
    # 주제 별로 검색할 책 정보
    topics = ['자연', '예술', '기술']
    all_books = []  # 모든 책 정보를 담을 리스트
    topic_stats = {}  # 주제별 통계를 저장할 딕셔너리
    overall_price = 0  # 전체 가격 합계
    overall_year = 0  # 전체 출판 연도 합계

    # 5.1 [ fetch_book_by_topic 함수 완성 후 주제별 도서 데이터 검색하여 가져오기 ]
    for topic in topics:
        # 5.2 [ all_books 리스트에 가져온 도서 데이터 추가하기 ]
        data = fetch_books_by_topic(topic)
        books = data.get('item', [])
        all_books += books

        # 5.3 [ 주제별 가격 및 출판 연도 수집하기 ]
        prices = []         # 가격 리스트
        pub_years = []      # 출판 연도 리스트
        for book in books:
            prices.append (book['priceSales'])
            pub_data = int(book['pubDate'][0:4])
            pub_years.append (pub_data)

        # 5.4 [ 평균 가격, 연도 계산하기 ]
        # 연도는 정수형으로 변환
        avg_pub_year = sum(pub_years) // len(pub_years)
        avg_price = sum(prices) / len(prices)

        topic_stats[topic] = {
            'avg_price': avg_price,
            'avg_pub_year': avg_pub_year
        }

        # 5.5 [ 전체 도서 평균 가격과 평균 연도 구하기]
        overall_price += topic_stats[topic]['avg_price']
        overall_year += topic_stats[topic]['avg_pub_year']


    overall_avg_price = overall_price / 3
    overall_avg_year = overall_year // 3

    # 계산 결과 출력
    print("통합된 도서 수:", len(all_books))
    print(f"\n전체 통계: 평균 가격 {overall_avg_price:.0f}원, 평균 출판 연도 {overall_avg_year}")

    for topic in topics:
        print(f"{topic} 주제 통계:")
        print(f"  평균 가격: {topic_stats[topic]['avg_price']:.2f}원")
        print(f"  평균 출판 연도: {topic_stats[topic]['avg_pub_year']}")


# 함수 실행
if __name__ == '__main__':
    collect_and_analyze_books()

