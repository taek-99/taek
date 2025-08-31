# 평가 대비

## HTML

- Hyper Text

    - 웹 페이지를 다른 페이지로 연결하는 링크

    - 비선형성, 상호연결서르 사용자 주도적 탐색

- Markup Language

    - 태그등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- HTML 속성

    - 사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값

    - 목적

        - 나타내고 싶지 않지만 추가적인 기능 내용을 담고 싶을때 사용

    - 작성 규칙

        - 속성은 요소이름과 속성 사이에 공백이 있어야함

        - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함

        - 속성 값은 열고 닫는 따옴표로 감싸야함

- 대표적인 HTML 속성

    - p

        - 문단의 약자로 텍스트 문단을 만드는 태그

    - a

        - 닻의 약자로 다른페이지로 이동시키는 하이퍼링크 태그

    - img

        - 이미지의 약자로 src에 지정된 그림을 보여주는 태그

## CSS

- 인라인 스타일
    
    - HTML 요소 안에 style 속성 값으로 작성

    - p style=""이런거

- 내부 스타일 시트

    - head 태그 안에 style 태그 작성

- 외부 스타일 시트

    - 별도의 css 파일 생성후 html link태그를 사용해 불러오기

- 스타일 적용 우선순위는 인라인-내부-외부 순으로 적용

- 인라인 스타일은 재사용이 어렵고 유지보수를 방해하므로 권장 X


- css 선택자

    - html 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

    - 전체 선택자 - *

        - HTML 모든 요소를 선택

    - 요소 선택자 - h1~6, p, div

        - 지정된 모든 태그를 선택

    - 클래스 선택자 - .abc

        - 주어진 클래스 속성을 가진 모든 요소를 선택
    
    - 아이디 선택자 - idabc

        - 주어진 아이디 속성을 가진 요소 선택

        - 아이디는 하나만 있어야함

    - 속성 선택자 - [abc]

        - []사용

## 명시도

- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘

- !Important - Inline - id - class - 요소 - 코드 선언 순

## css 박수 구성 요소

- content

    - 실제 내용이 위치하는 영역

- padding 

    - content와 border 사이의 내부 여백

- border

    - content와 padding을 감싸는 테두리

- margine

    - 이 박스와 다른 요소와의 외부 간격

- 단축 속성

    - width, style, color를 한꺼번에 작성 가능 순선 상관 x

    - 4방향의 속성을 한번에 지정 가능

    - 상/우/하/좌, 상/우좌/하, 상하/좌우, 공통

- width와 height를 지정하면 content box의 크기를 조정하게 됨

- css는 border box가 아닌 content box의 크기를 width 값으로 지정

- 대체 상자 모델에서 모든 width와 height는 실제 상자의 너비

## 디스플레이 속성

- Block 타입

    - 하나의 독립된 덩어리처럼 동작하는 요소

    - 항상 새로운 행으로 나뉨(너비 100%)

    - width, height, margin, padding속성을 모두 사용할 수 있음

    - width를 지정하지 않으면 항상 모두 차지

    - h1~h6, p, div, ul, li

    - 헤더, 푸터, 사이드 바 등 웹페이지의 다양한 섹션을 구조화하는데 가장 많이 쓰이는 요소

- Inline 타입

    - 문장 안의 단어처럼 흐름에 따라 자연스러베 배치 되는요소

    - 줄 바꿈이 일어나지 ㅇ낳음

    - 너비, 높이 사용 불가

    - 수직방향은 다른 요소 밀어내기 불가

    - 수평 방향은 다른 요소 밀어내기 가능

    - a, img, span, strong

- Normal flow

    - 일반적인 흐름 또는 레이아웃을 변경하지 않는 경우 웹 페이지 요소가 배치되는 방식

- inline-block 타입

    - 인라인과 블럭의 특징을 모두 가진 특별한 display 속성값

- none 타입

    - 요소를 화면에 표시하지 않고, 공간 조차 부여되지 않음

- Class positiopn

    - static

        - 요소를 노말 플로우에 따라 배치

        - 방향 속성이 적용되지 않음

    - relative

        - 요소를 노말 플로우에 따라 배치

        - 자신의 원래 위치 기준으로 이동

        - 방향 속성 적용

        - 다른 요소의 레이아웃에 영향을 주지 않음

    - absolute

        - 요소를 노말 풀로우에서 제거

        - 가장 가까운 relative 부모 요소를 기준으로 이동

            - 만양 부모요소가 없다면 body 태그를 기준으로 함

        - 문서에서 요소가 차지하는 공간이 없어짐

    - fixed
        
        - 요소를 노말 플로우에서 제거

        - 현재 화면영역을 기준으로 이동

        - 스크롤해도 항상 같은 위치 유지

        - 문서에서 요소가 차지하는 공간이 없어짐

    - sticky

        - relative와 fixed의 특성을 결합한 속성

        - 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작

        - 스크롤 위치가 임계점에 도달하면 fixed처럼 화면에 고정

        - 다음 sticky 요소가 나오면 이전 sticky 요소의 자리를 대체

    - z-index

        - 요소의 쌓임 순서를 정의하는 속성

        - 정수 값을 사용해 z축 순서를 지정

        - 값이 클수로 요소가 위에 쌓이게 됨

        - static이 아닌 요소에만 적용됨

        - 기본값은 auto로 부모 요소의 z-index값에 영향을 받음

        - 같은 부모 내에서만 z-index값을 비교하고 값이 같으면 html 문서 순서대로 쌓임

## flexbox

- 요소를 행과 열 형태로 배치하는 레이아웃 방식

- flex container로 지정

    - display 속성을 flex로 설정하면 flex container로 지정됨

- flex direction

    - 기본값은 row

    - row: 가로 방향, 왼에서 오른쪽

    - col: 세로 방향, 위에서 아래

    - reverse 지정하면 시작과 끝이 바뀜


- flex-wrap

    - flex item 목록이 flex container의 한헹에 들어갖 않을경우 다른행에 배치할지 말지 여부 설정

    - 기본값은 nowrap

    - nowrap: 줄바꿈 하지 않음

    - wrap: 여러줄에 걸쳐 배치될수 있게 설정

- jusify-content

    - 주 축을 따라 flex item들을 정렬하고 간격을 조정

    - 기본값은 flex-start

    - flex-start, center, flex-end

    - space-between, space-around, space-evenly

- align-content

    - 컨테이너에 여러줄의 flex item이 있을 때 그 줄들의 사이의 공간을 어떻게 분배할지 지정

    - flex-wrap이 설정된 여러행에만 적용

    - 기본값은 stretch

    - stretch, flex-start, center, flex-end

- align-items

    - 컨테이너 안에 있는 flex item들의 교차 축 정렬 방법을 지정


- aligh-self

    - 컨테이너 안에 있는 flex item들을 교차 축을 따라 개별적으로 정렬

    - 기본값은 auto

- flex-grow

    - 남는 행 여백을 비율에 따라 각 flex-item에 분배

    - 각 비율을 지정해 늘어나는 만큼 추가 부여

- flex-basis

    - flex-item의 초깃값을 설정

    - width 와 basis 동시 적용할 경우 basis가 우선

- 마진 상쇄

    - 두 block 타입 요소의 martin top과 bottom이 만나 더 큰 margin으로 결함되는 현상


- 숏핸드

    - flex-flow

        - direction과 wrap을 한번에 지정할 수 있는 단축 속성

    - flex

        - grow, shrink, basis속성을 한번에 설정(기본값으로는 1, 1, 0%로 설정)


## bootstrap

- 이란 뭘까

    - 미리 만들어진 다양한 디자이 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

- CDN

    - 서버와 사용자 사이의 물리적인 거리를 줄여 컨텐츠 로딩에 소요되는 시간을 최소화

    - 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

- 기본 사용법

    - Bootstrap에는 특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있음

    - property: margin or padding 등

    - sides: 방향

    - size: spacing의 상대적 너비

    - t는 top/ b는 bottom/ s는 left/ e는 right/ x는 수평/ y는 수직/ blank는 4sides

    - rem은 최상위 요소의 글씨 크기를 기준으로 크기가 결정되는 상대 단위

- reset css

    - 모든 html 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 시트

- bg-color

    - primary 파랑

    - secondary 회색

    - success 초록

    - danger 빨강

    - subite는 연한색 보정

- Semantic web

    - 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

    - 외형 보다는 요소 자체의 의미에 집중하는 것

- html semantic element

    - 기본적인 모양과 기능 이외의 의미를 가지는 html 요소

    - header

        - 소개 및 탐색에 도움을 주는 컨텐츠

    - nav

        - 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획

    - main

        - 문서의 주요 컨텐츠

    - article

        - 독립적으로 구분해 배포하거나 재사용될 수 있는 구성의 컨텐츠 구획

    - section

        - 문서의 독립적인 구획

    - aside

        - 문서의 주요 내용과 간접적으로 연관된 부분

    - footer

        - 가장 가까운 조상구회의 작성자 저작권 정보, 관련 문서

- 의미론적 마크업이 필요한 이유

    - 검색엔진 최적화(SEO)

        - 검색 엔진이 해당 웹사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌

    - 웹 접근성

        - 웹 사이트, 도구, 기술이 고련자나 장애를 가진 사용자들이 사용할 수 있도록 설계및 개발하는것

## Grid system

- 웹 페이지의 레이아웃을 조정하는데 사용되는 12개의 컬럼으로 구성된 시스템

- 반응형 웹 디자인

    - 디바이스 종류나 화면 크기에 상관없이 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 기술

- Grid system 기본 요소

    - Container

        - column들을 담고 잇는 공간

    - column 

        - 실제 컨텐츠를 포함하는 부분

    - gutter

        - 컬럼과 컬럼 사이의 여백(상하좌우)

        - gx, gy, g등으로 여백 설정

        
        - x축은 padding, y축은 margin으로 여백 생성

        - x축의 간격은 실제로 변하지 ㅇ낳으면 padding으로 인해 컬럼 안에 contents의 너비가 변화

    
    - offset

        - 빈공간 할당
    
    - 1개의 row안에 12개의 컬럼 영역이 구성

- breakpoint

    - 웹 페이지를 다양한 화면 크기에 적절하게 배치하기 위한 분기점

    - 화면 너비에 따라 6개의 분기점 제공

    - xs, sm, md, lg, xl, xxl

    - 각 브레이크 포인트마다 설정된 최대 너비 값 이상으로 화면이 커지면 그리드 시스템 동작이 변경

- media query

    - 장치의 크기나 특징에 따라 적요오디는 스타일을 바꿀수 있는 css의 기능

- ux & ui

    - ux

        - 제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고 최적화하기 위한 디자인과 개발 분야

        - 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정

    - ui

        - 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야

- Grid cards

    - row-cols 클래스를 사용하여 행당 표시할 열 수를 손쉽게 제어할 수 있음
    