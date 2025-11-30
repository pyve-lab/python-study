"""
============================================================
📌 Python JSON — 데이터 저장 & 교환 형식
============================================================

● JSON(JavaScript Object Notation)
  - 데이터를 저장하고 교환하기 위한 형식
  - 문자열 기반, 가벼움
  - 언어와 무관하게 사용됨

● Python에서는 json 내장 모듈로 JSON 처리 가능
    import json
"""

"""
============================================================
📌 1. JSON 문자열 → Python 객체 (파싱)
============================================================

● json.loads() : JSON 문자열을 Python 객체로 변환

예:
    import json

    x = '{ "name":"John", "age":30, "city":"New York" }'
    y = json.loads(x)  # Python dict로 변환

    print(y["age"])  # 30
"""
# 파이썬 JSON 문자열 파싱 예제

import json
x = '{ "name":"John", "age":30, "city":"New York" }'
y = json.loads(x)
print(y["age"])  # 30

"""
============================================================
📌 2. Python 객체 → JSON 문자열 (직렬화)
============================================================

● json.dumps() : Python 객체를 JSON 문자열로 변환

예:
    import json

    x = {"name": "John", "age": 30, "city": "New York"}
    y = json.dumps(x)

    print(y)  # {"name": "John", "age": 30, "city": "New York"}
"""
# 파이썬 JSON 직렬화 예제

import json
x = {"name": "John", "age": 30, "city": "New York"}
y = json.dumps(x)
print(y)  # {"name": "John", "age": 30, "city": "New York"} 

"""
============================================================
📌 3. JSON으로 변환 가능한 Python 타입
============================================================

Python              JSON
---------------------------------
dict        →       object
list        →       array
tuple       →       array
str         →       string
int/float   →       number
True        →       true
False       →       false
None        →       null

예:
    json.dumps(["apple", "banana"])
    json.dumps(("apple", "banana"))
    json.dumps(42)
    json.dumps(True)
    json.dumps(None)
"""
# 파이썬 JSON 변환 가능한 타입 예제

import json
print(json.dumps(["apple", "banana"]))  # '["apple", "banana"]'
print(json.dumps(("apple", "banana")))  # '["apple", "banana"]'
print(json.dumps(42))                    # '42'
print(json.dumps(True))                  # 'true'
print(json.dumps(None))                  # 'null'

"""
============================================================
📌 4. 복합 구조도 변환 가능
============================================================

예:
    x = {
      "name": "John",
      "age": 30,
      "married": True,
      "children": ("Ann", "Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
      ]
    }

    print(json.dumps(x))
"""
# 파이썬 JSON 복합 구조 변환 예제

import json
x = {
  "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
      {"model": "BMW 230", "mpg": 27.5},
      {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))
# 결과 : {"name": "John", "age": 30, "married": true, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

"""
============================================================
📌 5. JSON 결과를 더 예쁘게 출력하기
============================================================

● 들여쓰기(indent)
    json.dumps(x, indent=4)

● 구분자 변경(separators)
    # 기본: (", ", ": ")
    json.dumps(x, indent=4, separators=(". ", " = "))

● 키 정렬(sort_keys)
    json.dumps(x, indent=4, sort_keys=True)
"""
# 파이썬 JSON 예쁘게 출력하기 예제

import json
x = {
  "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
      {"model": "BMW 230", "mpg": 27.5},
      {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# 들여쓰기
print(json.dumps(x, indent=4))
# 결과 : {
#     "name": "John",
#     "age": 30,
#     "married": true,
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "pets": null,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ]
# }

# 구분자 변경
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# 결과 : {
#     "name" = "John".
#     "age" = 30.
#     "married" = true.
#     "children" = [
#         "Ann".
#         "Billy"
#     ].
#     "pets" = null.
#     "cars" = [
#         {
#             "model" = "BMW 230".
#             "mpg" = 27.5
#         }.
#         {
#             "model" = "Ford Edge".
#             "mpg" = 24.1
#         }
#     ]
# }

# 키 정렬
print(json.dumps(x, indent=4, sort_keys=True))
# 결과 : {
#     "age": 30,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ],
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "married": true,
#     "name": "John",
#     "pets": null
# }

"""
============================================================
📌 핵심 요약
============================================================

✔ loads() → JSON 문자열 → Python 객체(dict 등)
✔ dumps() → Python 객체 → JSON 문자열
✔ indent / separators / sort_keys로 출력 포맷 제어 가능
✔ 데이터 교환·API 응답에서 매우 자주 사용됨

============================================================
"""
