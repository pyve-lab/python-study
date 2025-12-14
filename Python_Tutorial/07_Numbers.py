####################################################################################
# 파이썬 숫자
####################################################################################

#######################################
# 파이썬 숫자
#######################################
# Python에는 세 가지 숫자형이 있습니다.
# int
# float
# complex

# 숫자형 변수는 값을 할당할 때 생성됩니다.

# 예
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# Python에서 객체의 유형을 확인하려면 다음 type()함수를 사용하세요.

# 예
print(type(x))
print(type(y))
print(type(z))
# <class 'int'>
# <class 'float'>
# <class 'complex'>

#######################################
# Int
#######################################
# Int 또는 정수는 소수점이 없는 양수 또는 음수의 정수이며, 길이는 제한이 없습니다.

# 예
# 정수:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
# <class 'int'>
# <class 'int'>
# <class 'int'>

#######################################
# Float
#######################################
# 부동 소수점 숫자 또는 "부동 소수점 숫자"는 하나 이상의 소수점을 포함하는 양수 또는 음수 숫자입니다.
# 예
# Float:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
# <class 'float'>
# <class 'float'>
# <class 'float'>

# Float는 10의 거듭제곱을 나타내는 "e"를 사용한 과학적 숫자일 수도 있습니다.

# 예
# Float:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
# <class 'float'>
# <class 'float'>
# <class 'float'>

#######################################
# Complex
#######################################
# 복소수는 허수부에 "j"를 붙여서 표기합니다.

# 예
# Complex:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
# <class 'complex'>
# <class 'complex'>
# <class 'complex'>

#######################################
# 유형 변환 Type Conversion
#######################################
# int(), float(), 및 메서드를 사용하여 한 유형에서 다른 유형으로 변환할 수 있습니다 complex().

# 예
# 한 유형에서 다른 유형으로 변환:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)        # 1.0
print(b)        # 2
print(c)        # (1+0j)

print(type(a))  # <class 'float'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'complex'>

# 참고: 복소수를 다른 숫자 유형으로 변환할 수 없습니다.

#######################################
# 난수 Random Number
#######################################
# Python에는 난수를 만드는 함수가 없지만 Python에는 난수를 만드는 데 사용할 수 있는 random()내장 모듈이 있습니다 .random

# 예
# random 모듈을 가져와서 1에서 9까지의 난수를 표시합니다.
import random

print(random.randrange(1, 10))
# 7

# 랜덤 모듈 참조 에서는 랜덤 모듈에 대해 자세히 알아볼 수 있습니다.

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Which is NOT a legal numeric data type in Python:
# Python에서 합법적인 숫자형 데이터 유형이 아닌 것은 무엇입니까?
# int
# long          # Correct Answer!
# float