## 변수
- let: 재할당 가능, 재선언 불가능
- const: 재할당 불가능, 재선언 불가능
- var: 재선언, 재할당 가능, 호이스팅 문제로 사용 x

## DOM
- 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
- querySelector()
    - 요소 한개 선택
    - 제공한 선택자를 만족하는 첫번째 객체 반환(없으면 null 반환)

- querySelectorAll()
    - 요소 여러개 선택
    - 제공한 선택자와 일치하는 여러 객체 선택

## 속성 조작
- classList 요소의 클래스 목록을 유사배열 형태로 반환
- classList 메서드
    - add, renmove, toggle

- 일반속성 조작 메서드
    - getAttribute, setAttribute, removeAttribute

## HTML 콘텐츠 조작
- textContent
    - 요소의 택스트 컨텐츠를 표현

## DOM 요소 조작
- document.createElement()
    - 작성한 tagName의 HTML 요소를 생성하여 반환

- Node.appendChild()
    - 한 노드의 특정 부모 노드의 자식 노드리스트 중 마지막 자식으로 삽입
    - 추가된 노드 객체를 반환

- Node.removeChild()
    - DOM에서 자식 Node를 제거

## style조작
- style.color, style.fontsize, style.border

## 호이스팅
- 변수 선언문이 코드의 최상단으로 끌어올려지는 현상

## 문제
1. a
2. c
3. c, const
4. d, Dom
5. d
6. d - c
7. c
8. d
9. b
10. b
11. c
12. c

## 데이터 타입
- 원시 자료형
    - Number, String, Boolean, null, undefined
- 참조 자료형
    - objects

## 반복문
- for ... in
    - 객체의 열거 가능한 속성의 키값에 대한 반복

- for ... of
    - 반복 가능한 객체의 값에 대한 반복

## 함수
- 함수 선언식
    - 호이스팅 됨
    - 코드의 구조와 가독성 면에서는 표현식에 비해 장점이 있음

- 함수 표현식
    - 호이스팅 x
    - 변수 선언만 호이스팅 되고 함수 할당은 실행할때 됨
    - 함수 이름이 없는 익명 함수 사용 가능

    - 권장 이유
        - 예측 가능성
        - 유연성
        - 스코프 관리

## 매개변수
- 기본 매개변수
    - 기본값 지정 가능함
- 나머지 매개변수
    - 정해지지 않은 인자들을 배열로 모아서 받는 방법
    (1, 2, ...~~)

- 누락된 인자는 undefiend로 표시됨

## Spread syntax
- 전개 구문
- 배열이나 문자열처럼 반복 가능한 항목들을 개별 요소로 펼치는것

## 화살표 함수 표현식
- functions 키워드 제거 후 매개변수와 중괄호 사이에 화살표 작성
- 매개변수가 하나만 있으면 () 제거 가능

## 문제
1. c Array
2. c
3. b
4. b
5. a
6. c
7. d
8. c
9. c
10. b
