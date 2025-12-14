####################################################################################
# 파이썬 - 변수 이름
####################################################################################

#######################################
# 변수 이름
#######################################
# 변수는 짧은 이름(예: x 및 y)을 가질 수도 있고, 더 설명적인 이름(예: age, carname, total_volume)을 가질 수도 있습니다.

# Python 변수에 대한 규칙
# - 변수 이름은 문자 또는 밑줄 문자로 시작해야 합니다.
# - 변수 이름은 숫자로 시작할 수 없습니다.
# - 변수 이름에는 영숫자 문자와 밑줄(Az, 0-9, _)만 포함될 수 있습니다.
# - 변수 이름은 대소문자를 구분합니다(age, Age 및 AGE는 세 개의 다른 변수입니다)
# - 변수 이름은 Python 키워드 중 하나가 될 수 없습니다.

# 예
# 합법적인 변수 이름:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar); print(my_var); print(_my_var); print(myVar); print(MYVAR); print(myvar2);
# John
# John
# John
# John
# John
# John

# 예 (오류)
# 불법적인 변수 이름:
# 2myvar = "John"
# my-var = "John"
# my var = "John"
# File "05_05_Variables_Names.py", line 35
# 2myvar = "John"
# ^
# SyntaxError: invalid decimal literal
# File "05_Variables_Names.py", line 36
# my-var = "John"
# ^^^^^^
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# File "05_Variables_Names.py", line 37
# my var = "John"
# ^^^
# SyntaxError: invalid syntax

# 변수 이름은 대소문자를 구분한다는 점을 기억하세요.

#######################################
# 여러 단어로 구성된 변수 이름
#######################################
# 변수 이름이 두 개 이상의 단어로 구성되면 읽기 어려울 수 있습니다.
# 읽기 쉽게 만들기 위해 사용할 수 있는 몇 가지 기술은 다음과 같습니다.

#######################################
# 낙타 케이스 Camel Case
#######################################
# 첫 번째 단어를 제외한 모든 단어는 대문자로 시작합니다.
# myVariableName = "John"

#######################################
# 파스칼 케이스 Pascal Case
#######################################
# 각 단어는 대문자로 시작합니다:
# MyVariableName = "John"

#######################################
# 뱀 케이스 Snake Case
#######################################
# 각 단어는 밑줄 문자로 구분됩니다.
# my_variable_name = "John"

# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Exercise
# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Which is NOT a legal variable name?

# my-var = 20       # Correct Answer!
# my_var = 20
# Myvar = 20
# _myvar = 20
