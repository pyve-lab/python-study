####################################################################################
# 파이썬 비트 연산자
####################################################################################

#######################################
# 비트 연산자
#######################################
# 비트 연산자는 (이진) 숫자를 비교하는 데 사용됩니다.

# Operator	Name	Description	Example
# & 	AND	Sets each bit to 1 if both bits are 1	x & y
print(6 & 3)
"""
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

# |	OR	Sets each bit to 1 if one of two bits is 1	x | y
print(6 | 3)
"""
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

# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101
print(6 ^ 3)

# ~	NOT	Inverts all the bits	~x  비트를 뒤집는 거라는데 쓸일 없을 듯 근데 맨 앞이 1이라서 음수가 된다카네
print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
# -4

# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

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
# 12

# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(8 >> 2)
"""
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

# 예
# & 연산자는 각 비트를 비교하여 둘 다 1이면 1로 설정하고, 그렇지 않으면 0으로 설정합니다.
print(6 & 3)
# 2

# 6의 이진 표현은 0110이고
# 3의 이진 표현은 0011입니다.
# 그런 다음 & 연산자는 비트를 비교하여 0010을 반환합니다. 이는 10진수로 2입니다.

# 예
# | 연산자는 각 비트를 비교하여 하나 또는 둘 다 1이면 1로 설정하고, 그렇지 않으면 0으로 설정합니다.
print(6 | 3)
# 7

# 6의 이진 표현은 0110이고
# 3의 이진 표현은 0011입니다.
# 그런 다음 | 연산자는 비트를 비교하여 0111을 반환합니다. 이는 10진수로 7입니다.

# 예
# ^ 연산자는 각 비트를 비교하여 하나만 1이면 1로 설정하고, 그렇지 않으면(둘 다 1이거나 둘 다 0이면) 0으로 설정합니다.
print(6 ^ 3)
# 6의 이진 표현은 0110이고
# 3의 이진 표현은 0011입니다.
# 5

# 그런 다음 ^ 연산자는 비트를 비교하여 0101을 반환합니다. 이는 10진수로 5입니다.

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the result of 0110 & 0011?

# 0010      # Correct Answer!
# 0011
# 1001