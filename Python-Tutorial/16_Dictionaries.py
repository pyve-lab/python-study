"""
📌 Python 사전(Dictionary) 정리
==============================

사전은 **키:값 (key:value) 쌍**으로 데이터를 저장하는 컬렉션 타입입니다.

Python의 4가지 컬렉션 타입
--------------------------
- List       : 정렬됨, 변경 가능, 중복 허용
- Tuple      : 정렬됨, 변경 불가, 중복 허용
- Set        : 순서 없음, 변경 가능(요소는 변경 불가), 중복 없음
- Dictionary : 정렬됨(Python 3.7+), 변경 가능, 키 중복 없음

사전(Dictionary)의 특징
------------------------
1. **키:값 쌍**으로 구성
2. **순서 있음** (Python 3.7+)
3. **변경 가능 (mutable)**
4. **키 중복 불가** (같은 키를 다시 넣으면 기존 값 덮어씀)
5. **중괄호 {}** 또는 dict() 생성자 사용

예:
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)
"""
# 파이썬 사전(Dictionary) 개념 정리

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   
print(thisdict)
# 결과 : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

"""
사전 항목 접근
==============
- 대괄호로 키를 지정
- get() 메서드 사용도 가능

예:
    thisdict["brand"]      # "Ford"
    thisdict.get("model")  # "Mustang"
"""
# 파이썬 사전 항목 접근

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])      # Ford
print(thisdict.get("model"))  # Mustang

"""
사전의 길이(len)
=================
항목(키:값 쌍)의 개수 확인:

    len(thisdict)


사전 값의 데이터 타입
======================
값(Value)은 어떤 타입이든 가능:
- 문자열, 숫자, 불리언, 리스트, 다른 사전 등

예:
    thisdict = {
        "brand": "Ford",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }
"""
# 파이썬 사전 값의 데이터 타입

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
# 결과 : {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

"""
타입 확인
=========
Python에서 사전은 dict 타입 객체:

    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    print(type(thisdict))  # <class 'dict'>
"""
# 파이썬 사전 타입 확인

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))  # <class 'dict'>

"""
dict() 생성자
=============
dict() 를 사용해 사전 생성 가능:

    thisdict = dict(name="John", age=36, country="Norway")


키, 값, 항목 조회 (keys, values, items)
========================================

1) keys()
---------
- 사전의 모든 **키 목록(view)** 반환
- 사전에 변경이 생기면 이 뷰도 자동 반영됨

예:
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    x = car.keys()
    print(x)          # dict_keys([...])

    car["color"] = "white"
    print(x)          # 변경 내용 반영


2) values()
-----------
- 사전의 **값 목록(view)** 반환

예:
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    x = car.values()
    print(x)          # before change

    car["year"] = 2020
    print(x)          # after change

    car["color"] = "red"
    print(x)          # 추가된 값도 반영


3) items()
----------
- 각 항목을 **(키, 값) 튜플** 형태로 묶어 반환
- 이것도 view 이므로 변경 자동 반영

예:
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    x = car.items()
    print(x)          # before change

    car["year"] = 2020
    print(x)          # after change

    car["color"] = "red"
    print(x)          # 새 항목도 반영
"""
# 파이썬 사전 키, 값, 항목 조회

# 1) keys()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x_keys = car.keys()
print(x_keys)          # dict_keys(['brand', 'model', 'year'])

car["color"] = "white"
print(x_keys)          # dict_keys(['brand', 'model', 'year', 'color'])

# 2) values()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x_values = car.values()
print(x_values)        # dict_values(['Ford', 'Mustang', 1964, 'white'])

car["year"] = 2020
print(x_values)        # dict_values(['Ford', 'Mustang', 2020, 'white'])

car["color"] = "red"
print(x_values)        # dict_values(['Ford', 'Mustang', 2020, 'red'])

# 3) items()
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x_items = car.items()
print(x_items)         # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'red')])

car["year"] = 2021
print(x_items)         # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2021), ('color', 'red')])

car["color"] = "blue"
print(x_items)         # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2021), ('color', 'blue')])

"""
키 존재 여부 확인 (in)
======================
in 키워드로 특정 키가 있는지 확인:

예:
    if "model" in thisdict:
        print("Yes, 'model' is one of the keys")


값 변경 / 추가 / 업데이트
=========================

1) 특정 값 변경
----------------
키를 사용해 직접 값 수정:

    thisdict["year"] = 2018


2) update()로 값 변경
----------------------
update()에 다른 dict 또는 (키:값) 쌍을 넘기면 해당 키를 갱신 또는 추가:

    thisdict.update({"year": 2020})


3) 새 항목 추가
----------------
존재하지 않는 키에 값 할당 → 새 항목 추가:

    thisdict["color"] = "red"

또는 update() 사용:

    thisdict.update({"color": "red"})
"""
# 파이썬 사전 값 변경 / 추가 / 업데이트

# 1) 특정 값 변경
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# 2) update()로 값 변경
thisdict.update({"year": 2020})
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# 3) 새 항목 추가
thisdict["color"] = "red"
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}
thisdict.update({"color": "blue"})
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'blue'}

"""
항목 제거
=========
여러 방법 존재:

1) pop(key)
-----------
- 지정한 키의 항목 제거 및 **값 반환**

예:
    thisdict.pop("model")


2) popitem()
------------
- **마지막으로 추가된 항목** 제거 (Py3.7+)

예:
    thisdict.popitem()


3) del 키워드
--------------
- 특정 키 삭제:  del thisdict["model"]
- 사전 전체 삭제: del thisdict

예:
    del thisdict       # thisdict 자체가 사라짐


4) clear()
----------
- 모든 항목 삭제 (빈 사전으로 만들기)

    thisdict.clear()
"""
# 파이썬 사전 항목 제거

# 1) pop(key)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
model_value = thisdict.pop("model")
print(model_value)  # Mustang
print(thisdict)     # {'brand': 'Ford', 'year': 1964}

# 2) popitem()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
last_item = thisdict.popitem()
print(last_item)    # ('year', 1964)
print(thisdict)     # {'brand': 'Ford', 'model': 'Mustang'}

# 3) del 키워드
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)     # {'brand': 'Ford', 'year': 1964}

del thisdict
# print(thisdict)   # 오류 발생 (thisdict 자체가 삭제됨)

# 4) clear()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)     # {}

"""
사전 반복(for 루프)
====================
기본적으로 반복하면 **키**가 반환됨.

예:
    for x in thisdict:
        print(x)                # 키 출력

    for x in thisdict:
        print(thisdict[x])      # 값 출력

    for v in thisdict.values():
        print(v)                # 값만

    for k in thisdict.keys():
        print(k)                # 키만

    for k, v in thisdict.items():
        print(k, v)             # 키와 값 둘 다
"""
# 파이썬 사전 반복문

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
    print(x)                # brand / model / year
for x in thisdict:
    print(thisdict[x])      # Ford / Mustang / 1964
for v in thisdict.values():
    print(v)                # Ford / Mustang / 1964
for k in thisdict.keys():
    print(k)                # brand / model / year
for k, v in thisdict.items():
    print(k, v)             # brand Ford / model Mustang / year 1964

"""
사전 복사
=========
⚠ dict2 = dict1 은 **같은 객체 참조**이므로 진짜 복사가 아님.

진짜 복사 방법:

1) copy() 메서드
-----------------
    mydict = thisdict.copy()


2) dict() 함수
---------------
    mydict = dict(thisdict)
"""
# 파이썬 사전 복사

# 1) copy() 메서드
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict1 = thisdict.copy()
print(mydict1)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# 2) dict() 함수
mydict2 = dict(thisdict)
print(mydict2)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

"""
중첩 사전(Nested Dictionary)
=============================
사전 안에 사전을 넣어서 계층 구조를 만들 수 있음.

예:
    myfamily = {
        "child1": {"name": "Emil",   "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
        "child3": {"name": "Linus",  "year": 2011}
    }

혹은:

    child1 = {"name": "Emil", "year": 2004}
    child2 = {"name": "Tobias", "year": 2007}
    child3 = {"name": "Linus", "year": 2011}

    myfamily = {
        "child1": child1,
        "child2": child2,
        "child3": child3
    }
"""
# 파이썬 중첩 사전(Nested Dictionary)

# 방법 1
myfamily = {
    "child1": {"name": "Emil",   "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus",  "year": 2011}
}
print(myfamily)
# 결과 : {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
    
# 방법 2
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
# 결과 : {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

"""
중첩된 사전의 값 접근
----------------------
바깥 키 → 안쪽 키 순으로 접근:

    myfamily["child2"]["name"]   # "Tobias"


중첩된 사전 반복
-----------------
items()를 사용하여 전체 구조 순회:

    for key, obj in myfamily.items():
        print(key)
        for sub_key in obj:
            print(sub_key + ":", obj[sub_key])
"""
# 파이썬 중첩된 사전 값 접근 및 반복

myfamily = {
    "child1": {"name": "Emil",   "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus",  "year": 2011}
}
print(myfamily["child2"]["name"])   # Tobias
for key, obj in myfamily.items():
    print(key)
    for sub_key in obj:
        print(sub_key + ":", obj[sub_key])
# 결과 :
# Tobias
# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011

"""
사전(Dictionary) 메서드 요약
=============================

- clear()       : 모든 항목 삭제
- copy()        : 얕은 복사 반환
- fromkeys()    : 지정한 키들로 새 사전 생성 (같은 값 설정)
- get()         : 키에 해당하는 값 반환 (없으면 기본값)
- items()       : (키, 값) 튜플들의 뷰 반환
- keys()        : 키들의 뷰 반환
- pop()         : 지정한 키 삭제 및 값 반환
- popitem()     : 마지막으로 추가된 항목 삭제
- setdefault()  : 키가 있으면 값 반환, 없으면 넣고 그 값 반환
- update()      : 다른 dict/반복 가능한 객체로 키:값 갱신/추가
- values()      : 값들의 뷰 반환
"""
