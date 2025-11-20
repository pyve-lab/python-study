"""
📌 문자열 (Strings)
====================

기본 문자열
--------------
Python에서 문자열은 작은따옴표(' ') 또는 큰따옴표(" ")로 묶어서 표현합니다.
두 방식은 동일하게 취급됩니다.

예:
    print("Hello")
    print('Hello')


문자열 안의 따옴표
--------------------
문자열을 둘러싸고 있는 따옴표와 다른 종류의 따옴표는
문자열 내부에 자유롭게 사용할 수 있습니다.

예:
    print("It's alright")
    print("He is called 'Johnny'")
    print('He is called "Johnny"')
"""
# 파이썬 문자열

print("It's alright")
print('He is called "Johnny"')
# 결과 :
# It's alright
# He is called "Johnny"

"""
📌 변수에 문자열 할당
---------------------
문자열을 변수에 저장하려면 변수 이름 뒤에 `=` 를 사용합니다.

예:
    a = "Hello"
    print(a)
"""
# 파이썬 문자열 변수

a = "Hello"
print(a)
# 결과 : Hello

"""
📌 다중 줄 문자열 (Multiline String)
----------------------------------
세 개의 큰따옴표(\"\"\" ) 또는 작은따옴표(\'\'\')를 사용하여
여러 줄에 걸친 문자열을 만들 수 있습니다.

예 — 큰따옴표 3개:
    a = """"""Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
"""
print(a)
"""
"""
예 — 작은따옴표 3개:
    a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''
    print(a)

참고:
    다중 줄 문자열에서는 줄바꿈이 작성된 그대로 포함됩니다.
"""
# 파이썬 다중 줄 문자열

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# 결과 :
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

