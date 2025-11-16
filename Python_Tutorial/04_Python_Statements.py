####################################################################################
# 파이썬 문장
####################################################################################

#######################################
# 진술
#######################################
# 컴퓨터 프로그램 은 컴퓨터가 "실행"해야 할 "지시" 목록입니다.
# 프로그래밍 언어에서는 이러한 프로그래밍 명령어를 명령문 이라고 합니다.
# 다음 문장은 "Python is fun!"이라는 텍스트를 화면에 출력합니다.

# 예
print("Python is fun!")
# Python is fun!

# Python에서는 일반적으로 줄이 끝나면 명령문이 끝납니다.
# 다른 프로그래밍 언어(예: Java 또는 C ) 처럼 세미콜론( )을 사용할 필요가 없습니다 .;

#######################################
# 많은 진술
#######################################
# 대부분의 Python 프로그램에는 많은 문장이 포함되어 있습니다.
# 문장은 쓰여진 순서대로 하나씩 실행됩니다.

# 예
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")
# Hello World!
# Have a good day.
# Learning Python is fun!

# 예시 설명
# 위의 예에서 우리는 세 가지 진술을 얻습니다.
# 1. print("Hello World!")
# 2. print("Have a good day.")
# 3. print("Learning Python is fun!")
# 첫 번째 문장이 먼저 실행됩니다("Hello World!"를 출력).
# 그런 다음 두 번째 문장이 실행됩니다("Have a good day."를 출력).
# 마지막으로 세 번째 문장이 실행됩니다("Learning Python is fun!"을 출력).

#######################################
# 세미콜론(선택 사항, 거의 사용되지 않음)
#######################################
# 파이썬에서 세미콜론은 선택 사항입니다. 세미콜론으로 여러 문장을 구분하여 한 줄에 작성할 수 있지만 ;, 읽기 어려워서 거의 사용하지 않습니다.

# 예
print("Hello"); print("How are you?"); print("Bye bye!")
# Hello
# How are you?
# Bye bye!

# 그러나 구분 기호(줄 바꿈 또는 .) 없이 같은 줄에 두 개의 문장을 넣으면 ; Python에서 오류가 발생합니다.

# 예 (오류)
# print("Python is fun!") print("Really!")
# File "04_Python_Statements.py", line 57
# print("Python is fun!") print("Really!")
# ^^^^^
# SyntaxError: invalid syntax

# 결과:
# SyntaxError: invalid syntax
# 모범 사례: 각 문장을 한 줄에 입력하면 코드를 쉽게 이해할 수 있습니다.
