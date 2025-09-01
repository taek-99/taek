# django

## Template System

- 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당

- Template에서 조건, 반복, 변수 드으이 프로그래밍적 기능을 제공

- Variable

    - render함수의 세번째 인자로 딕셔너리 데이터 사용

    - .을 사용하여 변수 속서에 접근

- Filters

    - 표시할 변수를 수정할 때 사용 (변수+|+필터)

- Tags

    - 반복 또는 논리를 수행하여 제어 흐름을 만듦

- Comments

    - DTL에서의 주석

## 템플릿 상속

- 페이지의 공통 요소를 포함하고 하위 템플릿이 재정의 할수 있는 공간을 정의

- skeleton 역살을 하게 되는 상위 템플릿 작성

- extends 태그

    - 자식 템플릿이 부모 템플릿을 확장한다는것을 알림

- block 태그

    - 하위 템플릿에서 재정의 할 수 있는 블록을 정의

## 요청과 응답

- 데이터를 보내고 가져오기

    - form을 사용하여 요청을 서버에 보내는 가장 편리한 방법

- form element

    - 사용자로부터 할당된 데이터를 서버로 전송

- 핵심 속성

    - action

        - 입력 데이터가 전송될 URL을 지정

        - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 url로 보내짐

    - method

        - 데이터를 어떤 방식으로 보낼 것인지 정의

        - 데이터의 HTTP request methods (GET, POST)를 지정

    - input

        - 사용자의 데이터를 입력 받을 수 있는 요소

        - type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

    - name 속성

        - input의 핵심 속성

        - 사용자가 입력한 데이터에 붙이는 이름

    - Query String parameters

        - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법

- Django URLs

    - url dispatcher

        - url 패턴을 정의하고 해당 패턴이 일치하면 가져오는거

    - variable routing

        - url 일부에 변수를 포함시키는것

    