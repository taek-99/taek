# Vue

## Template Syntax
- Raw HTML
    - v-html을 사용하는 방식
    - 권장되진 않음

- Attribute Binding
    - v-bind를 사용
    - HTML의 id 속성 값을 vue의 동적속성과 동기화 되도록함

- JavaScript Expressions
    - Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
    - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음

## Directive
- v-접두사를 가진 특수속성

- 특징
    - 속성값은 단일 JavaScript 표현식이여햐함
    - 표현식 값이 변경될때 DOM에 반응적으로 업데이트를 적용

- 전체 구문
    - Name
    - Argument
    - Modifiers
    - Value

## v-bind
- 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
- HTML의 속성 값을 Vue의 상태 속성 값과 동기화
- ":" 약어로 쓰기도 함
- Dynamic attribute name
