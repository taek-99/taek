import requests

# 간단한 요청 예제
URL = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(URL).json() # JSON 응답을 Dictionary로 변환환
print(response)

results = response.get('message')   # 응답 결과에서 필요한 부분 가져오기기
print(results)