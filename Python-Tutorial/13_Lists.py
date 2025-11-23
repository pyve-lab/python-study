"""
📌 파이썬 리스트 (List)
========================

리스트는 하나의 변수에 여러 항목을 저장하는 데 사용됩니다.
Python의 4가지 컬렉션 자료형 중 하나이며, 나머지는 다음과 같습니다:

- 튜플 (tuple)
- 세트 (set)
- 딕셔너리 (dict)

리스트는 **대괄호 [ ]** 를 사용하여 생성합니다.

예:
    thislist = ["apple", "banana", "cherry"]
    print(thislist)
"""

"""
=====================================
📌 리스트의 특징
=====================================

1) 정렬됨 (Ordered)
---------------------
리스트는 요소가 삽입된 순서를 기억합니다.
첫 번째 항목은 index 0, 두 번째는 index 1 …

새 항목을 추가하면 리스트의 **끝에** 추가됩니다.

※ 순서를 변경하는 메서드(sort 등)는 예외적으로 순서를 변경합니다.

2) 변경 가능함 (Mutable)
--------------------------
리스트는 생성 후에도 값 변경, 추가, 삭제가 가능합니다.

3) 중복 허용 (Allows Duplicates)
----------------------------------
리스트는 인덱스로 관리되기 때문에 동일한 값을 여러 번 넣을 수 있습니다.

예:
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)

4) 다양한 데이터 타입 포함 가능
----------------------------------
리스트는 문자열뿐 아니라 정수, 부울, 여러 타입을 포함할 수 있습니다.

예:
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]

    mixed = ["abc", 34, True, 40, "male"]
"""
# 파이썬 리스트 특징

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
mixed = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(mixed)
# 결과 :
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]
# ['abc', 34, True, 40, 'male']


"""
=====================================
📌 리스트 길이 (len)
=====================================

len() 함수를 사용하여 리스트 항목 수를 확인할 수 있습니다.

예:
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))
"""
# 파이썬 리스트 길이

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# 결과 : 3

"""
=====================================
📌 리스트의 데이터 유형 (type)
=====================================

리스트는 Python에서 <class 'list'> 객체입니다.

예:
    mylist = ["apple", "banana", "cherry"]
    print(type(mylist))   # <class 'list'>
"""
# 파이썬 데이터 유형

mylist = ["apple", "banana", "cherry"]
print(type(mylist))   # <class 'list'>
# 결과 : <class 'list'>

"""
=====================================
📌 list() 생성자
=====================================

list() 생성자를 사용해 리스트를 생성할 수도 있습니다.

예:
    thislist = list(("apple", "banana", "cherry"))
    print(thislist)
(주의: 두 개의 괄호를 사용하는 것에 주의)
"""
# 파이썬 생성자

thislist = list(("apple", "banana", "cherry"))
print(thislist)
# 결과 : ['apple', 'banana', 'cherry']

"""
=====================================
📌 파이썬 컬렉션(배열) 종류 요약
=====================================

Python에는 4가지 주요 컬렉션 데이터 타입이 있습니다:

1) 리스트(list)
----------------
- 정렬됨 (Ordered)
- 변경 가능 (Mutable)
- 중복 허용

2) 튜플(tuple)
----------------
- 정렬됨 (Ordered)
- 변경 불가 (Immutable)
- 중복 허용

3) 세트(set)
--------------
- 정렬되지 않음 (Unordered)
- 변경 가능하지만, 항목 자체는 변경 불가
- 인덱싱 불가
- 중복 불가

4) 딕셔너리(dict)
--------------------
- 정렬됨 (Python 3.7+ 기준)
- 변경 가능 (Mutable)
- 중복 키 없음 (값은 중복 가능)

※ Python 3.6 이하에서는 딕셔너리가 정렬되지 않았음.

적절한 컬렉션 타입 선택은 코드 구조, 효율성, 가독성, 안전성 등을 크게 향상시킵니다.
"""

"""
📌 리스트 항목 접근 (Access List Items)
=======================================

리스트는 인덱싱(Indexing)이 가능하며,
대괄호 [ ] 안에 인덱스 번호를 넣어 특정 항목에 접근할 수 있습니다.

예 — 두 번째 항목 출력:
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])   # banana

※ 첫 번째 항목의 인덱스는 0입니다.
"""
# 파이썬 리스트 항목 접근

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# 결과 : banana

"""
=====================================
📌 음수 인덱싱 (Negative Indexing)
=====================================

음수 인덱싱을 사용하면 리스트의 끝에서부터 항목에 접근합니다.

    -1 → 마지막 항목
    -2 → 뒤에서 두 번째 항목

예 — 마지막 항목 출력:
    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])   # cherry
"""
# 파이썬 리스트 음수 인덱싱

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# 결과 : cherry

"""
=====================================
📌 인덱스 범위 (List Slicing)
=====================================

[start : end] 슬라이싱을 사용하여 여러 항목을 잘라 새로운 리스트를 반환합니다.
end 인덱스는 포함되지 않습니다.

예 — 3번째~5번째 항목 가져오기:
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])   # ['cherry', 'orange', 'kiwi']
"""
# 파이썬 리스트 인덱스 범위

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# 결과 : ['cherry', 'orange', 'kiwi']

"""
📌 시작 인덱스 생략
----------------------
처음부터 특정 위치까지 가져옵니다.

예:
    print(thislist[:4])
    # ['apple', 'banana', 'cherry', 'orange']
"""
# 파이썬 리스트 시작 인덱스 생략

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# 결과 : ['apple', 'banana', 'cherry', 'orange']

"""
📌 끝 인덱스 생략
----------------------
특정 위치부터 리스트 끝까지 가져옵니다.

예:
    print(thislist[2:])
    # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
"""
# 파이썬 리스트 끝 인덱스 생략

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# 결과 : ['cherry', 'orange', 'kiwi', 'melon', 'mango']

"""
=====================================
📌 음수 인덱스 슬라이싱 (Negative Range)
=====================================

리스트의 끝에서부터 범위를 지정할 수도 있습니다.

예 — -4에서 -1까지(단, -1은 포함되지 않음):
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])
    # ['orange', 'kiwi', 'melon']
"""
# 파이썬 리스트 음수 인덱스 슬라이싱

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# 결과 : ['orange', 'kiwi', 'melon']

"""
=====================================
📌 항목 존재 여부 확인 (in 키워드)
=====================================

리스트에 특정 값이 있는지 확인하려면 in 키워드를 사용합니다.

예:
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

"""
# 파이썬 리스트 항목 존재 여부 확인

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
# 결과 : Yes, 'apple' is in the fruits list

"""
📌 리스트 항목 값 변경 (Changing List Items)
============================================

리스트는 변경 가능한 자료형이므로,
특정 항목의 값을 인덱스를 이용해 변경할 수 있습니다.

예 — 두 번째 항목 변경:
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)
    # ['apple', 'blackcurrant', 'cherry']
"""
# 파이썬 리스트 항목 값 변경

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# 결과 : ['apple', 'blackcurrant', 'cherry']

"""
=====================================
📌 리스트 항목 범위 변경 (Change Range of Items)
=====================================

[start : end] 범위를 지정하여 여러 항목을 한 번에 바꿀 수 있습니다.

예 — 'banana', 'cherry' → 'blackcurrant', 'watermelon':
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)
"""
# 파이썬 리스트 항목 범위 변경

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# 결과 : ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

"""
📌 더 많은 항목으로 교체할 때
--------------------------------
바꾸는 항목보다 새 항목이 많으면 리스트 길이가 늘어납니다.

예 — 1개의 값 → 2개의 값으로 변경:
    thislist = ["apple", "banana", "cherry"]
    thislist[1:2] = ["blackcurrant", "watermelon"]
    print(thislist)
    # ['apple', 'blackcurrant', 'watermelon', 'cherry']
"""
# 파이썬 리스트 더 많은 항목으로 교체

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# 결과 : ['apple', 'blackcurrant', 'watermelon', 'cherry']

"""
📌 더 적은 항목으로 교체할 때
--------------------------------
바뀌는 항목보다 새 항목이 적으면 리스트 길이가 줄어듭니다.

예 — 두 항목 → 한 항목:
    thislist = ["apple", "banana", "cherry"]
    thislist[1:3] = ["watermelon"]
    print(thislist)
    # ['apple', 'watermelon']
"""
# 파이썬 리스트 더 적은 항목으로 교체

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# 결과 : ['apple', 'watermelon']

"""
=====================================
📌 리스트 항목 삽입 (Insert Items)
=====================================

기존 값을 덮어쓰지 않고 새로운 값을 삽입하려면 insert() 메서드를 사용합니다.

insert(index, value)

예 — 2번 인덱스에 "watermelon" 삽입:
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist)
    # ['apple', 'banana', 'watermelon', 'cherry']
"""
# 파이썬 리스트 항목 삽입

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# 결과 : ['apple', 'banana', 'watermelon', 'cherry']

"""
📌 리스트(List) — 항목 추가 / 제거 / 반복 / 리스트 컴프리헨션 / 정렬
=====================================================================

====================================================
📍 1. 항목 추가 (Add Items)
====================================================

append() — 리스트 끝에 항목 추가
--------------------------------
예:
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)
    # ['apple', 'banana', 'cherry', 'orange']
"""
# 파이썬 리스트 항목 추가

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# 결과 : ['apple', 'banana', 'cherry', 'orange']

"""
insert() — 특정 위치에 항목 삽입
---------------------------------
예:
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)
    # ['apple', 'orange', 'banana', 'cherry']
"""
# 파이썬 리스트 특정 위치에 항목 삽입

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# 결과 : ['apple', 'orange', 'banana', 'cherry']

"""
extend() — 다른 리스트(또는 반복 가능한 객체)를 확장하여 추가
----------------------------------------------------------------
예 — 리스트로 확장:
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)

예 — 튜플 요소 추가:
    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)
    print(thislist)
"""
# 파이썬 리스트 확장

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# 결과 : ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# 결과 : ['apple', 'banana', 'cherry', 'kiwi', 'orange']

"""
====================================================
📍 2. 항목 제거 (Remove Items)
====================================================

remove() — 특정 값을 가진 첫 번째 항목 제거
--------------------------------------------
예:
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")

중복일 경우 첫 번째만 제거:
    thislist = ["apple", "banana", "cherry", "banana"]
    thislist.remove("banana")


pop() — 특정 인덱스 제거 (미지정 시 마지막 항목 제거)
-----------------------------------------------------
예:
    thislist.pop(1)
    thislist.pop()     # 마지막 항목 제거
"""
# 파이썬 리스트 항목 제거

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# 결과 : ['apple', 'cherry']

thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)
# 결과 : ['apple', 'cherry', 'banana']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# 결과 : ['apple', 'cherry']

thislist.pop()
print(thislist)
# 결과 : ['apple']

"""
del — 인덱스 제거 또는 리스트 전체 삭제
------------------------------------------
예:
    del thislist[0]
    del thislist      # 전체 리스트 삭제
"""
# 파이썬 리스트 del

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# 결과 : ['banana', 'cherry']

del thislist
# 결과 : thislist 변수가 삭제됨

"""
clear() — 리스트 비우기(리스트는 유지)
---------------------------------------
예:
    thislist.clear()
    print(thislist)   # []
"""
# 파이썬 리스트 비우기

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# 결과 : []

"""
====================================================
📍 3. 리스트 반복 (Loop Through a List)
====================================================

for 문으로 반복:
-------------------
예:
    for x in thislist:
        print(x)
"""
# 파이썬 리스트 for 문 반복
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# 결과 :
# apple
# banana
# cherry

"""
인덱스 기반 반복(range + len):
------------------------------
예:
    for i in range(len(thislist)):
        print(thislist[i])
"""
# 파이썬 리스트 인덱스 기반 반복

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# 결과 :
# apple
# banana
# cherry

"""
while 문으로 반복:
-------------------
예:
    i = 0
    while i < len(thislist):
        print(thislist[i])
        i += 1
"""
# 파이썬 리스트 while 문 반복

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
# 결과 :
# apple
# banana
# cherry

"""
리스트 컴프리헨션으로 반복 출력:
--------------------------------
예:
    [print(x) for x in thislist]
"""
# 파이썬 리스트 컴프리헨션 반복 출력

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# 결과 :
# apple
# banana
# cherry

"""
====================================================
📍 4. 리스트 컴프리헨션 (List Comprehension)
====================================================

리스트 컴프리헨션 기본 형태:
    newlist = [expression for item in iterable if condition]

조건을 포함한 간단 예:
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)

조건 없는 버전:
    newlist = [x for x in fruits]

range() 와 함께 사용:
    newlist = [x for x in range(10)]
    newlist = [x for x in range(10) if x < 5]

표현식 조작:
    newlist = [x.upper() for x in fruits]
    newlist = ['hello' for x in fruits]

조건을 포함한 표현식:
    newlist = [x if x != "banana" else "orange" for x in fruits]
"""
# 파이썬 리스트 컴프리헨션

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# 결과 : ['apple', 'banana', 'mango']

newlist = [x for x in fruits]
print(newlist)
# 결과 : ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
print(newlist)
# 결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist)
# 결과 : [0, 1, 2, 3, 4]

newlist = [x.upper() for x in fruits]
print(newlist)
# 결과 : ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]
print(newlist)
# 결과 : ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# 결과 : ['apple', 'orange', 'cherry', 'kiwi', 'mango']

"""
====================================================
📍 5. 리스트 정렬 (Sort Lists)
====================================================

sort() — 기본 오름차순 정렬
----------------------------
예 — 문자열:
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()

예 — 숫자:
    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
"""
# 파이썬 리스트 정렬

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# 결과 : ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# 결과 : [23, 50, 65, 82, 100]

"""
내림차순 정렬(reverse=True):
------------------------------
예:
    thislist.sort(reverse=True)
"""
# 파이썬 리스트 내림차순 정렬

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
# 결과 : [100, 82, 65, 50, 23]

"""
====================================================
📍 6. 사용자 정의 정렬 (Custom Sort)
====================================================

key 매개변수를 사용하여 정렬 기준 지정
-----------------------------------------
예 — 숫자가 50에 얼마나 가까운지 기준으로 정렬:
    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
"""
# 파이썬 리스트 사용자 정의 정렬

def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
# 결과 : [50, 65, 23, 82, 100]

"""
====================================================
📍 7. 대소문자 구분 없는 정렬
====================================================

대소문자를 구분하면 대문자가 먼저 정렬되므로 예기치 않은 순서 발생.

해결 — str.lower 를 key 로 사용:
    thislist.sort(key=str.lower)
"""
# 파이썬 리스트 대소문자 구분 없는 정렬

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
# 결과 : ['banana', 'cherry', 'Kiwi', 'Orange']

"""
====================================================
📍 8. 리스트 반전 (Reverse)
====================================================

reverse() — 현재 순서 반대로 정렬
----------------------------------
예:
    thislist.reverse()
    print(thislist)

"""
# 파이썬 리스트 반전

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# 결과 : ['cherry', 'Kiwi', 'Orange', 'banana']

"""
📌 리스트 복사 (Copy Lists)
============================

리스트는 mutable(변경 가능)한 객체이므로,
단순히  list2 = list1  로 복사하면 두 변수가 같은 객체를 가리킵니다.
즉, list2 를 변경하면 list1 도 함께 변경됩니다.

정상적인 ‘복사본’을 만들려면 아래 방법 중 하나를 사용해야 합니다.


1) copy() 메서드 사용
----------------------
예:
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
"""
# 파이썬 리스트 복사 copy() 메서드

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# 결과 : ['apple', 'banana', 'cherry']

"""
2) list() 생성자 사용
----------------------
예:
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)
"""
# 파이썬 리스트 복사 list() 생성자

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# 결과 : ['apple', 'banana', 'cherry']

"""
3) 슬라이싱 연산자 [:] 사용
-----------------------------
예:
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist[:]
    print(mylist)
"""
# 파이썬 리스트 복사 슬라이싱 연산자

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
# 결과 : ['apple', 'banana', 'cherry']

"""
====================================================
📌 두 개의 리스트 결합 (Join Lists)
====================================================

1) + 연산자 사용 (가장 간단한 방법)
-------------------------------------
예:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)
"""
# 파이썬 리스트 결합 + 연산자

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# 결과 : ['a', 'b', 'c', 1, 2, 3]

"""
2) append() 를 이용해 list2 요소를 하나씩 list1에 추가
--------------------------------------------------------
예:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    for x in list2:
        list1.append(x)

    print(list1)
"""
# 파이썬 리스트 결합 append() 사용

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
# 결과 : ['a', 'b', 'c', 1, 2, 3]

"""
3) extend() 사용 (가장 정석적인 리스트 결합)
-----------------------------------------------
extend() 는 다른 리스트 또는 반복 가능한(iterable) 객체를 확장하여 현재 리스트 끝에 추가합니다.

예:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list1.extend(list2)
    print(list1)
"""
# 파이썬 리스트 결합 extend() 사용

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# 결과 : ['a', 'b', 'c', 1, 2, 3]

"""
====================================================
📌 리스트 메서드 전체 요약 (List Methods)
====================================================

아래는 Python 리스트에서 사용 가능한 주요 내장 메서드들입니다:

    append()   → 리스트 끝에 항목 추가
    clear()    → 모든 요소 제거
    copy()     → 리스트의 얕은 복사본 반환
    count()    → 특정 값의 등장 횟수 반환
    extend()   → iterable의 요소를 리스트 끝에 추가
    index()    → 특정 값이 처음 나타나는 인덱스 반환
    insert()   → 지정한 위치에 항목 삽입
    pop()      → 지정된 인덱스 요소 제거 (미지정 시 마지막 요소)
    remove()   → 특정 값을 가진 첫 번째 요소 제거
    reverse()  → 리스트 순서 뒤집기
    sort()     → 리스트 정렬

"""
