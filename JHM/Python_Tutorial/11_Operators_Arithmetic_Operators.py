####################################################################################
# 파이썬 산술 연산자
####################################################################################

#######################################
# 산술 연산자
#######################################
# 산술 연산자는 숫자 값과 함께 사용되어 일반적인 수학 연산을 수행합니다.

# Operator	Name	Example
# +	Addition	x + y
x = 5
y = 3
print(x + y)
# 8

# -	Subtraction	x - y
x = 5
y = 3
print(x - y)
# 2

# *	Multiplication	x * y
x = 5
y = 3
print(x * y)
# 15

# /	Division	x / y
x = 12
y = 3
print(x / y)
# 4

# %	Modulus	x % y
x = 5
y = 2
print(x % y)
# 1

# **	Exponentiation	x ** y
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
#  32

# //	Floor division	x // y
x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole number
# 7

# 예시
# 다음은 다양한 산술 연산자를 사용한 예입니다.

# 예
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
# 19
# 11
# 60
# 3.75
# 3
# 50625
# 3

#######################################
# 파이썬에서의 나눗셈
#######################################
# 파이썬에는 두 가지 나누기 연산자가 있습니다.
# / - 나누기(float를 반환)
# // - 나눗셈(정수를 반환)

# 예
# 나누기는 항상 float를 반환합니다.
x = 12
y = 5
print(x / y)
# 2.4

# 예
# 내림차순 나눗셈은 항상 정수를 반환합니다.
# 가장 가까운 정수로 반올림합니다.
x = 12
y = 5
print(x // y)
# 2

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the result of 15 % 4?
# 3                 # Correct Answer!
# 3.75
# 4