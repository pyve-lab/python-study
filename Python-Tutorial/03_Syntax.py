"""
📌 Python 구문 실행
===================

파이썬 구문은 다음 두 가지 방식으로 실행할 수 있습니다.

1) 명령줄에서 직접 실행
------------------------
Python 인터프리터에 직접 구문을 입력하여 즉시 실행할 수 있습니다.

    >>> print("Hello, World!")
    Hello, World!

2) .py 파일을 만들어 실행
---------------------------
.py 확장자의 Python 파일을 생성한 뒤,
명령줄에서 해당 파일을 직접 실행할 수도 있습니다.

    C:\\Users\\Your Name> python myfile.py
"""
# 터미널에서 print문 실행

# PS C:\Users\권나현\Desktop\python-study\Python-Tutorial> print("Hello, World!")
# PRN 장치를 초기화할 수 없습니다.
# 원인 : PowerShell에서 print는 Python 문법이 아니라 프린터 장치를 의미하는 예약어로 받아들여져서 오류가 난 것.

# 해결방법 : 터미널에서 python입력으로 Python 인터랙티브 모드(대화형 모드) 열기
# PS C:\Users\권나현\Desktop\python-study\Python-Tutorial> python
# Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("Hello, World!")
# Hello, World!

"""
📌 파이썬 들여쓰기(Indentation)
===============================

들여쓰기란?
------------
들여쓰기는 코드 줄의 시작 부분에 들어가는 공백을 의미합니다.
다른 프로그래밍 언어에서 들여쓰기는 단순히 '가독성'을 위한 경우가 많지만,
Python에서는 들여쓰기가 매우 중요한 문법 요소입니다.

파이썬은 들여쓰기를 사용하여 코드 블록을 표시합니다.

예시 (올바른 들여쓰기):
------------------------
if 5 > 2:
    print("Five is greater than two!")

예시 (잘못된 들여쓰기 – 오류 발생):
-----------------------------------
# Syntax Error 발생
if 5 > 2:
print("Five is greater than two!")

들여쓰기 공백 개수
--------------------
들여쓰기는 최소 1개의 공백이 필요하며,
일반적으로 4개의 공백을 사용하는 것이 표준입니다.

예:
if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
        print("Five is greater than two!") 

⚠️ 주의: 같은 코드 블록에서는 반드시 같은 수의 공백을 사용해야 합니다.
그렇지 않으면 Python에서 오류가 발생합니다.

예시 (잘못된 들여쓰기 – 서로 다른 공백 수):
-----------------------------------------------
# Syntax Error 발생
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!")
"""
# 파이썬 들여쓰기

if 5 > 2:
    print("Five is greater than two!")
# 결과 : Five is greater than two!

# if 5 > 2:
# print("Five is greater than two!")
# 결과 :
# File "<stdin>", line 1
# & C:/Users/권나현/AppData/Local/Programs/Python/Python313/python.exe c:/Users/권나현/Desktop/python-study/Python-Tutorial/03_Syntax.py
# ^
# SyntaxError: invalid syntax

"""
📌 파이썬 변수 (Python Variables)
=================================

변수 생성
-----------
Python에서는 값을 할당하는 순간 변수가 자동으로 생성됩니다.
따로 변수를 선언하는 명령은 존재하지 않습니다.

예시:
    x = 5
    y = "Hello, World!"

즉, 변수는 자료형에 상관없이 값을 넣는 즉시 만들어집니다.

더 자세한 내용은 ‘Python 변수(Variables)’ 장에서 다룹니다.
"""
# 파이썬 변수

x = 5
y = "Hello, World!"

"""
📌 파이썬 주석 (Comments)
=========================

Python에서는 코드 안에 설명이나 메모를 남기기 위해 '주석(comment)'을 사용합니다.

주석 작성 방법
----------------
파이썬에서 주석은 # 기호로 시작하며,
해당 줄에서 # 이후의 모든 내용은 실행되지 않고 무시됩니다.

예시:
    # This is a comment.
    print("Hello, World!")   # 이것도 가능 (코드 뒤 주석)

주석은 코드의 이해를 돕거나,
기능 설명, TODO 메모 등에 사용됩니다.
"""
# 파이썬 변수

# 주석처리
x = 5 # 설명 주석