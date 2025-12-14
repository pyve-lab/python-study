####################################################################################
# 파이썬 항등 연산자
####################################################################################

#######################################
# 항등 연산자
#######################################
# 항등 연산자는 객체가 같은지 여부가 아니라 실제로 동일한 객체이고 동일한 메모리 위치를 가지고 있는지 여부를 비교하는 데 사용됩니다.

# Operator	Description	Example
# is 	Returns True if both variables are the same object	x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
# True
# False
# True

# is not	Returns True if both variables are not the same object	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
# False
# True
# False

# 예
# 두 변수가 모두 같은 객체를 가리키는 경우 연산자 is는 다음을 반환합니다 .True
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
# True
# False
# True

# 예
# 두 변수가 모두 같은 객체를 가리키지 않으면 연산자 is not는 다음을 반환합니다 .True
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)
# True
# HAM : 왜 다르다는 거야?
# GPT : == 는 값(내용) 비교
#       is / is not은 “객체 자체(메모리 주소)” 비교

#######################################
# is와 의 차이점==
#######################################
# is - 두 변수가 메모리에서 동일한 객체를 가리키는지 확인합니다.
# == - 두 변수의 값이 같은지 확인합니다.

# 예
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
# True
# False

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What does the is operator check?

# If two values are equal
# If two variables point to the same object     # Correct Answer!
# If a value exists