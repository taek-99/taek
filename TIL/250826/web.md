# css 박스모델

## display 속성

- 박스 타입
    
    - 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

    - block 타입

         - block 타입은 책의 각 문단과 같습니다.

         - 모든 문단은 항상 새로운 줄에서 시작하며, 그 자체로 하나의 독립된 덩어리를 이룹니다. 다른 문단이 끼어둘수 없음

         - 항상 새로운 행으로 나뉨 (너비100%)

         - weight, height, margin, padding 적용 가능

         - 다른 요소를 상자로부터 밀어냄

         - 너비를 지정하지 않을 경우 inline방향으로 사용 가능한 공간을 다 차지함

         - h1~6, p, div, ul, li

    - inline 타입

        - 문장속 단어를 형광펜으로 칠하는것과 같다

        - 줄을 바꾸지 않고, 텍스트의 일부에만 다른 스타일을 적용할때 사용됩니다.

        - 줄바꿈이 일어나지 않음(콘텐츠의 크기만큼만 영역을 차지)

        - weight와 height 속성 사용할수 없음

        - 수평 방향만 다른 요소를 밀어낼 수 있음

        - a, img, span, strong

    - Nomal flow

        - 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹페이지 요소가 배치되는 방식

## 기타 속성

- inline-block 속성

    - inline과 block의 특징을 모두 가진 특별한 display 속성 값

    - 줄바꿈 없이 크기 지정 가능

    - 너비와 높이 조정 가능

    - 다른 ㅇㅛ소가 밀려남

- none 타입

    - 요소를 화면에 표시하지 않고, 공간 차지함


## css 포지션

- css layout

    - 각 요소의 위치와 크기르 ㄹ조정하여 웹페이지의 디자인을 결정하는 것

    - 각 요소들을 상하 좌우ㅗㄹ 정력

- css postion

    - 요소를 nomal flow에서 제거하여 다른 위치로 배치

- position 이동 방향

    - 네가지 방향으로 요소의 위치를 조절할 수 있음

    - 겹치는 요소의 쌓이는 순서 조절 가능(z축)

- position 유형

    - static 
        
        - 요소를 normal flow에 따라 배치

        - 4방향 속서잉 적용 되지 않음

    - relative

        - 요소를 normal flow에 따라 배치

        - 자신의 원래 위치를 기준으로 이동


    - absolute

        - 요소를 nomal flow에서 제거

        - 가장 가까운 relative 부모요소를 기준으로 이동

        - 문서에서 요소가 차지하는 공간이 없어짐
    
    - fixed

        - 요소를 nomal flow에서 제거

        - 현재 화면영역을 기준으로 이동

        - 스크롤해도 항상 같은 위치에 유지됨

    - sticky

        - relative와 fixed 특징을 결합한 속성

        - 스크롤 위치가 임계점에 도달하면 화면에 고정

    - z-index

        - 요소의 쌓임 순서를 정의하는 순서

        - 기본값은 auto로 부모 요소의 z-index값에 영향을 받음

        - z-index값이 같으면 html문서 순서대로 쌓임


## css Flexbox

- inner display 타입

    - 박스 내부의 요소들이 어떻게 배치될지를 결정

- 공간배열, 정렬

- 구성요소

    - main axis

    - cross axis

    - flex container

    - flex item

- flexbox 속성

    - flex container

        - display, flex-direction

    - flex item

        - 기타 등등

    - flex-diretion

        - flex-item이 나열되는 방향을 지정

    - flex-wrap

        - 행안에 들어가지 않을 경우 다른 행에 배치