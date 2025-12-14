####################################################################################
# 파이썬 JSON
####################################################################################

# JSON은 데이터를 저장하고 교환하기 위한 구문입니다.
# JSON은 JavaScript 객체 표기법으로 작성된 텍스트입니다.

#######################################
# 파이썬의 JSON
#######################################
# jsonPython에는 JSON 데이터를 다루는 데 사용할 수 있는 이라는 내장 패키지가 있습니다 .

# 예
# JSON 모듈을 가져옵니다.

import json

#######################################
# JSON 구문 분석 - JSON에서 Python으로 변환
#######################################
# JSON 문자열이 있는 경우 해당 json.loads()메서드를 사용하여 구문 분석할 수 있습니다.
# 결과는 Python 사전이 됩니다 .

# 예
# JSON에서 Python으로 변환:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# 30

#######################################
# Python에서 JSON으로 변환
#######################################
# Python 객체가 있는 경우 해당 json.dumps()메서드를 사용하여 이를 JSON 문자열로 변환할 수 있습니다.

# 예
# Python에서 JSON으로 변환:
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# {"name": "John", "age": 30, "city": "New York"}

# 다음 유형의 Python 객체를 JSON 문자열로 변환할 수 있습니다.
# 사전 dict
# 목록 list
# 튜플 tuple
# 끈  string
# 정수 int
# 뜨다 float
# 진실 True
# 거짓 False
# 없음 None

# 예
# Python 객체를 JSON 문자열로 변환하고 값을 출력합니다.
import json

print(json.dumps({"name": "John", "age": 30}))
# {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))
# ["apple", "bananas"]
print(json.dumps(("apple", "bananas")))
# ["apple", "bananas"]
print(json.dumps("hello"))
# "hello"
print(json.dumps(42))
# 42
print(json.dumps(31.76))
# 31.76
print(json.dumps(True))
# true
print(json.dumps(False))
# false
print(json.dumps(None))
# null

# Python에서 JSON으로 변환하면 Python 객체가 JSON(JavaScript)과 동일하게 변환됩니다.

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

# 예
# 모든 합법적인 데이터 유형을 포함하는 Python 객체를 변환합니다.
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

#######################################
# 결과 형식 지정
#######################################
# 위의 예는 JSON 문자열을 출력하지만, 들여쓰기와 줄바꿈이 없어 읽기가 쉽지 않습니다.
# 이 json.dumps()메서드에는 결과를 더 쉽게 읽을 수 있도록 하는 매개변수가 있습니다.

# 예
# 매개변수를 사용하여 indent들여쓰기 횟수를 정의합니다.
json.dumps(x, indent=4)
# 구분 기호를 정의할 수도 있습니다. 기본값은 (", ", ": ")입니다. 즉, 쉼표와 공백을 사용하여 각 객체를 구분하고 콜론과 공백을 사용하여 키와 값을 구분합니다.

# 예
# 매개변수를 사용하여 separators기본 구분 기호를 변경합니다.
json.dumps(x, indent=4, separators=(". ", " = "))

#######################################
# 결과를 주문하세요
#######################################
# 이 json.dumps()메서드에는 결과의 키를 정렬하기 위한 매개변수가 있습니다.
# 예
# sort_keys결과를 정렬할지 여부를 지정하려면 매개변수를 사용하세요.

json.dumps(x, indent=4, sort_keys=True)


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Consider the following code:
import datetime
x = datetime.datetime
# Which syntax will print the current date?

# print(x.datetime())
# print(x.date())
# print(x.now())          # Correct Answer!