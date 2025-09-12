# Django

## Web Application
- 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정

- 다양한 디바이스에서 웹 브라우저를 통해 접근하고 사용할 수 있음

- Frontend와 Backend
    
    - Frontend

        - 사용자 인터페이스를 구성하고 사용자가 애플리케이션과 상호작용할 수 있도록 함

        - HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

    - Backend

        - 서버측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당

        - 서버언어 및 벡엔드 프레임워크, 데이터베이스, API, 보안 등

## Framework

- Web Framework

    - 웹 서비스 개발에 필요한 다양한 기술

        - 로그인/ 로그아웃, 회원관리, 데이터베이스, 보안 등

    - 모든 기능을 직접 개발하기에는 현실적 어려움 존재

    - 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구

- Django Framework

    - 파이썬 기반의 대표적인 웹 프레임워크

    - 다양성, 확장성, 보안, 커뮤니티 지원

    - Django를 사용해서 서버를 구현할 것


## 가상 환경

- 가상 환경 생성 및 활성화

    - 하나의 컴퓨터 안에서 또 다른 독립된 파이썬 환경

    - .venv -> source/script/activate

- 의존성 패키지

    - 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리

    - 프로젝트가 의존하는 "개별 라이브러리들"을 가리키는 말

    - 패키지 목록 확인 pip list

    - 같이 개발할땐 패키지 목록 공유 필수

        - pip install -r requirements.txt


- 주의사항 및 권장사항

    - 가상 환경에 들어가고 나오는것이 아닌 ON/OFF로 전환하는 개념

    - 프로젝트마다 별도의 가상환경을 사용

    
- 요악

    - 가상환경 만든다: python -m venv venv

    - 가상환경 활성화: source venv/scripts/acrivate

    - 의존성 패키지 설치: pip install

    - 현재 환경의 패키지 목록 관리 pip freeze -> requirements.txt

    - 다른 컴퓨터나 팀원도 같은 환경이 필요하다면 pip install -r requirements.txt

    - 작업이 끝나면 deactivate로 가상환경 비활성화


## Django 프로젝트

    - 프로젝트 구조 
    
        - settings.py #

            - 프로젝트의 모든 설정을 관리

        - urls.py #
    
            - 요청 들어오는 URL에 따라 이에 해당하는 적절한 VIEWS를 연결

        - __init__.py

            - 해당 폴더를 패키지로 인식하도록 설정하는 파일

        - asgi.py
            
            - 비동기식 웹 서버와의 연결 관련 설정

        - wsgi.py

            - 웹 서버와의 연결 관련 설정

        - manage.py

            - Django프로젝트와 다양한 방법으로 상호작용하는 커멘드라인 유틸리티

    - 앱 구조

        - admin.py

            - 관리자용 페이지 설정

        - models.py

            - DB와 관련된 Model을 정의

            - MTV 패턴의 M

        - views.py

            - HTTP요청을 처리하고 해당 요청에 대한 응답을 반환

            - (URL, MODEL, TEMPLATE과 연계)

        - apps.py

            - 앱의 정보가 작성되는 곳

        - tests.py

            - 프로젝트 테스트 코드를 작성하는 곳

## 디자인 패턴

- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책

- MVC 디자인 패턴

    - 애플리케이션을 구조화하는 대표적인 패턴

    - 데이터/사용자인터페이스/비즈니스로직 을 분리

- MTV 디자인 패턴

    - Django에서 애플리케이션을 구조화하는 패턴
    

## 요청과 응답

- URLs 우선 작성

    - 갈수 있는 urls들 설정

- view

    - 모든 view 함수는 첫번째 인자로 요청 객체를 필수적으로 받음

    - 매개 변수 이름이 request가 아니어도 되지만 그렇게 작성되지 않음

- Template

