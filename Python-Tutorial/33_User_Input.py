"""
============================================================
📌 Python 사용자 입력 (input) 요약
============================================================

● input() 함수는 사용자에게 입력을 받기 위해 사용됨.
● input() 실행 시 프로그램이 잠시 멈추고 사용자의 입력을 기다림.
● input()의 반환값은 항상 "문자열(str)" 형태.
"""

"""
============================================================
📌 1. 기본 입력
============================================================

print("Enter your name:")
name = input()
print(f"Hello {name}")

# input() → 사용자 입력 대기
# 입력 후 다음 줄 실행
"""
# 파이썬 기본 입력 예제

print("Enter your name:")
name = input()
print(f"Hello {name}")
# 결과 :
# Enter your name:
# Happy
# Hello Happy

"""
============================================================
📌 2. 프롬프트(메시지) 넣기
============================================================

name = input("Enter your name: ")
print(f"Hello {name}")

# 같은 줄에 안내 메시지를 표시한 상태로 입력받기 가능
"""
# 파이썬 프롬프트 메시지 입력 예제

name = input("Enter your name: ")
print(f"Hello {name}")
# 결과 :
# Enter your name: Happy
# Hello Happy

"""
============================================================
📌 3. 여러 입력 받기
============================================================

name = input("Enter your name: ")
fav1 = input("Favorite animal: ")
fav2 = input("Favorite color: ")
fav3 = input("Favorite number: ")

print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
"""
# 파이썬 여러 입력 받기 예제

name = input("Enter your name: ")
fav1 = input("Favorite animal: ")
fav2 = input("Favorite color: ")
fav3 = input("Favorite number: ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
# 결과 :
# Enter your name: Happy
# Favorite animal: dog
# Favorite color: brown
# Favorite number: 4
# Do you want a brown dog with 4 legs?

"""
============================================================
📌 4. 숫자 입력 → 꼭 형변환 필요
============================================================

● input()의 결과는 항상 문자열이므로  
● 숫자로 계산하려면 int() 또는 float() 변환 필요

예:
    x = input("Enter a number: ")
    y = math.sqrt(float(x))
    print(y)
"""
# 파이썬 숫자 입력 및 변환 예제

import math
x = input("Enter a number: ")
y = math.sqrt(float(x))
print(y)
# 결과 :
# Enter a number: 25
# 5.0

"""
============================================================
📌 5. 입력 검증 (Validation)
============================================================

사용자가 숫자가 아닌 값을 넣으면 오류 발생 → 예외 처리 필요.

예:
    valid = True
    while valid:
        x = input("Enter a number: ")
        try:
            x = float(x)     # 숫자로 변환 시도
            valid = False    # 성공 → 루프 종료
        except:
            print("Wrong input, please try again.")

    print("Thank you!")
"""
# 파이썬 입력 검증 예제

valid = True
while valid:
    x = input("Enter a number: ")
    try:
        x = float(x)     # 숫자로 변환 시도
        valid = False    # 성공 → 루프 종료
    except:
        print("Wrong input, please try again.")
print("Thank you!")
# 결과 :
# Enter a number: hello
# Wrong input, please try again.
# Enter a number: 42
# Thank you!

"""
============================================================
📌 핵심 정리
============================================================

✔ input() → 항상 문자열 반환  
✔ 숫자가 필요하면 int(), float()로 변환  
✔ 잘못된 입력 대비하려면 try/except 사용  
✔ 프롬프트 문구로 안내 메시지 출력 가능

============================================================
"""
