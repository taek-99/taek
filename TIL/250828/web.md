# DAY 4

## Bootstrap Grid system

- 웹페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템

- 12개인 이유는 약수가 많고 적당한 숫자라서

- 반응형 웹 디자인

    - 디바이스 종류나 화면 크기에 상관없이 어디서든 일관된 레이아읏 제공

## Grid 구조

- container

    - column을 포함하는 부분

- column

    - 실제 컨텐츠를 포함하는 부분

- Gutter 

    - 컬럼과 컬럼 사이의 여백 영역

- 1개의 로우 안에 12개의 컬럼 영역이 구성

    - 각 요소는 12개중 몇개를 차지할 것인지 지정됨

    - 가장 위 부모에 컨테이너, 그 안에 로우, 그 안에 컬럼

    -   총 12를 벗어나면 밑으로 줄바뀜

- offset

    - 상쇄시킴(jump)

- Gutters

    - 시스템에서 컬럼 사이에 여백

    - x축은 padding, y축은 margin으로 여백 생성

- Responsive web design

    - 12개의 컬럼과 6개의 브레이크포인트를 사용하여 웹 디자인을 구현

    -  6개의 분기점 제공(xs, sm, md, lg, xl, xxl)

    - col-size-칸수


- css layout

    - position, flex, grid system

    - 상호보완적으로 다 사용해야함


