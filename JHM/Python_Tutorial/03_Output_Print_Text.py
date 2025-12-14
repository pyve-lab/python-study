####################################################################################
# 파이썬 출력/인쇄
####################################################################################

#######################################
# 텍스트 인쇄
#######################################
# print()함수를 사용하여 텍스트를 표시하거나 값을 출력할 수 있다는 사실은 이미 알고 계셨습니다.

# 예
print("Hello World!")
# Hello World!

# print()이 함수는 원하는 만큼 사용할 수 있습니다. 각 호출은 기본적으로 새 줄에 텍스트를 출력합니다.

# 예
print("Hello World!")
print("I am learning Python.")
print("It is awesome!")
# Hello World!
# I am learning Python.
# It is awesome!

#######################################
# 큰따옴표
#######################################
# Python에서 텍스트는 따옴표로 묶어야 합니다. "큰따옴표나 '작은따옴표를 사용할 수 있습니다.
# HAM : 큰 따옴표랑 작은 따옴표의 차이가 뭐야?
# GPT : 둘 다 문자열을 만드는 용도는 완전히 동일해.
#       Python에서는 " "(큰따옴표)와 ' '(작은따옴표)를 기능적으로 구분하지 않아 — 즉, 성능 차이도 없고, 의미 차이도 없어.
#       단, 문자열 내부에 어떤 문자가 들어가느냐에 따라 편하게 선택하는 차이가 있어.
#       둘 다 쓰고 싶으면 → \ 백슬래시로 이스케이프
#       print("He said \"I'm here\"")

# 예
print("This will work!")
print('This will also work!')
# This will work!
# This will also work!

# 텍스트를 따옴표로 묶는 것을 잊어버리면 Python에서 오류가 발생합니다.

# 예 (오류)
# print(This will cause an error)
# File "03_Output_Print_Text.py", line 38
# print(This will cause an error)
# ^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

# 결과:
# SyntaxError: invalid syntax.

#######################################
# 줄바꿈 없이 인쇄
#######################################
# 기본적으로 print()함수는 새 줄로 끝납니다.
# 같은 줄에 여러 단어를 인쇄하려면 다음 end매개변수를 사용할 수 있습니다.

# 예
print("Hello World!", end=" ")
print("I will print on the same line.")
# Hello World! I will print on the same line.

# end=" "가독성을 높이기 위해 뒤에 공백을 추가했습니다 .

# HAM : end=" " 이렇게 하는 방법 밖에 없어?
# GPT : 1) 가장 기본: print(…, end=””)
#       2) 여러 값을 한 번에 print로 출력하기
#       print("Hello", "World")
#       >> Hello World
#       3) sys.stdout.write 사용하기 → 완전한 ‘줄바꿈 없음’
#       print()는 기본적으로 end=”\n”이 붙어 있어.
#       줄바꿈을 절대 안 하고 싶으면 sys.stdout.write()가 더 원초적이고 강력해.
#       import sys
#       sys.stdout.write("Hello ")
#       sys.stdout.write("World")
#       >> Hello World
#       - print보다 출력 속도도 조금 더 빠름
#       - 자동으로 공백도 줄바꿈도 안 붙임
#       - flush 필요할 때는 flush=True 써야 함
#       4) print(…, end=””) + 반복문 조합
#       for i in range(5):
#          print(i, end=" ")
#       >> 0 1 2 3 4
#       5) 문자열을 미리 합쳐서 한 번에 출력하기
#       text = ""
#       for i in range(5):
#           text += str(i) + " "
#       print(text)
#       >> print(" ".join(str(i) for i in range(5)))

