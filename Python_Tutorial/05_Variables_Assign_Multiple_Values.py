####################################################################################
# 파이썬 변수 - 여러 값 할당
####################################################################################

#######################################
# 여러 변수에 대한 여러 값
#######################################
# Python을 사용하면 한 줄로 여러 변수에 값을 할당할 수 있습니다.

# 예
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Orange
# Banana
# Cherry

# 참고: 변수의 개수와 값의 개수가 일치하는지 확인하세요. 일치하지 않으면 오류가 발생합니다.

#######################################
# 하나의 값을 여러 변수에
#######################################
# 그리고 한 줄에 여러 변수에 같은 값을 할당할 수 있습니다.

# 예
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Orange
# Orange
# Orange

#######################################
# 컬렉션 풀기
#######################################
# list, 등의 값 컬렉션이 있는 경우, tuple Python에서는 값을 변수로 추출할 수 있습니다. 이를 '언 패킹' 이라고 합니다.
# 예
# 목록을 풀어보세요:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# apple
# banana
# cherry

# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Exercise
# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# What is a correct syntax to add the value 'Hello World', to 3 variables in one statement?
# x, y, z = 'Hello World'
# x = y = z = 'Hello World'     # Correct Answer!
# x|y|z = 'Hello World'

# HAM : x, y, z = 'Hello World' 이렇게 하면 어떻게 돼?
# GPT : x, y, z = 'Hello World' 이 코드는 문자열을 하나씩 분해해서 변수에 순서대로 할당하려는 시도야.
#       'Hello World'는 길이가 11개인 문자열이야.
#       H e l l o   W o r l d
#       1 2 3 4 5 6 7 8 9 10 11
#       근데 너는 변수 3개(x, y, z)에 이 문자열을 하나씩 나눠 넣으려고 한 거야.
#       즉 Python 입장에서는 이렇게 보임:
#       x = 'H'
#       y = 'e'
#       z = 'l'
#       ? = 'l'
#       ? = 'o'
#       ...
#       하지만 변수는 3개뿐이라서 나머지 글자를 받을 곳이 없기 때문에 오류가 남.
#       개수 맞게 하거나 확장 언패킹을 하면 됨
#       x, y, *z = 'Hello World'
#       x = 'H'
#       y = 'e'
#       z = ['l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']