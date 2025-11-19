####################################################################################
# 파이썬 연산자 우선순위
####################################################################################

#######################################
# 연산자 우선순위
#######################################
# 연산자 우선순위는 연산이 수행되는 순서를 설명합니다.

# 예
# 괄호는 가장 높은 우선순위를 가지므로 괄호 안의 표현식이 먼저 평가되어야 합니다.
print((6 + 3) - (6 + 3))
# 0

# 예
# 곱셈은 * 덧셈보다 우선순위가 높으므로 곱셈은 덧셈보다 먼저 평가됩니다.
print(100 + 5 * 3)
# 115

#######################################
# 우선순위
#######################################
# 우선순위는 아래 표에 설명되어 있으며, 가장 높은 우선순위가 맨 위에 있습니다.
# Operator	Description
# ()	Parentheses
print((6 + 3) - (6 + 3))
"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
# 0

# **	Exponentiation
print(100 - 3 ** 3)
"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""
# 73

# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
print(100 + ~3)
"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""
# 96

# *  /  //  %	Multiplication, division, floor division, and modulus
print(100 + 5 * 3)
"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""
# 115

# +  -	Addition and subtraction
print(100 - 5 * 3)
"""
Subtraction has a lower precedence than multiplication, and we need to calculate the multiplication first.
The calculation above reads 100 - 15 = 85
"""
# 85

# <<  >>	Bitwise left and right shifts
print(8 >> 4 - 2)
"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
# 2

# &	Bitwise AND
print(6 & 2 + 1)
"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2

More explanation:
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
# 2
# ^	Bitwise XOR
print(6 ^ 2 + 1)
"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5

More explanation:
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
# 5

# |	Bitwise OR
print(6 | 2 + 1)
"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7

More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
# 7

# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
print(5 == 4 + 1)
"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""
# True

# not	Logical NOT
print(not 5 == 5)
"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""
# False

# and	AND
print(1 or 2 and 3)
"""
The and operator has a higher precedence than or, and we need to calculate the and expression first.
The calculation above reads: 1 or 3 = 1
"""
# 1
# GPT : 왼쪽 값이 False(거짓값)이면 → 왼쪽 값을 그대로 반환
#       왼쪽 값이 True(참값)이면 → 오른쪽 값을 평가하고 그 값을 반환

# or	OR
print(4 or 5 + 10 or 8)
"""
The or operator has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads: 4 or 15 or 8 = 4
"""
#  4
# GPT : or = 왼쪽이 참값이면 왼쪽을 그대로 반환
#       or 연산자는 “참 같은 값”을 만나면 거기서 멈춘다
#       파이썬에서 or는 이렇게 동작해:
#       ✔ 왼쪽 값이 True(=참 같은 값)이면 → 왼쪽 값을 그대로 반환
#       ✔ 왼쪽 값이 False(=거짓 같은 값)이면 → 오른쪽 값을 평가하고 반환
#       파이썬에서 숫자의 True/False 규칙:
#       0 → False
#       그 외 모든 숫자 → True
#       그래서 4는 True처럼 취급됨.

#######################################
# 왼쪽에서 오른쪽으로 평가
#######################################
# 두 연산자의 우선순위가 같으면 표현식은 왼쪽에서 오른쪽으로 평가됩니다.

# 예
# 덧셈 +과 뺄셈은 -동일한 우선순위를 가지므로 표현식은 왼쪽에서 오른쪽으로 평가됩니다.
print(5 + 4 - 7 + 3)
# False

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
# What is the result of 2 + 3 * 4?

# 20
# 14        # Correct Answer!
# 24