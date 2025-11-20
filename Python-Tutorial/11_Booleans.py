"""
📌 Boolean 값 (Boolean Values)
===========================

프로그래밍에서는 표현식이 True인지 False인지 판단하는 것이 매우 중요합니다.

Python은 모든 표현식을 평가하여
그 결과를 **True** 또는 **False** 로 반환합니다.


비교 연산의 결과는 항상 Boolean
--------------------------------
예:
    print(10 > 9)    # True
    print(10 == 9)   # False
    print(10 < 9)    # False
"""
# 파이썬 불린

print(10 > 9)    # True
print(10 == 9)   # False
print(10 < 9)    # False

"""
📌 f 조건문에서의 Boolean 사용
------------------------------
조건식의 결과가 True인지 False인지에 따라 다른 코드가 실행됩니다.

예:
    a = 200
    b = 33

    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")
"""
# 파이썬 불린 조건문

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# 결과 : b is not greater than a

"""
📌 값과 변수의 평가 (bool() 함수)
-------------------------------
bool() 함수를 사용하면 어떤 값이든 True 또는 False 로 평가됩니다.

예 — 문자열과 숫자 평가:
    print(bool("Hello"))   # True (비어 있지 않은 문자열)
    print(bool(15))        # True (0이 아닌 숫자)

예 — 두 변수 평가:
    x = "Hello"
    y = 15

    print(bool(x))   # True
    print(bool(y))   # True
"""
# 파이썬 불린 평가

x = "Hello"
y = 15
print(bool(x))   # True
print(bool(y))   # True

