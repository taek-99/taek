# gTTS 모듈 임포트
from gtts import gTTS


# 텍스트 정의
text = "안녕하세요, gTTS를 이용한 텍스트 음성 변환 예제입니다."

# gTTS 객체 생성
# text: 변환할 텍스트
# lang: 음성의 언어 (여기서는 한국어 'ko')
# slow: 느린 속도로 읽을지 여부 (False는 일반 속도)
tts = gTTS(text=text, lang='ko', slow=False)

# 생성된 음성을 MP3 파일로 저장
# 파일명은 'output.mp3'로 지정
tts.save("output.mp3")
