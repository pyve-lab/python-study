# Format Strings
# 문자열 형식 지정 (String Format)
# 1. 문자열과 숫자 결합의 문제
# 문제점: 파이썬에서 문자열(String)과 숫자(Number)를 + 연산자로 직접 결합할 수 없습니다. 시도하면 오류가 발생합니다.

age = 36
# 에러 발생: 문자열(str)과 숫자(int)를 +로 직접 연결할 수 없음
# txt = "My name is John, I am " + age 
# print(txt)
# 해결책: 이 문제를 해결하고 문자열과 숫자를 결합하기 위해 f-string 또는 format() 메서드를 사용해야 합니다.


# 2. f-string 사용 (F-Strings)
# f-string은 Python 3.6부터 도입되었으며, 현재 문자열 형식 지정에 가장 선호되는 방식입니다.

#사용법:
# 문자열 리터럴 앞에 단순하게 **f**를 붙입니다.
#변수나 기타 연산이 들어갈 자리에 중괄호 {} 를 플레이스홀더(placeholder)로 사용합니다.

# f-string 생성 예시
age = 36
# f"..." 형태로 문자열을 정의하고, {} 안에 변수를 넣음
txt = f"My name is John, I am {age}"
print(txt)
# 출력: My name is John, I am 36


# 3. 플레이스홀더와 수정자 (Placeholders and Modifiers)
# A. 변수 사용
# 플레이스홀더 {} 안에는 변수를 넣어 값을 문자열에 삽입할 수 있습니다.

# price 변수를 플레이스홀더에 추가하는 예시
price = 59
txt = f"The price is {price} dollars"
print(txt)
# 출력: The price is 59 dollars

# B. 형식 수정자 (Modifiers) 사용
# 플레이스홀더는 값의 형식을 지정하는 **수정자(modifier)**를 포함할 수 있습니다.

# 사용법: 콜론 : 뒤에 **.2f**와 같이 유효한 형식 지정 타입을 추가합니다. 
# (예: .2f는 소수점 이하 두 자리까지 표시하는 고정 소수점 숫자를 의미합니다.)

# 가격을 소수점 이하 두 자리로 표시하는 예시
price = 59
# :.2f 는 "소수점 두 자리로 고정"하라는 수정자
txt = f"The price is {price:.2f} dollars"
print(txt)
# 출력: The price is 59.00 dollars

# C. 파이썬 코드 실행
# 플레이스홀더 {} 안에는 수학 연산과 같은 파이썬 코드를 포함하고 그 결과를 문자열에 반환할 수 있습니다.

# 플레이스홀더 내에서 수학 연산을 수행하고 결과를 반환하는 예시
# {} 안에 20 * 59 연산 코드를 직접 작성
txt = f"The price is {20 * 59} dollars"
print(txt)
# 출력: The price is 1180 dollars