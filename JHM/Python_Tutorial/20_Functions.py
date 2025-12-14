####################################################################################
# 파이썬 힘수
####################################################################################

#######################################
# 파이썬 함수
#######################################
# 함수는 호출될 때만 실행되는 코드 블록입니다.
# 함수는 결과로 데이터를 반환할 수 있습니다.
# 함수는 코드 반복을 피하는 데 도움이 됩니다.

#######################################
# 함수 만들기
#######################################
# Python에서 함수는 def 키워드를 사용하여 정의되고, 그 뒤에 함수 이름과 괄호가 옵니다.

# 예
def my_function():
  print("Hello from a function")

# my_function이렇게 하면 호출 시 "Hello from a function"이라는 메시지를 출력하는 함수가 생성됩니다 .
# 함수 내부의 코드는 들여쓰기를 해야 합니다. 파이썬은 들여쓰기를 사용하여 코드 블록을 정의합니다.

#######################################
# 함수 호출
#######################################
# 함수를 호출하려면 함수 이름 뒤에 괄호를 씁니다.

# 예
def my_function():
  print("Hello from a function")

my_function()
# Hello from a function

# 동일한 함수를 여러 번 호출할 수 있습니다.

# 예
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

# Hello from a function
# Hello from a function
# Hello from a function

#######################################
# 함수 이름
#######################################
# 함수 이름은 Python의 변수 이름과 동일한 규칙을 따릅니다.

# 함수 이름은 문자 또는 밑줄로 시작해야 합니다.
# 함수 이름에는 문자, 숫자, 밑줄만 포함될 수 있습니다.
# 함수 이름은 대소문자를 구분합니다( myFunction및 myfunction는 다릅니다)

# 예
# 유효한 함수 이름:
# calculate_sum()
# _private_function()
# myFunction2()

# 함수의 기능을 설명하는 설명적인 이름을 사용하는 것이 좋습니다.

#######################################
# 왜 함수를 사용해야 하나요?
#######################################
# 프로그램에서 화씨 온도를 섭씨로 여러 번 변환해야 한다고 가정해 보겠습니다.
# 함수가 없다면 같은 계산 코드를 반복해서 작성해야 할 것입니다.

# 예
# 함수 없이 - 반복적인 코드:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
# 25.0
# 35.0
# 10.0

# 함수를 사용하면 코드를 한 번만 작성하고 재사용할 수 있습니다.

# 예
# 함수를 사용하여 재사용 가능한 코드:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
# 25.0
# 35.0
# 10.0

#######################################
# 반환 값
#######################################
# 함수는 명령문을 사용하여 호출한 코드로 데이터를 다시 보낼 수 있습니다 return.
# 함수가 return명령문에 도달하면 실행을 멈추고 결과를 다시 보냅니다.

# 예
# 값을 반환하는 함수:
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
# Hello from a function

# 반환된 값을 직접 사용할 수 있습니다.

# 예
# 반환 값을 직접 사용:
def get_greeting():
  return "Hello from a function"

print(get_greeting())
# Hello from a function

# 함수에 명령문이 없으면 기본적으로 return반환됩니다 .None

#######################################
# 패스 진술 The pass Statement
#######################################
# 함수 정의는 비워둘 수 없습니다. 코드 없이 함수 자리 표시자를 생성해야 하는 경우 pass다음 문을 사용하세요.

# 예
def my_function():
  pass

# 이 pass문장은 개발 시 자주 사용되며, 먼저 구조를 정의하고 나중에 세부 사항을 구현할 수 있습니다.

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the correct keyword for defining functions in Python?

# function
# func
# def        # Correct Answer!