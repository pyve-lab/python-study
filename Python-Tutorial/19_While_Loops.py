"""
📌 Python 루프(Loops)
=====================

Python에는 두 가지 기본 반복문이 있습니다:

1) while 루프  
2) for 루프

이 문서는 그 중 ‘while 루프’에 대해 설명합니다.
"""

"""
📌 while 루프란?
-----------------
while 루프는 **조건이 참(True)인 동안 반복해서 코드 블록을 실행**합니다.

형식:
    while 조건:
        실행할 코드
"""

"""
📌 기본 예제
-------------
i = 1
while i < 6:
    print(i)
    i += 1

설명:
- i 가 6보다 작은 동안 반복됨
- i를 증가시키지 않으면 무한 루프(infinite loop)가 됨
- 반복문 전에 변수 준비가 필요 (예: i = 1)
"""
# 파이썬 while 루프 기본 예제

i = 1
while i < 6:
    print(i)
    i += 1
# 결과 : 1 2 3 4 5

"""
📌 break 문
-----------
break 는 **조건이 여전히 참이어도** 강제로 루프를 종료합니다.

예:
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1

출력: 1, 2, 3  
3에서 break 되며 루프 종료
"""
# 파이썬 break 문

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# 결과 : 1 2 3

"""
📌 continue 문
---------------
continue 는 **현재 반복을 건너뛰고 다음 반복으로 넘어감**.

예:
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)

출력: 1, 2, 4, 5, 6  
(3일 때 print 건너뜀)
"""
# 파이썬 continue 문

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# 결과 : 1 2 4 5 6

"""
📌 while-else 문
-----------------
조건이 거짓(False)이 되어 루프가 “정상적으로 종료”되면 else 블록이 실행됩니다.

예:
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")

설명:
- i < 6 이 False가 되면서 else 실행
- break 로 종료된 경우에는 else 실행되지 않음
"""
# 파이썬 while-else 문

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# 결과 : 1 2 3 4 5 i is no longer less than 6

"""
📌 요약
-------
- while 조건: → 조건이 True 동안 반복
- break → 반복 즉시 종료
- continue → 현재 반복 건너뛰고 다음 반복 진행
- else → 루프가 “정상 종료”되었을 때 실행
- 무한 루프에 주의 (조건 변화 필수)

"""
