####################################################################################
# 파이썬 논리 연산자
####################################################################################

#######################################
# 논리 연산자
#######################################
# 논리 연산자는 조건문을 결합하는 데 사용됩니다.

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
x = 5
print(x > 3 and x < 10)
# True

# or	Returns True if one of the statements is true	x < 5 or x < 4
x = 5
print(x > 3 or x < 4)
# True

# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
x = 5
print(not(x > 3 and x < 10))
# False

# 예
# 숫자가 0보다 크고 10보다 작은 지 테스트합니다.
x = 5
print(x > 0 and x < 10)
# True

# 예
# 숫자가 5보다 작은지 또는 10보다 큰지 테스트합니다.
x = 5
print(x < 5 or x > 10)
# False

# 예
# not을 사용하여 결과를 반대로 합니다 .
x = 5
print(not(x > 3 and x < 10))
# False

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the result of 5 < 7 and 5 > 7?

# True
# False             # Correct Answer!
# None