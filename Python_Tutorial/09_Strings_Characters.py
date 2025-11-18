####################################################################################
# 파이썬 - 이스케이프 문자
####################################################################################

#######################################
# 이스케이프 문자
#######################################
# 문자열에 허용되지 않는 문자를 삽입하려면 이스케이프 문자를 사용하세요.
# 이스케이프 문자는 백슬래시 \뒤에 삽입하려는 문자를 입력하는 것입니다.
# 불법 문자의 예로는 큰따옴표로 둘러싸인 문자열 내부의 큰따옴표가 있습니다.

# 예 (오류)
# 큰따옴표로 둘러싸인 문자열 안에 큰따옴표를 사용하면 오류가 발생합니다.
# txt = "We are the so-called "Vikings" from the north."
# print(txt)
#   File "09_Strings_Characters.py", line 15
#     txt = "We are the so-called "Vikings" from the north."
#                                  ^^^^^^^
# SyntaxError: invalid syntax

# 이 문제를 해결하려면 이스케이프 문자를 사용하세요 \".
# 예
# 이스케이프 문자를 사용하면 일반적으로 허용되지 않는 큰따옴표를 사용할 수 있습니다.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# We are the so-called "Vikings" from the north.

#######################################
# 이스케이프 문자
#######################################
# Python에서 사용되는 다른 이스케이프 문자:

# Code	Result
# \'	Single Quote    작은따옴표 문자 출력
txt = 'It\'s alright.'
print(txt)
# It's alright.

# \\	Backslash       백슬래시 문자 출력
txt = "This will insert one \\ (backslash)."
print(txt)
# This will insert one \ (backslash).

# \n	New Line        새 줄로 이동
txt = "Hello\nWorld!"
print(txt)
# Hello
# World!

# \r	Carriage Return  커서(문자 위치)를 맨 앞으로 이동(줄 맨 앞으로 이동 후, 뒤 문자열로 덮어씀)
txt = "Hello\rWorld!"
print(txt)
# World!

# \t	Tab             네 칸 또는 일정 간격 띄움
txt = "Hello\tWorld!"
print(txt)
# Hello   World!

# \b	Backspace       직전 문자 삭제
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
# HelloWorld!

# \f	Form Feed       페이지 넘김 → 개행처럼 보일 수 있음
txt = "Hello\fWorld"
print(txt)
# Hello
#      World

# \ooo	Octal value     8진수 값으로 문자 표현
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
# Hello

# \xhh	Hex value       16진수(헥사) 값으로 문자 표현
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
# Hello