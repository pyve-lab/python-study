####################################################################################
# 파이썬 캐스팅
####################################################################################

#######################################
# 변수 유형 지정
#######################################
# 변수에 타입을 지정해야 할 때가 있습니다. 이는 캐스팅을 통해 가능합니다.
# Python은 객체 지향 언어이므로 클래스를 사용하여 기본 타입을 포함한 데이터 타입을 정의합니다.

# 따라서 파이썬에서의 캐스팅은 생성자 함수를 사용하여 수행됩니다.
# int() - 정수 리터럴, 모든 소수점을 제거한 부동 소수점 리터럴 또는 문자열 리터럴(문자열이 정수를 나타내는 경우)에서 정수를 생성합니다.
# float() - 정수 리터럴, float 리터럴 또는 문자열 리터럴에서 float 숫자를 구성합니다(문자열이 float 또는 정수를 나타내는 경우)
# str() - 문자열, 정수 리터럴, 부동 소수점 리터럴을 포함한 다양한 데이터 유형에서 문자열을 구성합니다.

# 예
# 정수:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)    # 1
print(y)    # 2
print(z)    # 3

# 예
# 플로트:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)    # 1.0
print(y)    # 2.8
print(z)    # 3.0
print(w)    # 4.2

# 예
# 문자열:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)    # s1
print(y)    # 2
print(z)    # 3.0


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What will be the result of the following code:
print(int(35.88))

# 35        # Correct Answer!
# # float
# 35.88
# 36