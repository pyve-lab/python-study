####################################################################################
# 파이썬 - 출력 변수
####################################################################################

#######################################
# 출력 변수
#######################################
# 이 print()함수는 종종 변수를 출력하는 데 사용됩니다.

# 예
x = "Python is awesome"
print(x)
# Python is awesome

# 함수에서는 print()쉼표로 구분된 여러 변수를 출력합니다.

# 예
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Python is awesome

# + 연산자를 사용하여 여러 변수를 출력할 수도 있습니다.

# 예
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Python is awesome

# "Python "and 뒤에 있는 공백 문자에 주목하세요. 공백 문자 "is "가 없으면 결과는 "Pythonisawesome"이 됩니다.

# 숫자의 경우 해당 +문자는 수학 연산자로 작동합니다.

# 예
x = 5
y = 10
print(x + y)
# 15

# 함수 에서 연산자를 print()사용하여 문자열과 숫자를 결합하려고 하면 + Python에서 오류가 발생합니다.

# 예 (오류)
# x = 5
# y = "John"
# print(x + y)
# Traceback (most recent call last):
#   File "05_Variables_Output_Variables.py", line 48, in <module>
#     print(x + y)
#           ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 함수 에서 여러 변수를 출력하는 가장 좋은 방법은 print()쉼표로 구분하는 것입니다. 쉼표는 다양한 데이터 유형을 지원합니다.

# 예
x = 5
y = "John"
print(x, y)
# 5 John

# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Exercise
# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Consider the following code:
print('Hello', 'World')
# What will be the printed result?

# Hello, World
# Hello World       # Correct Answer!
# HelloWorld