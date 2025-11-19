"""
📌 전역 변수 (Global Variables)
===============================

전역 변수란?
--------------
함수 외부에서 생성된 변수는 '전역 변수(global variable)'입니다.
전역 변수는 **함수 내부와 외부 모두**에서 사용할 수 있습니다.

예 — 함수 외부에서 만든 변수를 함수 내부에서 사용:
    x = "awesome"

    def myfunc():
        print("Python is " + x)

    myfunc()
"""
# 파이썬 전역 변수

x = "awesome"
def myfunc():
        print("Python is " + x)

myfunc()
# 결과 : Python is awesome

"""
📌 지역 변수와 전역 변수의 이름이 같을 때
----------------------------------------
함수 내부에서 전역 변수와 동일한 이름의 변수를 만들면,
그 변수는 함수 내부에서만 유효한 **지역 변수(local variable)**가 됩니다.

전역 변수는 원래 값을 유지합니다.

예:
    x = "awesome"

    def myfunc():
        x = "fantastic"   # 지역 변수
        print("Python is " + x)

    myfunc()

    print("Python is " + x)   # 전역 변수 사용
"""
# 파이썬 전역 변수와 지역 변수

x = "awesome"

def myfunc():
        x = "fantastic"   # 지역 변수
        print("Python is " + x)

myfunc()
# 결과 : Python is fantastic

print("Python is " + x)
# 결과 : Python is awesome

"""
📌 global 키워드
-----------------
함수 내부에서 변수를 만들면 기본적으로 지역 변수가 됩니다.
하지만 **global 키워드**를 사용하면 함수 내부에서도 전역 변수를 만들거나 수정할 수 있습니다.

예 — 함수 내부에서 전역 변수 생성:
    def myfunc():
        global x
        x = "fantastic"

    myfunc()

    print("Python is " + x)


예 — 함수 내부에서 전역 변수 수정:
    x = "awesome"

    def myfunc():
        global x
        x = "fantastic"   # 전역 변수 값을 변경

    myfunc()

    print("Python is " + x)
"""
# 파이썬 전역 변수 선언(global)

# 함수 내부에서 전역 변수 생성
def myfunc():
        global x
        x = "fantastic"

myfunc()

print("Python is " + x)
# 결과 : Python is fantastic

# 함수 내부에서 전역 변수 수정
x = "awesome"

def myfunc():
    global x
    x = "fantastic"   # 전역 변수 값을 변경

myfunc()

print("Python is " + x)
# 결과 : Python is fantastic