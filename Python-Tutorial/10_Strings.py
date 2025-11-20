"""
📌 문자열 (Strings)
===================

기본 문자열
--------------
Python에서 문자열은 작은따옴표(' ') 또는 큰따옴표(" ")로 감쌉니다.
'hello' 와 "hello" 는 동일합니다.

예:
    print("Hello")
    print('Hello')
"""

"""
📌 문자열 안의 따옴표
--------------------
문자열을 둘러싼 따옴표와 다른 종류의 따옴표는 문자열 내부에 그대로 쓸 수 있습니다.

예:
    print("It's alright")
    print("He is called 'Johnny'")
    print('He is called "Johnny"')
"""

"""
📌 변수에 문자열 저장
---------------------
문자열을 변수에 넣으려면 = 뒤에 문자열을 작성하면 됩니다.

예:
    a = "Hello"
    print(a)
"""

"""
📌 다중 줄 문자열 (Multiline String)
-----------------------------------
세 개의 따옴표를 사용하여 여러 줄의 문자열을 만들 수 있습니다.

예 — 큰따옴표 3개:
    a = \"\"\"Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.\"\"\"
    print(a)

예 — 작은따옴표 3개:
    a = \'\'\'Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.\'\'\'
    print(a)

참고:
    여러 줄 문자열은 작성된 줄바꿈과 공백이 그대로 유지됩니다.
"""

"""
📌 문자열은 배열입니다 (Strings are Arrays)
===========================================

Python의 문자열은 유니코드 문자들로 이루어진 배열(시퀀스)입니다.
단, Python에는 문자(char) 타입이 없으며, 길이가 1인 문자열이 '문자'처럼 취급됩니다.

문자 접근
-----------
문자열의 각 문자는 인덱스 번호로 접근할 수 있습니다.
(첫 번째 문자는 위치 0)

예:
    a = "Hello, World!"
    print(a[1])   # 'e'
"""
# 파이썬 문자열 문자 접근

a = "Hello, World!"
print(a[1])
# 결과 : e

"""
📌 문자열 반복(루프)
------------------
문자열은 배열이므로 for 루프를 사용해 문자열의 문자를 하나씩 반복할 수 있습니다.

예:
    for x in "banana":
        print(x)
"""
# 파이썬 문자열 반복

for x in "banana":
    print(x)
# 결과 :
# b
# a
# n
# a
# n
# a

"""
📌문자열 길이 확인 (len 함수)
------------------------------
문자열의 길이를 확인하려면 len() 함수를 사용합니다.

예:
    a = "Hello, World!"
    print(len(a))   # 13
"""
# 파이썬 문자열 길이

a = "Hello, World!"
print(len(a))
# 결과 : 13

"""
📌 문자열에 특정 단어/문자 포함 여부 확인 (in 키워드)
---------------------------------------------------
문자열에 특정 문자열이 포함되어 있는지 확인할 수 있습니다.

예:
    txt = "The best things in life are free!"
    print("free" in txt)   # True

if 문에서 사용하기:
    txt = "The best things in life are free!"
    if "free" in txt:
        print("Yes, 'free' is present.")
"""
# 파이썬 문자열 포함 여부 확인

txt = "The best things in life are free!"
print("free" in txt)   
# 결과 :
# True


"""
📌 문자열에 특정 단어가 없는지 확인 (not in 키워드)
-------------------------------------------------
예:
    txt = "The best things in life are free!"
    print("expensive" not in txt)   # True

if 문에서 사용하기:
    txt = "The best things in life are free!"
    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")
"""
# 파이썬 문자열 미포함 여부 확인

txt = "The best things in life are free!"
print("expensive" not in txt)
# 결과 :
# True

"""
📌 문자열 슬라이싱 (String Slicing)
====================================

슬라이싱은 문자열의 일부(부분 문자열)를 가져오는 방법입니다.
문자열은 배열처럼 인덱스로 접근할 수 있으며,
슬라이싱은 [start:end] 형식으로 지정합니다.
end 인덱스는 포함되지 않는다는 점이 중요합니다.


기본 슬라이싱
----------------
예 — 인덱스 2부터 5까지(5는 포함되지 않음):
    b = "Hello, World!"
    print(b[2:5])   # 'llo'

참고:
    첫 번째 문자의 인덱스는 0입니다.
"""
# 파이썬 문자열 슬라이싱

b = "Hello, World!"
print(b[2:5])
# 결과 : llo

"""
📌 시작 인덱스 생략
-------------------
start 생략 → 문자열의 처음부터 시작

예:
    b = "Hello, World!"
    print(b[:5])    # 'Hello'
"""
# 파이썬 문자열 시작 인덱스 생략

b = "Hello, World!"
print(b[:5])
# 결과 : Hello

"""
📌 끝 인덱스 생략
----------------
end 생략 → 문자열 끝까지 반환

예:
    b = "Hello, World!"
    print(b[2:])    # 'llo, World!'
"""
# 파이썬 문자열 끝 인덱스 생략

b = "Hello, World!"
print(b[2:])
# 결과 : llo, World!

"""
📌 음수 인덱싱
--------------
음수 인덱스를 사용하면 문자열의 끝에서부터 계산합니다.
-1 → 마지막 문자  
-2 → 뒤에서 두 번째 문자, …

예 — "World!" 에서 부분 문자열 가져오기:
    b = "Hello, World!"
    print(b[-5:-2])   # 'orl'

설명:
    -5 → 'o'
    -2 → 'd' (end는 포함되지 않으므로 'r', 'l', 'd' 중 'd' 바로 전까지)
"""
# 파이썬 문자열 음수 인덱싱

b = "Hello, World!"
print(b[-5:-2])
# 결과 : orl

"""
📌 문자열 메서드 (String Methods)
=================================

대문자 변환 — upper()
-----------------------
upper() 메서드는 문자열의 모든 문자를 대문자로 변환합니다.

예:
    a = "Hello, World!"
    print(a.upper())   # 'HELLO, WORLD!'
"""
# 파이썬 문자열 대문자 변환

a = "Hello, World!"
print(a.upper())
# 결과 : HELLO, WORLD!

"""
📌 소문자 변환 — lower()
-----------------------
lower() 메서드는 문자열의 모든 문자를 소문자로 변환합니다.

예:
    a = "Hello, World!"
    print(a.lower())   # 'hello, world!'
"""
# 파이썬 문자열 소문자 변환

a = "Hello, World!"
print(a.lower())
# 결과 : hello, world!

"""
📌 공백 제거 — strip()
---------------------
strip() 메서드는 문자열의 앞뒤 공백(whitespace)을 제거합니다.

예:
    a = " Hello, World! "
    print(a.strip())   # 'Hello, World!'
"""
# 파이썬 문자열 공백 제거

a = " Hello, World! "
print(a.strip())
# 결과 : Hello, World!

"""
📌 문자열 치환 — replace()
-------------------------
replace(old, new) 메서드는 문자열의 일부를 다른 문자열로 대체합니다.

예:
    a = "Hello, World!"
    print(a.replace("H", "J"))   # 'Jello, World!'
"""
# 파이썬 문자열 치환

a = "Hello, World!"
print(a.replace("H", "J"))
# 결과 : Jello, World!

"""
📌 문자열 분할 — split()
------------------------
split(sep) 메서드는 문자열을 지정된 구분자(sep)를 기준으로 분리해
리스트(list) 형태로 반환합니다.

예:
    a = "Hello, World!"
    print(a.split(","))   # ['Hello', ' World!']


참고:
    문자열 관련 더 많은 메서드는 Python 공식 문자열 메서드 문서에서 확인할 수 있습니다.
"""
# 파이썬 문자열 분할

a = "Hello, World!"
print(a.split(","))
# 결과 : ['Hello', ' World!']

"""
📌 문자열 연결 (String Concatenation)
=====================================

문자열 두 개를 연결하려면 + 연산자를 사용합니다.

예 — 두 문자열 연결:
    a = "Hello"
    b = "World"
    c = a + b
    print(c)   # HelloWorld
"""
# 파이썬 문자열 연결

a = "Hello"
b = "World"
c = a + b
print(c)
# 결과 : HelloWorld

"""
📌 공백을 포함하여 문자열 연결
------------------------------
문자열을 자연스럽게 연결하기 위해 공백(" ")을 사이에 넣을 수 있습니다.

예:
    a = "Hello"
    b = "World"
    c = a + " " + b
    print(c)   # Hello World
"""
# 파이썬 문자열 공백 포함 연결

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# 결과 : Hello World

"""
📌 문자열 형식 (String Formatting)
==================================

문자열과 숫자 결합 문제
-------------------------
문자열과 숫자를 + 연산자로 직접 연결하면 오류가 발생합니다.

예 (오류 발생):
    age = 36
    txt = "My name is John, I am " + age
    print(txt)
    # TypeError 발생
"""
# 파이썬 문자열과 숫자 결합 오류

age = 36
txt = "My name is John, I am " + age
print(txt)
# 결과 : TypeError: can only concatenate str (not "int") to str

"""
📌 문자열과 숫자를 결합하는 올바른 방법
---------------------------------------
Python에서는 문자열을 형식화할 때
- f-string (권장)
- format() 메서드  
를 사용할 수 있습니다.

F-문자열 (f-strings)
------------------------
Python 3.6부터 도입되었으며,
현재 가장 많이 사용하는 문자열 포맷 방식입니다.

문법:
    f"문자열 {값 또는 표현식}"

예:
    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)
"""
# 파이썬 f-문자열

age = 36
txt = f"My name is John, I am {age}"
print(txt)
# 결과 : My name is John, I am 36

"""
📌 플레이스홀더에 변수 넣기
-------------------------
예:
    price = 59
    txt = f"The price is {price} dollars"
    print(txt)
"""
# 파이썬 f-문자열 플레이스홀더

price = 59
txt = f"The price is {price} dollars"
print(txt)
# 결과 : The price is 59 dollars

"""
📌 플레이스홀더에 형식 지정자 사용하기
------------------------------------
형식 지정자는 콜론(:) 뒤에 작성합니다.

예 — 소수점 둘째 자리까지 표시:
    price = 59
    txt = f"The price is {price:.2f} dollars"
    print(txt)
    # 출력: The price is 59.00 dollars
"""
# 파이썬 f-문자열 형식 지정자

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# 결과 : The price is 59.00 dollars

"""
📌 플레이스홀더 안에서 수학 연산 수행
------------------------------------
예:
    txt = f"The price is {20 * 59} dollars"
    print(txt)
    # 출력: The price is 1180 dollars
"""
# 파이썬 f-문자열 수학 연산

txt = f"The price is {20 * 59} dollars"
print(txt)
# 결과 : The price is 1180 dollars

"""
📌 이스케이프 문자 (Escape Characters)
=====================================

문자열 내에 원래는 사용할 수 없는 문자를 넣고 싶을 때
**이스케이프 문자(Escape Character)** 를 사용합니다.

이스케이프 문자는 역슬래시(\\) + 특수문자로 구성됩니다.

예 — 큰따옴표 문제
---------------------
큰따옴표로 감싼 문자열 안에 큰따옴표를 그대로 넣으면 오류가 발생합니다.

오류 예:
    txt = "We are the so-called "Vikings" from the north."   # SyntaxError

해결: 이스케이프 문자 \\" 사용
예:
    txt = "We are the so-called \\\"Vikings\\\" from the north."
    print(txt)
"""
# 파이썬 이스케이프 문자

txt = "We are the so-called \\\"Vikings\\\" from the north."
print(txt)
# 결과 : We are the so-called "Vikings" from the north.

"""
📌 Python에서 사용 가능한 주요 이스케이프 문자
------------------------------------------------

    Code        설명
    --------------------------------
    \\'         작은따옴표(Single Quote)
    \\\\        역슬래시(Backslash)
    \\n         줄바꿈(New Line)
    \\r         캐리지 리턴(Carriage Return)
    \\t         탭(Tab)
    \\b         백스페이스(Backspace)
    \\f         폼 피드(Form Feed)
    \\ooo       8진수(Octal) 값
    \\xhh       16진수(Hex) 값

"""

"""
📌 문자열 메서드 (String Methods)
=================================

Python에는 문자열에 사용할 수 있는 다양한 내장 메서드가 있습니다.

참고:
------
모든 문자열 메서드는 **새로운 문자열을 반환하며**,  
원본 문자열은 변경되지 않습니다. (문자열은 불변 객체)

아래는 주요 문자열 메서드와 그 기능 요약입니다:


📌 문자열 메서드 목록
----------------------

capitalize()     → 첫 문자를 대문자로 변환
casefold()       → 문자열을 소문자로 변환(강력한 lower)
center()         → 문자열을 가운데 정렬하여 반환
count()          → 특정 값이 문자열에 등장한 횟수를 반환
encode()         → 문자열의 인코딩된 버전 반환
endswith()       → 특정 문자열로 끝나는지 여부 반환
expandtabs()     → 탭(tab)의 크기를 설정
find()           → 특정 값을 검색하여 첫 위치 반환 (없으면 -1)
format()         → 문자열을 포맷팅
format_map()     → 딕셔너리를 사용해 문자열을 포맷팅
index()          → 특정 값을 검색하여 첫 위치 반환 (없으면 오류)

isalnum()        → 영문자/숫자로만 이루어졌는지 확인
isalpha()        → 알파벳 문자만 포함하는지 확인
isascii()        → ASCII 문자로만 구성되었는지 확인
isdecimal()      → 10진 숫자로만 구성되었는지 확인
isdigit()        → 숫자로만 구성되었는지 확인
isidentifier()   → 유효한 파이썬 식별자인지 확인
islower()        → 모두 소문자인지 확인
isnumeric()      → 숫자값(유니코드 숫자 포함)인지 확인
isprintable()    → 출력 가능한 문자로만 구성되어 있는지
isspace()        → 공백 문자로만 이루어졌는지 확인
istitle()        → 제목 형식(각 단어 첫 글자 대문자)인지
isupper()        → 모두 대문자인지 확인

join()           → 반복 가능한(iterable) 요소들을 문자열로 결합
ljust()          → 왼쪽 정렬
lower()          → 소문자로 변환
lstrip()         → 왼쪽 공백 제거
maketrans()      → translate()에 사용할 변환 테이블 생성
partition()      → 문자열을 3부분으로 분리하여 튜플 반환

replace()        → 특정 문자열을 새 문자열로 대체
rfind()          → 특정 값을 뒤에서부터 찾아 위치 반환
rindex()         → 특정 값을 뒤에서부터 찾아 위치 반환(없으면 오류)
rjust()          → 오른쪽 정렬
rpartition()     → 문자열을 오른쪽에서부터 3부분으로 분리
rsplit()         → 구분자로 분리하여 리스트로 반환
rstrip()         → 오른쪽 공백 제거

split()          → 문자열을 구분자로 분리하여 리스트 반환
splitlines()     → 줄바꿈 기준으로 분리하여 리스트 반환
startswith()     → 특정 값으로 시작하는지 확인
strip()          → 양쪽 공백 제거
swapcase()       → 대↔소문자 변환
title()          → 각 단어의 첫 글자를 대문자로 변환
translate()      → 변환 테이블을 사용해 치환
upper()          → 대문자로 변환
zfill()          → 앞쪽을 0으로 채워 길이 맞추기

"""
