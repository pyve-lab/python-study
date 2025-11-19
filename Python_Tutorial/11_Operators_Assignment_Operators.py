####################################################################################
# 파이썬 할당 연산자
####################################################################################

#######################################
# 할당 연산자
#######################################
# 할당 연산자는 변수에 값을 할당하는 데 사용됩니다.

# Operator	Example	Same As
# =	x = 5	x = 5
x = 5
print(x)
# 5

# +=	x += 3	x = x + 3
x = 5
x += 3
print(x)
#  8

# -=	x -= 3	x = x - 3
x = 5
x -= 3
print(x)
# 2

# *=	x *= 3	x = x * 3
x = 5
x *= 3
print(x)
# 15

# /=	x /= 3	x = x / 3
x = 5
x /= 3
print(x)
# 1.6666666666666667

# %=	x %= 3	x = x % 3 너이자식나머지 반올림이구나
x = 5
x%=3
print(x)
# 2

# //=	x //= 3	x = x // 3 이놈은 나머지 버리기
x = 5
x//=3
print(x)
# 1

# **=	x **= 3	x = x ** 3
x = 5
x **= 3
print(x)
# 125

# &=	x &= 3	x = x & 3
x = 5
x &= 3
print(x)
# 1

# |=	x |= 3	x = x | 3
x = 5
x |= 3
print(x)
# 7

# ^=	x ^= 3	x = x ^ 3
x = 5
x ^= 3
print(x)
# 6

# >>=	x >>= 3	x = x >> 3
x = 5
x >>= 3
print(x)
# 0

# <<=	x <<= 3	x = x << 3
x = 5
x <<= 3
print(x)
# 40

# :=	print(x := 3)	x = 3
print(x := 3)
# 3

#######################################
# 바다코끼리 운영자 The Walrus Operator
#######################################
# Python 3.8에서는 "바다코끼리 연산자"로 알려진 := 연산자가 도입되었습니다. 이 연산자는 더 큰 표현식의 일부로 변수에 값을 할당합니다.

# 예
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# List has 5 elements
# List has 5 elements

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What will be the value of x after this code?
# x = 10
# x += 5

# 5
# 10
# 15        # Correct Answer!


