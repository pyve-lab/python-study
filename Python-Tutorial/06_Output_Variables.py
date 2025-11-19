"""
📌 출력 변수 (Printing Variables)
=================================

print() 함수는 변수를 출력할 때 자주 사용됩니다.

예:
    x = "Python is awesome"
    print(x)
"""

"""
📌 여러 변수 출력 (쉼표 사용)
---------------------------
print() 함수에서 쉼표(,)를 사용하면 여러 변수를 한 번에 출력할 수 있습니다.

예:
    x = "Python"
    y = "is"
    z = "awesome"
    print(x, y, z)
"""
# 파이썬 여러 변수 출력(,)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# 결과 : Python is awesome

"""
📌 여러 변수 출력 (+ 연산자 사용)
-------------------------------
문자열을 + 연산자로 연결(concatenate)할 수도 있습니다.

예:
    x = "Python "
    y = "is "
    z = "awesome"
    print(x + y + z)

주의:
    문자열 뒤에 공백이 없으면 출력이 붙어서 나옵니다.
    예: "Python" + "is" + "awesome" → "Pythonisawesome"
"""
# 파이썬 여러 변수 출력(+)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# 결과 : Python is awesome

"""
📌 숫자에서의 + 연산자
---------------------
숫자끼리는 + 연산자가 수학적 덧셈으로 작동합니다.

예:
    x = 5
    y = 10
    print(x + y)   # 결과: 15
"""
# 파이썬 숫자에서의 +

x = 5
y = 10
print(x + y)
# 결과 : 15

"""
📌 문자열 + 숫자 → 오류 발생
---------------------------
문자열(str)과 숫자(int)를 + 연산자로 결합하려 하면 오류가 발생합니다.

예:
    x = 5
    y = "John"
    print(x + y)   # TypeError 발생
"""
# 파이썬 문자열 + 숫자

x = 5
y = "John"
print(x + y)
# 결과 : TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""
📌 가장 좋은 방법: 쉼표로 출력
----------------------------
여러 타입(숫자, 문자열 등)을 함께 출력하려면
print() 함수에서 쉼표로 구분하는 것이 가장 안전하고 권장됩니다.

예:
    x = 5
    y = "John"
    print(x, y)    # 정상 출력
"""