"""
📌 Python 조건문(If Statements)
==============================

Python은 기본적인 논리 조건을 지원합니다:

- 같음: a == b
- 같지 않음: a != b
- 보다 작음: a < b
- 이하: a <= b
- 보다 큼: a > b
- 이상: a >= b

이 조건들은 if 문, while 문, for 문 등에서 사용됩니다.
"""

"""
📌 기본 if 문
--------------
조건이 True일 때 코드 블록이 실행됩니다.

예:
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")
"""
# 파이썬 기본 if 문

a = 33
b = 200
if b > a:
    print("b is greater than a")
# 결과 : b is greater than a

"""
📌 if 문이 실행되는 방식
-----------------------
- 조건식 → True 또는 False 반환
- True → 내부 코드 실행
- False → 건너뜀

예:
    number = 15
    if number > 0:
        print("The number is positive")
"""
# 파이썬 if 문 실행 방식

number = 15
if number > 0:
    print("The number is positive")
# 결과 : The number is positive

"""
📌 들여쓰기(Indentation)
-----------------------
Python은 들여쓰기(공백/탭)를 사용하여 코드 범위를 구분합니다.
같은 블록에서는 **동일한 들여쓰기**를 유지해야 함.

잘못된 예 (Error):
    if b > a:
    print("...")

올바른 예:
    if b > a:
        print("...")
"""
# 파이썬 들여쓰기 예시

if b > a:
    print("b is greater than a")  # 올바른 들여쓰기
# 결과 : b is greater than a

"""
📌 if 블록 내부에 여러 문장 가능
--------------------------------
예:
    if age >= 18:
        print("You are an adult")
        print("You can vote")
"""
# 파이썬 if 블록 내부 여러 문장

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
# 결과 : 
# You are an adult
# You can vote

"""
📌 Boolean 값 사용
------------------
변수를 직접 조건으로 사용할 수 있음.

- False로 평가: 0, "", None, 빈 리스트/집합/튜플/딕셔너리
- True로 평가: 그 외 모든 값

예:
    is_logged_in = True
    if is_logged_in:
        print("Welcome back!")
"""
# 파이썬 Boolean 값 사용

is_logged_in = True
if is_logged_in:
    print("Welcome back!")
# 결과 : Welcome back!

"""
===================================
📌 elif : 여러 조건 검사
===================================

elif = "이전 조건이 아니면 이 조건을 검사"

예:
    if b > a:
        print("b > a")
    elif a == b:
        print("a and b are equal")

여러 개의 elif 사용 가능:

예:
    score = 75
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")

Python은 **위에서 아래로 순서대로 검사하며**,  
첫 번째로 참(True)인 조건을 찾으면 나머지는 무시합니다.
"""
# 파이썬 elif 문

score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
# 결과 : C

"""
===================================
📌 else : 나머지 모든 경우
===================================

조건 모두가 False일 경우 실행됨.

예:
    if b > a:
        print("b > a")
    elif a == b:
        print("a == b")
    else:
        print("a > b")

else는 마지막에만 사용 가능.
"""
# 파이썬 else 문

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# 결과 : a is greater than b

"""
===================================
📌 단축형(if / if-else 한 줄)
===================================

1) 한 줄 if
    if a > b: print("a > b")

2) 한 줄 if-else (삼항 연산자)
    print("A") if a > b else print("B")

3) 변수에 값 할당
    max_value = a if a > b else b

4) 여러 조건 연결
    print("A") if a > b else print("=") if a == b else print("B")
"""
# 파이썬 단축형 if / if-else

a = 5
b = 10

# 1) 한 줄 if
if a > b: print("a > b")
# 결과 : (출력 없음)

# 2) 한 줄 if-else (삼항 연산자)
print("A") if a > b else print("B")
# 결과 : B

# 3) 변수에 값 할당
max_value = a if a > b else b
print("Max value is", max_value)
# 결과 :
# B
# Max value is 10

# 4) 여러 조건 연결
print("A") if a > b else print("=") if a == b else print("B")
# 결과 : B

"""
===================================
📌 논리 연산자 (and / or / not)
===================================

✔ and : 둘 다 True → True  
✔ or  : 하나라도 True → True  
✔ not : True ↔ False 반전

예:
    if a > b and c > a:
        print("Both conditions are True")

    if a > b or a > c:
        print("At least one is True")

    if not a > b:
        print("a is NOT greater than b")
"""
# 파이썬 논리 연산자

a = 5
b = 10
c = 15
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one is True")
if not a > b:
    print("a is NOT greater than b")
# 결과 : a is NOT greater than b

"""
📌 연산자 우선순위
------------------
1) not
2) and
3) or

예:
    if (age < 18 or age > 65) and not is_student:
        ...
"""
# 파이썬 연산자 우선순위

age = 70
is_student = False
if (age < 18 or age > 65) and not is_student:
    print("Eligible for discount")
# 결과 : Eligible for discount

"""
📌 논리 연산자 진리표
----------------------

AND
조건1 | 조건2 | 결과
True  | True  | True
True  | False | False
False | True  | False
False | False | False

OR
조건1 | 조건2 | 결과
True  | True  | True
True  | False | True
False | True  | True
False | False | False
"""

"""
===================================
📌 중첩 If 문 (Nested If)
===================================

if 문 안에 또 다른 if 문 포함 가능.

예:
    x = 41
    if x > 10:
        print("Above ten,")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

중첩이 깊어질수록 조건 흐름이 복잡해짐.
"""
# 파이썬 중첩 If 문

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# 결과 :
# Above ten,
# and also above 20!

"""
📌 중첩 vs 논리 연산자
----------------------
둘 다 같은 결과지만 상황에 따라 선택.

중첩:
    if temp > 20:
        if is_sunny:
            print("Nice day!")

논리 연산자:
    if temp > 20 and is_sunny:
        print("Nice day!")
"""
# 파이썬 중첩 vs 논리 연산자

temp = 25
is_sunny = True

# 중첩
if temp > 20:
    if is_sunny:
        print("Nice day!")
# 결과 : Nice day!

# 논리 연산자
if temp > 20 and is_sunny:
    print("Nice day!")
# 결과 : Nice day!

"""
===================================
📌 pass 문
===================================

if문은 빈 상태일 수 없음 → pass 사용하여 오류 방지

예:
    if b > a:
        pass

pass = 아무 동작을 하지 않는 "빈 명령문"  
플레이스홀더로 사용됨.


언제 pass를 사용하는가?
------------------------
- 함수/클래스의 뼈대만 만들어두고 싶을 때
- 아직 구현하지 않은 조건문 자리 잡기용
- 구문적으로 문장이 필요하지만 실제 동작은 필요 없을 때

예:
    if score > 90:
        pass  # later implement

함수에서 pass:
    def calculate():
        pass
"""
# 파이썬 pass 문

if b > a:
    pass  # 나중에 구현 예정
# 결과 : (출력 없음)
def calculate():
    pass  # 함수 구현 예정
# 결과 : (출력 없음)

"""
===================================
📌 전체 정리
===================================

- if : 조건이 True일 때 실행
- elif : 여러 조건 중 하나 선택
- else : 모든 조건이 False일 때 실행
- 논리 연산자(and, or, not)로 조건 결합 가능
- 중첩 if로 계층적인 조건 구성 가능
- pass 문으로 빈 블록 허용
- 삼항 연산자(if-else 한 줄)로 짧은 조건 표현 가능
"""
