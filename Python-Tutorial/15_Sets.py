"""
📌 Python 세트(Set) 개념 정리
=============================

집합(Set)은 여러 항목을 하나의 변수에 저장하는 Python의 기본 컬렉션 데이터 타입 중 하나입니다.

Python의 4가지 컬렉션 타입:
- List       : 순서 O, 변경 가능, 중복 허용
- Tuple      : 순서 O, 변경 불가, 중복 허용
- Set        : 순서 X, 변경 불가(요소 자체는 수정 불가), 인덱스 없음, 중복 불가
- Dictionary : 순서 O, 변경 가능, 키 중복 불가

세트(Set)의 특징
----------------
1. 순서가 없음 (unordered)
2. 색인이 없음 (indexing 불가)
3. 중복 허용하지 않음
4. 요소(item)는 변경할 수 없지만 set 자체에는 추가/삭제 가능
5. 중괄호 {} 또는 set() 생성자 사용

예:
    thisset = {"apple", "banana", "cherry"}
    print(thisset)
"""


"""
📌 세트의 기본 특징
-------------------

✔ 순서 없음  
    - 출력 순서는 매번 달라질 수 있다.
✔ 요소 변경 불가  
    - 요소 자체는 수정할 수 없지만, 추가/삭제는 가능하다.
✔ 중복 없음  
    - 중복된 값은 자동으로 제거된다.

예:
    thisset = {"apple", "banana", "cherry", "apple"}
    print(thisset)  # apple 중복 제거

⚠ True == 1, False == 0 때문에 중복으로 처리됨.
"""
# 파이썬 세트 기본 특징

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # {'banana', 'cherry', 'apple'}

"""
📌 세트 길이 확인 (len)
------------------------

예:
    thisset = {"apple", "banana", "cherry"}
    print(len(thisset))
"""
# 파이썬 세트 길이 확인

thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # 3

"""
📌 다양한 데이터 타입 포함 가능
-------------------------------

예:
    set1 = {"abc", 34, True, 40, "male"}
"""
# 파이썬 다양한 데이터 타입 세트
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# 결과 : {34, 'male', True, 40, 'abc'}

"""
📌 set() 생성자
----------------

예:
    thisset = set(("apple", "banana", "cherry"))
    print(thisset)
"""
# 파이썬 set() 생성자

thisset = set(("apple", "banana", "cherry"))
print(thisset)  # {'banana', 'cherry', 'apple'}

"""
📌 세트 요소 접근
------------------

세트는 인덱싱이 불가하지만:

- for 반복문으로 순회 가능
- in 키워드로 포함 여부 확인 가능

예:
    for x in thisset:
        print(x)

    print("banana" in thisset)
    print("banana" not in thisset)
"""
# 파이썬 세트 요소 접근

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
print("banana" in thisset)      # True
print("banana" not in thisset)  # False 

"""
📌 항목 추가(add)
------------------

예:
    thisset.add("orange")
"""
# 파이썬 세트 항목 추가

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # {'banana', 'cherry', 'orange', 'apple'}

"""
📌 여러 항목 추가(update)
-------------------------

update()는 집합, 리스트, 튜플 등 "반복 가능한" 객체 모두 추가 가능.

예:
    thisset.update(["kiwi", "orange"])
    thisset.update(tropical_set)
"""
# 파이썬 세트 여러 항목 추가

thisset = {"apple", "banana", "cherry"}
thisset.update(["kiwi", "orange"])
print(thisset)  
# 결과 : {'banana', 'cherry', 'orange', 'kiwi', 'apple'}

"""
📌 항목 제거(remove, discard)
-----------------------------

remove("x")  
    → 요소가 없으면 에러 발생

discard("x")  
    → 요소가 없어도 에러 없음

pop()  
    → 임의의 요소 제거 (어떤 요소가 제거될지 알 수 없음)

clear()  
    → 전체 요소 삭제

del  
    → 세트 자체 삭제

예:
    thisset.remove("banana")
    thisset.discard("banana")
    x = thisset.pop()
    thisset.clear()
    del thisset
"""
# 파이썬 세트 항목 제거

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # {'cherry', 'apple'}

thisset.discard("banana")  # 에러 없음

x = thisset.pop()
print(x)         # 임의의 요소 출력
print(thisset)  # 남은 요소 출력    

thisset.clear()
print(thisset)  # set()

del thisset
# print(thisset)  # 오류 발생 (세트 자체가 삭제됨)

"""
📌 세트 반복(loop)
--------------------

예:
    for x in thisset:
        print(x)
"""
# 파이썬 세트 반복문

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# 결과 : apple banana cherry (순서 다를 수 있음)

"""
📌 세트 결합(Join)
-------------------

✔ union() 또는 | 연산자  
    - 두 세트의 모든 요소를 포함한 새 세트 반환

예:
    set3 = set1.union(set2)
    set3 = set1 | set2

여러 세트 결합도 가능:
    myset = set1 | set2 | set3 | set4
"""
# 파이썬 세트 결합

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # {'a', 1, 2, 3, 'c', 'b'}
set4 = set1 | set2
print(set4)  # {'a', 1, 2, 3, 'c', 'b'}

"""
📌 세트 + 다른 타입 결합 (union)
---------------------------------

union()은 튜플/리스트 등과도 결합 가능 → 결과는 세트

예:
    x = {"a", "b", "c"}
    y = (1, 2, 3)
    z = x.union(y)

⚠ | 연산자는 집합끼리만 결합 가능
"""
# 파이썬 세트 + 다른 타입 결합

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)  # {'a', 1, 2, 3, 'c', 'b'}

"""
📌 update()
------------

update()는 **원래 세트를 변경**함 (새 세트 반환 X)

예:
    set1.update(set2)
"""
# 파이썬 세트 update()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)  # {'a', 1, 2, 3, 'c', 'b'}

"""
📌 교집합(intersection)
------------------------

중복(공통) 요소만 유지

예:
    set3 = set1.intersection(set2)
    set3 = set1 & set2

intersection_update()  
    → 원래 세트를 변경

예:
    set1.intersection_update(set2)
"""
# 파이썬 세트 교집합

set1 = {"a", "b", "c", 1, 2}
set2 = {1, 2, 3, "a"}
set3 = set1.intersection(set2)
print(set3)  # {1, 'a'}
set1.intersection_update(set2)
print(set1)  # {1, 'a'}

"""
📌 차집합(difference)
----------------------

‘첫 번째 세트에는 있지만 두 번째 세트에는 없는 요소’만 반환

예:
    set3 = set1.difference(set2)
    set3 = set1 - set2

difference_update()  
    → 원래 세트를 변경
"""
# 파이썬 세트 차집합

set1 = {"a", "b", "c", 1, 2}
set2 = {1, 2, 3, "a"}
set3 = set1.difference(set2)
print(set3)  # {'c', 'b'}

"""
📌 대칭 차집합 (symmetric_difference)
--------------------------------------

두 세트 중 하나에만 존재하는 요소들(=공통 제외)

예:
    set3 = set1.symmetric_difference(set2)
    set3 = set1 ^ set2

symmetric_difference_update()  
    → 원래 세트를 변경
"""
# 파이썬 세트 대칭 차집합
set1 = {"a", "b", "c", 1, 2}
set2 = {1, 2, 3, "a"}
set3 = set1.symmetric_difference(set2)
print(set3)  # {'c', 3, 'b'}    
set1.symmetric_difference_update(set2)
print(set1)  # {'c', 3, 'b'}

"""
📌 파이썬 Frozenset
---------------------

frozenset = "불변(immutable) 집합"

✔ 변경 불가  
✔ 중복 없음  
✔ 순서 없음  
✔ set의 비변형 연산(교집합, 합집합 등)은 모두 가능

예:
    x = frozenset({"apple", "banana", "cherry"})
    print(type(x))
"""
# 파이썬 Frozenset

x = frozenset({"apple", "banana", "cherry"})
print(type(x))  # <class 'frozenset'>

"""
📌 Set 전체 메서드 요약
-----------------------

add()                      항목 추가
clear()                    모든 항목 삭제
copy()                     얕은 복사
difference() (-)           차집합 반환
difference_update() (-=)   차집합으로 원본 변경
discard()                  항목 삭제(없어도 에러 없음)
intersection() (&)         교집합 반환
intersection_update() (&=) 교집합으로 원본 변경
isdisjoint()               교집합 여부 확인
issubset() (<=) (<)        부분집합인지 검사
issuperset() (>=) (>)      상위집합인지 검사
pop()                      임의 항목 제거
remove()                   항목 제거(없으면 에러)
symmetric_difference() (^) 대칭 차집합 반환
symmetric_difference_update() (^=) 원본 변경
union() (|)                합집합 반환
update() (|=)              합집합으로 원본 변경
"""
