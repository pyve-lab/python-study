"""
📌 Python for 루프
==================

Python의 for 루프는 시퀀스(리스트, 튜플, 사전, 집합, 문자열 등)를  
**하나씩 반복(iterate)** 하며 각 요소에 접근할 때 사용됩니다.

다른 언어의 일반적인 for-loop(카운터 기반)보다  
Python의 for는 ‘반복자(iterator)’에 더 가까운 방식입니다.
"""

"""
📌 기본 for 루프
-----------------

예:
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

특징:
- 인덱스 변수를 따로 만들 필요 없음
- 시퀀스의 각 항목을 직접 꺼내 반복함
"""
# 파이썬 기본 for 루프

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    
# 결과 : apple banana cherry

"""
📌 문자열 반복
-----------------
문자열도 반복 가능한 객체(iterable) → 문자 하나씩 반복 가능

예:
    for x in "banana":
        print(x)
"""
# 파이썬 문자열 반복
for x in "banana":
    print(x)
# 결과 : b a n a n a

"""
===================================
📌 break — 루프 강제 종료
===================================

break 는 반복을 즉시 끝냄.

예:
    for x in fruits:
        print(x)
        if x == "banana":
            break

break가 print보다 먼저 오면:

예:
    for x in fruits:
        if x == "banana":
            break
        print(x)

출력: apple
"""
# 파이썬 break 문

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# 결과 : apple banana

for x in fruits:
    if x == "banana":
        break
    print(x)
# 결과 : apple

"""
===================================
📌 continue — 현재 반복 건너뛰기
===================================

continue 는 현재 반복만 스킵하고 다음 반복으로 이동.

예:
    for x in fruits:
        if x == "banana":
            continue
        print(x)

출력: apple, cherry
"""
# 파이썬 continue 문

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# 결과 : apple cherry

"""
===================================
📌 range() 함수
===================================

range()는 숫자 시퀀스를 생성하는 함수.

형식:
    range(끝)
    range(시작, 끝)
    range(시작, 끝, 증가값)

예:
    for x in range(6):
        print(x)

출력: 0,1,2,3,4,5  (6은 포함되지 않음)


📌 시작 값을 지정할 때
예:
    for x in range(2, 6):
        print(x)
출력: 2,3,4,5


📌 증가값(step) 지정
예:
    for x in range(2, 30, 3):
        print(x)
출력: 2,5,8,...,29
"""
# 파이썬 range() 함수

for x in range(6):
    print(x)
# 결과 : 0 1 2 3 4 5

for x in range(2, 6):
    print(x)
# 결과 : 2 3 4 5

for x in range(2, 30, 3):
    print(x)
# 결과 : 2 5 8 11 14 17 20 23 26 29

"""
===================================
📌 for 루프의 else
===================================

for 문이 정상적으로 종료될 때(= break 없이 종료) 실행되는 블록.

예:
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")

⚠ break로 종료되면 else 실행되지 않음

예:
    for x in range(6):
        if x == 3:
            break
        print(x)
    else:
        print("Finished!")   # 실행되지 않음
"""
# 파이썬 for-else 문

for x in range(6):
    print(x)
else:
    print("Finally finished!")
# 결과 : 0 1 2 3 4 5 Finally finished!

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finished!")   # 실행되지 않음
# 결과 : 0 1 2

"""
===================================
📌 중첩 루프 (Nested Loops)
===================================

루프 안에 루프가 있을 수 있음.  
“내부 루프(inner)”는 “외부 루프(outer)”의 각 반복마다 전체 반복 수행.

예:
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

출력:
    red apple
    red banana
    red cherry
    big apple
    ...
"""
# 파이썬 중첩 루프

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# 결과 :
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

"""
===================================
📌 pass 문
===================================

for 문은 비어 있을 수 없음 → 비워두고 싶다면 pass 사용.

예:
    for x in [0, 1, 2]:
        pass
"""
# 파이썬 pass 문

for x in [0, 1, 2]:
    pass
# 결과 : (아무 출력 없음)

"""
===================================
📌 요약
===================================

- for 는 시퀀스를 반복(iterate)하는 데 사용됨
- 문자열도 iterable
- break → 반복 즉시 종료
- continue → 현재 반복 건너뛰기
- range() → 숫자 반복 생성
- for-else → 정상 종료 시 실행
- 중첩 for 가능
- pass → 빈 블록 처리용

"""
