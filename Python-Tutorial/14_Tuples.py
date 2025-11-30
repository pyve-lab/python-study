"""
📌 튜플(Tuple) 개념 정리
========================

튜플은 여러 항목을 하나의 변수에 저장하는 Python의 기본 자료형 중 하나입니다.

Python에는 네 가지 컬렉션 데이터 타입이 있으며 각각은 다음과 같은 특징을 가집니다:
- 리스트(list): 순서 O, 변경 가능, 중복 허용
- 튜플(tuple): 순서 O, 변경 불가능(immutable), 중복 허용
- 셋(set): 순서 X, 변경 가능, 중복 불가
- 딕셔너리(dict): 순서 O, 변경 가능, 중복 없음(Python 3.7+)

튜플의 특징
-----------
1. 순서가 있다 (ordered)
2. 변경할 수 없다 (immutable)
3. 중복 값을 허용한다 (duplicate allowed)
4. 대괄호가 아닌 **소괄호 ()** 로 작성된다

예:
    mytuple = ("apple", "banana", "cherry")
"""
# 파이썬 튜플 개념 정리

mytuple = ("apple", "banana", "cherry")
print(mytuple)
# 결과 : ('apple', 'banana', 'cherry')

"""
📌 튜플 생성
------------

thistuple = ("apple", "banana", "cherry")
print(thistuple)

튜플 항목은 인덱싱되며 첫 번째 요소는 index 0이다.
"""
# 파이썬 튜플 생성

thistuple = ("apple", "banana", "cherry")
print(thistuple)
# 결과 : ('apple', 'banana', 'cherry')

"""
📌 중복 허용
------------

튜플은 같은 값을 여러 번 포함할 수 있다.

예:
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
"""
# 파이썬 튜플 중복 허용

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# 결과 : ('apple', 'banana', 'cherry', 'apple', 'cherry')

"""
📌 튜플 길이 확인 (len)
----------------------

len() 함수를 사용해 항목 개수를 확인한다.

예:
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))
"""
# 파이썬 튜플 길이 확인

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# 결과 : 3

"""
📌 항목이 하나인 튜플 만들기
-----------------------------

중요! 항목 뒤에 **쉼표(,)** 를 붙여야 튜플로 인식된다.

예:
    thistuple = ("apple",)
    print(type(thistuple))   # tuple

    thistuple = ("apple")
    print(type(thistuple))   # str
"""
# 파이썬 항목 하나인 튜플

thistuple = ("apple",)
print(type(thistuple))   # tuple
thistuple = ("apple")
print(type(thistuple))   # str

"""
📌 다양한 데이터 타입 포함 가능
-------------------------------

예:
    tuple1 = ("abc", 34, True, 40, "male")
"""
# 파이썬 다양한 데이터 타입 튜플

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
# 결과 : ('abc', 34, True, 40, 'male')

"""
📌 tuple() 생성자
----------------

예:
    thistuple = tuple(("apple", "banana", "cherry"))
"""
# 파이썬 tuple() 생성자

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
# 결과 : ('apple', 'banana', 'cherry')

"""
📌 튜플 요소 접근
------------------

대괄호 [ ] 사용

예:
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])   # banana
"""
# 파이썬 튜플 요소 접근

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])   # banana
# 결과 : banana

"""
📌 음수 인덱싱
--------------

-1 → 마지막
-2 → 뒤에서 두 번째

예:
    print(thistuple[-1])
"""
# 파이썬 음수 인덱싱

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])   # cherry
# 결과 : cherry

"""
📌 인덱스 범위 슬라이싱
-----------------------

예:
    thistuple[2:5]
    thistuple[:4]
    thistuple[2:]
    thistuple[-4:-1]
"""
# 파이썬 튜플 인덱스 범위 슬라이싱

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])    # ('cherry', 'orange', 'kiwi')
print(thistuple[:4])     # ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:])     # ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1])  # ('orange', 'kiwi', 'melon')

"""
📌 항목 존재 여부 확인
-----------------------

예:
    if "apple" in thistuple:
        print("Yes!")
"""
# 파이썬 튜플 항목 존재 여부 확인

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes!")
# 결과 : Yes!

"""
📌 튜플은 변경할 수 없다 (immutable)
-----------------------------------

단, 리스트로 변환 → 수정 → 다시 튜플로 변환하는 우회 방법은 가능하다.

예:
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
"""
# 파이썬 튜플 변경 불가 우회 방법

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# 결과 : ('apple', 'kiwi', 'cherry')

"""
📌 항목 추가하는 두 가지 방법
------------------------------

1) 리스트로 변환 후 append()
2) 다른 튜플을 더해서 추가

예:
    thistuple += ("orange",)
"""
# 파이썬 튜플 항목 추가

thistuple = ("apple", "banana", "cherry")
thistuple += ("orange",)
print(thistuple)
# 결과 : ('apple', 'banana', 'cherry', 'orange')

"""
📌 항목 제거 (삭제)
-------------------

튜플 자체에서는 삭제 불가.
→ 리스트 변환 후 remove()

예:
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)

튜플 전체 삭제는 del 사용
"""
# 파이썬 튜플 항목 제거

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# 결과 : ('banana', 'cherry')

"""
📌 튜플 패킹 & 언패킹
---------------------

Packing:
    fruits = ("apple", "banana", "cherry")

Unpacking:
    (green, yellow, red) = fruits

* 사용하여 나머지를 리스트로 받을 수도 있다:
    (a, b, *rest) = fruits
"""
# 파이썬 튜플 패킹 & 언패킹

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)   # apple
print(yellow)  # banana
print(red)     # cherry

"""
📌 튜플 반복문
---------------

for 문:
    for x in thistuple:
        print(x)

인덱스 기반:
    for i in range(len(thistuple)):
        print(thistuple[i])

while 문:
    i = 0
    while i < len(thistuple):
        print(thistuple[i])
        i += 1
"""
# 파이썬 튜플 반복문

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
        print(thistuple[i])

while i < len(thistuple):
    print(thistuple[i])
    i += 1
# 결과 :
# apple
# banana
# cherry

"""
📌 튜플 결합 및 곱셈
---------------------

결합:
    tuple3 = tuple1 + tuple2

곱셈:
    fruits * 2
"""
# 파이썬 튜플 결합 및 곱셈

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # ('a', 'b', 'c', 1, 2, 3)
fruits = ("apple", "banana", "cherry")  
print(fruits * 2)  # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

"""
📌 튜플 메서드
--------------

count() : 특정 값이 몇 번 등장하는지 반환
index() : 값이 처음 나타난 위치 반환
"""
# 파이썬 튜플 메서드

thistuple = (1, 2, 3, 2, 2, 4, 5)
print(thistuple.count(2))   # 3
print(thistuple.index(4))    # 5
