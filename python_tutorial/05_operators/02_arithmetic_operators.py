# Arithmetic Operators
# 파이썬 산술 연산자 (Arithmetic Operators)

# 산술 연산자는 숫자 값과 함께 사용되어 일반적인 수학적 연산을 수행합니다.
# ------------------------------------------------------------------------------

# 산술 연산자 종류 (Arithmetic Operators List)

# Operator | Name | Example

# + | Addition (덧셈) | x + y
# - | Subtraction (뺄셈) | x - y
# * | Multiplication (곱셈) | x * y
# / | Division (나눗셈) | x / y
# % | Modulus (나머지) | x % y
# ** | Exponentiation (거듭제곱) | x ** y
# // | Floor division (몫 나눗셈) | x // y


# ------------------------------------------------------------------------------
# 예시: 다양한 산술 연산자 사용
# ------------------------------------------------------------------------------
x = 15
y = 4

# print(f"x = {x}, y = {y}")

# 덧셈 (Addition)
print(x + y) # 19

# 뺄셈 (Subtraction)
print(x - y) # 11

# 곱셈 (Multiplication)
print(x * y) # 60

# 나눗셈 (Division)
print(x / y) # 3.75

# 나머지 (Modulus)
print(x % y) # 3 (15를 4로 나누면 나머지는 3)

# 거듭제곱 (Exponentiation)
print(x ** y) # 50625 (15의 4제곱)

# 몫 나눗셈 (Floor Division)
print(x // y) # 3 (15를 4로 나눈 몫)


# ------------------------------------------------------------------------------
# 파이썬의 나눗셈 (Division in Python)
# ------------------------------------------------------------------------------

# 파이썬에는 두 가지 나눗셈 연산자가 있습니다:
# 1. /  - 일반 나눗셈 (Division): 결과를 부동 소수점(float)으로 반환합니다.
# 2. // - 몫 나눗셈 (Floor Division): 결과를 정수(integer)로 반환합니다. (가장 가까운 정수로 내림)

# 예시: 일반 나눗셈 (결과는 항상 float)
x_div = 12
y_div = 5

print(x_div / y_div) # 출력: 2.4

# 예시: 몫 나눗셈 (결과는 항상 integer, 내림)
# 소수점 아래를 버리고 가장 가까운 정수로 내림합니다.
x_floor = 12
y_floor = 5

print(x_floor // y_floor) 
# 출력: 2