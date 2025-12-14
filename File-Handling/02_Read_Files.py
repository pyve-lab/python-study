"""
==========================================================
📌 서버에서 파일 열기 (File Reading)
==========================================================

파이썬에서는 open() 함수로 파일을 열 수 있으며,
반환된 파일 객체를 사용해 read(), readline() 등으로 내용을 읽는다.

예제 파일 내용 (demofile.txt):

    Hello! Welcome to demofile.txt
    This file is for testing purposes.
    Good Luck!
"""

"""
==========================================================
📌 1. 기본 파일 열기 + 전체 읽기
==========================================================

f = open("demofile.txt")
print(f.read())

✔ open() → 파일 객체 반환  
✔ read() → 파일 전체 내용을 문자열로 반환  
"""
# 파이썬 파일 열기 및 전체 읽기 예시

f = open("demofile.txt")  # 읽기 모드로 파일 열기 -> 파일 위치 : 현재 프로젝트의 root (python-study)
print(f.read())  
# 파일 전체 내용 출력
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

"""
==========================================================
📌 2. 특정 경로의 파일 열기
==========================================================

파일이 다른 폴더에 있을 경우 절대경로/상대경로를 지정한다.

f = open("D:\\myfiles\\welcome.txt")
print(f.read())

✔ Windows에서는 백슬래시(\)를 두 번 쓰거나 r"경로" 사용
"""
# 파이썬 특정 경로의 파일 열기 예시

f = open("c:\\Users\\권나현\\Desktop\\python-study\\file_test\\demofile.txt")  # 절대경로로 파일 열기
print(f.read())
# 파일 전체 내용 출력
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

"""
==========================================================
📌 3. with 문으로 파일 열기 (추천 방식)
==========================================================

with open("demofile.txt") as f:
    print(f.read())

✔ with 블록 종료 시 자동으로 파일 close  
✔ 예외가 발생해도 파일이 정상적으로 닫히므로 매우 안전  
✔ 권장되는 파일 처리 방식
"""
# 파이썬 with 문으로 파일 열기 예시

with open("demofile.txt") as f:
    print(f.read())

# 파일 전체 내용 출력
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!
"""
==========================================================
📌 4. 파일 닫기 — close()
==========================================================

with 문을 사용하지 않을 때는 반드시 close() 호출해야 한다.

f = open("demofile.txt")
print(f.readline())
f.close()

✔ 파일을 닫지 않으면 버퍼링 문제로 변경 내용이 저장되지 않을 수도 있음
✔ 자주 발생하는 실수 → 반드시 close() 또는 with 사용
"""
# 파이썬 파일 닫기 예시

f = open("demofile.txt")
print(f.readline())  # 첫 번째 줄 읽기
f.close()            # 파일 닫기

# 결과 :
# Hello! Welcome to demofile.txt

"""
==========================================================
📌 5. read(n) — 원하는 문자 수만 읽기
==========================================================

기본적으로 read()는 전체 파일을 읽지만,  
문자 수를 지정하면 그만큼만 읽을 수 있다.

with open("demofile.txt") as f:
    print(f.read(5))   # 처음 5글자만 읽음

✔ 부분 읽기 가능  
✔ large file 다룰 때 매우 유용
"""
# 파이썬 read(n) 예시

with open("demofile.txt") as f:
    print(f.read(5))   # 처음 5글자만 읽음

# 결과 :
# Hello
"""
==========================================================
📌 6. readline() — 한 줄씩 읽기
==========================================================

with open("demofile.txt") as f:
    print(f.readline())   # 첫 번째 줄
    print(f.readline())   # 두 번째 줄

✔ 호출할 때마다 다음 줄을 반환  
✔ 줄바꿈(\n) 포함하여 반환됨
"""
# 파이썬 readline() 예시

with open("demofile.txt") as f:
    print(f.readline())   # 첫 번째 줄
    print(f.readline())   # 두 번째 줄

# 결과 :
# Hello! Welcome to demofile.txt
# This file is for testing purposes.

"""
==========================================================
📌 7. 파일을 한 줄씩 순회 (for 루프)
==========================================================

with open("demofile.txt") as f:
    for x in f:
        print(x)

✔ 메모리를 적게 사용  
✔ 대용량 파일을 읽을 때 가장 효율적인 방식  
✔ 한 줄씩 순회하면서 자동으로 읽어옴
"""
# 파이썬 파일을 한 줄씩 순회 예시

with open("demofile.txt") as f:
    for x in f:
        print(x)

# 결과 :
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

"""
==========================================================
📌 정리
----------------------------------------------------------
- open() 으로 파일을 열고, read(), readline(), for 루프로 내용 읽음
- with 문을 사용하면 자동으로 파일이 닫혀 안전함
- read(n) → 처음 n개의 문자 읽기
- readline() → 한 줄씩 읽기
- for 문 → 파일 전체를 한 줄씩 순회
- 파일 사용 후 close()는 필수 (단, with 사용 시 자동 처리)

"""
