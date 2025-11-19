"""
📌 변수 이름 규칙 (Variable Naming Rules)
=========================================

변수 이름은 짧게(x, y) 지을 수도 있고,
age, carname, total_volume처럼 의미 있는 이름으로 만들 수도 있습니다.

Python 변수 이름 규칙
-----------------------
1. 변수 이름은 문자 또는 밑줄(_)로 시작해야 합니다.
2. 변수 이름은 숫자로 시작할 수 없습니다.
3. 변수 이름에는 영문자(A–Z, a–z), 숫자(0–9), 밑줄(_)만 사용할 수 있습니다.
4. 변수 이름은 대소문자를 구분합니다.
   → age, Age, AGE는 서로 다른 변수입니다.
5. 변수 이름은 Python 키워드(keyword)를 사용할 수 없습니다.


✔ 합법적인 변수 이름 예시:
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"


✘ 잘못된 변수 이름 예시:
    2myvar = "John"    # 숫자로 시작 ❌
    my-var = "John"    # 하이픈은 사용 불가 ❌
    my var = "John"    # 공백 포함 불가 ❌
"""
# 파이썬 변수 이름

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 불가능 변수 

# 2myvar = "John"
# my-var = "John"
# print(my-var)
# 결과 : SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# my var = "John"