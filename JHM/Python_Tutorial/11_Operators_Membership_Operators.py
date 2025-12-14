####################################################################################
# 파이썬 멤버십 연산자
####################################################################################

#######################################
# 멤버십 운영자
#######################################
# 멤버십 연산자는 객체에 시퀀스가 표현되는지 테스트하는 데 사용됩니다.

# Operator	Description	Example
# in 	Returns True if a sequence with the specified value is present in the object	x in y
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
# True

# not in	Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
# True

# 예
# "banana"가 목록에 있는지 확인하세요.
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
# True

# 예
# 목록에 "pineapple"이 없는지 확인하세요:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
# True

#######################################
# 문자열의 멤버십
#######################################
# 멤버십 연산자는 문자열과도 작동합니다.

# 예
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)
# True
# False
# True

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What does the in operator do?

# Checks if a value exists in a sequence        # Correct Answer!
# Adds a value to a list
# Compares two values