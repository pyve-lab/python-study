"""
📌 텍스트 출력(print)
======================

print() 함수는 텍스트를 화면에 표시하거나 값을 출력할 때 사용합니다.

예:
    print("Hello World!")

print() 함수는 원하는 만큼 여러 번 사용할 수 있으며,
각 print() 호출은 기본적으로 새 줄에 출력됩니다.

예:
    print("Hello World!")
    print("I am learning Python.")
    print("It is awesome!")
"""
# 파이썬 print

print("Hello World!")
print("I am learning Python.")
print("It is awesome!")
# 결과 :
# Hello World!
# I am learning Python.
# It is awesome!

"""
📌따옴표 사용
------------
Python에서 텍스트(문자열)는 반드시 따옴표로 묶어야 합니다.
큰따옴표(" ")와 작은따옴표(' ')는 모두 사용할 수 있습니다.

예:
    print("This will work!")
    print('This will also work!')

만약 따옴표를 빼먹으면 Python은 오류를 발생시킵니다.

예 (잘못된 코드):
    print(This will cause an error)

결과:
    SyntaxError: invalid syntax.
"""
# 파이썬 따옴표

print("This will work!")
print('This will also work!')
# 결과 : 
# This will work!
# This will also work!

"""
📌줄바꿈 없이 출력하기
---------------------
기본적으로 print() 함수는 출력 후 자동으로 줄바꿈(newline)을 합니다.

같은 줄에서 여러 문장을 출력하고 싶다면 end 매개변수를 사용할 수 있습니다.

예:
    print("Hello World!", end=" ")
    print("I will print on the same line.")

여기서 end=" "는 가독성을 위해 뒤에 공백을 추가한 것입니다.
"""
# 파이썬 줄바꿈 없이 출력(end)

print("Hello World!", end=" ")
print("I will print on the same line.")
# 결과 : Hello World! I will print on the same line.