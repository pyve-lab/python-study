"""
📌 파이썬 명령문(Statements)
============================

컴퓨터 프로그램이란?
---------------------
컴퓨터 프로그램은 컴퓨터가 실행해야 할 '지시(instruction)'들의 목록입니다.

프로그래밍 언어에서는 이러한 지시들을 '명령문(statement)'이라고 부릅니다.

예시 명령문:
-------------
다음 문장은 화면에 "Python is fun!"을 출력하는 파이썬 명령문입니다.

    print("Python is fun!")

파이썬 명령문의 특징
----------------------
Python에서는 **줄의 끝이 곧 명령문의 끝**입니다.

따라서 Java, C 등의 언어에서 사용하는 세미콜론(;)을 명령문 끝에 붙일 필요가 없습니다.

예:
    print("Hello")        # 세미콜론 없이 OK
    print("World");       # 세미콜론을 붙여도 동작은 하지만 권장되지 않음
"""
# 파이썬 명령문

print("Hello") # 결과 : Hello
print("World") # 결과 : World

"""
📌 많은 문장(Multiple Statements)
=================================

대부분의 Python 프로그램은 여러 개의 명령문(Statements)으로 구성됩니다.
이 명령문들은 작성된 순서대로 위에서 아래로 하나씩 실행됩니다.

예시:
    print("Hello World!")
    print("Have a good day.")
    print("Learning Python is fun!")

예시 설명
-----------
위 코드에는 총 세 개의 명령문이 있습니다.

1) 첫 번째 문장 실행
       print("Hello World!")
   → 화면에 "Hello World!" 출력

2) 두 번째 문장 실행
       print("Have a good day.")
   → 화면에 "Have a good day." 출력

3) 세 번째 문장 실행
       print("Learning Python is fun!")
   → 화면에 "Learning Python is fun!" 출력

이처럼 Python은 작성된 순서대로 문장을 차례대로 실행합니다.
"""
# 파이썬 여러 문장 출력

print("Hello World!") # 결과 : Hello World!
print("Have a good day.") # 결과 : Have a good day.
print("Learning Python is fun!") # 결과 : Learning Python is fun!

"""
📌 세미콜론(;) — 선택 사항, 거의 사용되지 않음
===========================================

파이썬에서 세미콜론은 **필수가 아닌 선택 사항**입니다.
세미콜론을 사용하면 한 줄에 여러 문장을 넣을 수 있지만,
코드 가독성이 떨어지기 때문에 실제로는 거의 사용하지 않습니다.

예시 (가능하지만 권장하지 않음):
    print("Hello"); print("How are you?"); print("Bye bye!")

⚠️ 주의  
줄 바꿈(newline)이나 세미콜론(;) 같은 '구분 기호' 없이  
한 줄에 여러 문장을 쓰면 Python은 오류를 발생시킵니다.

잘못된 예:
    print("Python is fun!") print("Really!")

결과:
    SyntaxError: invalid syntax
"""
# 파이썬 세미콜론

print("Hello"); print("How are you?"); print("Bye bye!") 
# 결과 : 
# Hello
# How are you?
# Bye bye!