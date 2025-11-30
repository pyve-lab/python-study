"""
📌 Python match-case 문
=======================

Python 3.10부터 도입된 **match-case 문**은  
여러 조건을 처리할 때 if-elif-else 보다 더 간결하고 읽기 쉬운 구조를 제공합니다.

match-case 구조는 다른 언어의 switch-case와 비슷하지만,  
파이썬에서는 훨씬 더 강력하고 다양한 패턴 매칭 기능을 제공합니다.
"""

"""
📌 기본 문법
------------

match expression:
    case value1:
        # code block
    case value2:
        # code block
    case _:
        # default block

동작 방식:
1. `expression`이 한 번 평가됨
2. 그 값이 각 case의 값(또는 패턴)과 비교됨
3. 가장 먼저 일치하는 case의 코드 블록 실행
4. 일치하는 것이 없으면 `_`(기본 case) 실행
"""
# 파이썬 match-case 기본 문법

day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
# 결과 : Wednesday

"""
📌 기본 예시 — 요일 출력
-------------------------

예:
    day = 4
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
"""
# 파이썬 match-case 요일 출력

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
# 결과 : Thursday

"""
📌 기본값(Default Case) : `_`
----------------------------
`_` 는 모든 값과 일치하는 “와일드카드” 패턴이다.  
항상 **마지막 case**에 두어야 기본 case처럼 동작한다.

예:
    match day:
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Looking forward to the Weekend")
"""
# 파이썬 match-case 기본값

day = 5
match day:
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Looking forward to the Weekend")
# 결과 : Looking forward to the Weekend

"""
📌 여러 값 결합 (| 연산자)
--------------------------

`|` 기호는 OR 역할을 한다.  
여러 값을 하나의 case에서 처리할 때 사용.

예:
    match day:
        case 1 | 2 | 3 | 4 | 5:
            print("Weekday")
        case 6 | 7:
            print("Weekend")
"""
# 파이썬 match-case 여러 값 결합

day = 2
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
# 결과 : Weekday

"""
📌 Guard 조건(조건부 case) — case 뒤에 if 추가
----------------------------------------------

case 패턴에 **추가적인 조건**을 검사하고 싶을 때 사용한다.

예:
    month = 5
    day = 4

    match day:
        case 1 | 2 | 3 | 4 | 5 if month == 4:
            print("A weekday in April")
        case 1 | 2 | 3 | 4 | 5 if month == 5:
            print("A weekday in May")
        case _:
            print("No match")
"""
# 파이썬 match-case Guard 조건

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
# 결과 : A weekday in May

"""
📌 match-case 요약
------------------

- match-case는 여러 조건을 처리할 때 if-elif보다 더 깔끔함
- `_`는 기본값처럼 사용 (항상 마지막)
- `|` 로 여러 값을 하나의 case에서 처리 가능
- case 문의 조건부 검사 → `case 값 if 조건:`
- Python 3.10 이상에서 사용 가능

"""
