####################################################################################
# 파이썬 None
####################################################################################

#######################################
# 파이썬 없음
#######################################

# None는 값의 부재를 나타내는 Python의 특수 상수입니다.
# 데이터 유형은 NoneType, 이며 객체 None의 유일한 인스턴스입니다 NoneType.

#######################################
# 없음 유형 NoneType
#######################################
# None변수는 "값 없음" 또는 "설정되지 않음"을 나타내도록 할당될 수 있습니다.

# 예
# 값을 할당하고 표시합니다 None.
x = None
print(x)
# None

# type()값 의 유형을 확인하는 데 사용합니다 None.

# 예
# 값 의 데이터 유형을 할당하고 인쇄합니다 None.
x = None
print(type(x))
# <class 'NoneType'>

#######################################
# Comparing to None
#######################################
# 값을 비교하려면 None항등 연산자 is또는is not

# 예
# is비교를 위해 항등 연산자를 사용하세요 None:
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")
# No result yet

# 예
# 비슷한 예이지만 is not대신 다음을 사용합니다.
result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")
# No result yet

#######################################
# 참 또는 거짓
#######################################
# NoneFalse부울 컨텍스트에서 평가됩니다.

# 예
# 진실성 확인:
print(bool(None))
# False

#######################################
# None을 반환하는 함수 Functions returning None
#######################################
# 값을 명시적으로 반환하지 않는 함수는 None기본적으로 반환됩니다.

# 예
# 반환 문이 없는 함수는 다음을 반환합니다 None.
def myfunc():
  x = 5

x = myfunc()
print(x)
# None


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the data type of the value None?

# None
# NoneType    # Correct Answer!
# NullType