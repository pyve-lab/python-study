# 파이썬 문자열 형식 지정 (String Formatting)

# F-string은 Python 3.6에서 도입되었으며, 현재 문자열 형식 지정에 가장 선호되는 방식입니다. 
# Python 3.6 이전에는 format() 메서드를 사용해야 했습니다.

# ------------------------------------------------------------------------------
# 1. F-스트링 (F-Strings)
# ------------------------------------------------------------------------------

# F-string은 문자열의 특정 부분을 형식화(format)할 수 있게 해줍니다.
# 사용법: 문자열 리터럴 앞에 단순하게 **f**를 붙입니다.
# 
# # 예시: f-string 생성
# txt = f"The price is 49 dollars"
# print(txt) # 출력: The price is 49 dollars

# A. 플레이스홀더와 수정자 (Placeholders and Modifiers)
# f-string에서 값을 형식화하려면 **중괄호 {}**를 플레이스홀더로 추가합니다. 
# 플레이스홀더는 변수, 연산, 함수, 그리고 값 형식을 지정하는 **수정자(modifier)**를 포함할 수 있습니다.
# 
price = 59
# # 예시: price 변수에 대한 플레이스홀더 추가
# txt = f"The price is {price} dollars"
# print(txt) # 출력: The price is 59 dollars

# 플레이스홀더는 값 형식을 지정하는 수정자를 포함할 수 있습니다. 
# 수정자는 콜론 : 뒤에 **.2f**와 같이 유효한 형식 지정 타입을 추가하여 포함됩니다. 
# (.2f는 소수점 이하 두 자리로 고정된 소수점 숫자를 의미합니다.)
# 
price = 59
# # 예시: 가격을 소수점 이하 두 자리로 표시
# txt = f"The price is {price:.2f} dollars"
# print(txt) # 출력: The price is 59.00 dollars

# 값을 변수에 담지 않고 직접 형식화할 수도 있습니다.
# 
# # 예시: 값 95를 소수점 이하 두 자리로 표시
# txt = f"The price is {95:.2f} dollars"
# print(txt) # 출력: The price is 95.00 dollars

# B. F-string 내에서 연산 수행 (Perform Operations)
# 플레이스홀더 내부에서 파이썬 연산을 수행할 수 있습니다.
# 
# # 예시: 플레이스홀더 내에서 수학 연산을 수행하고 결과 반환
# txt = f"The price is {20 * 59} dollars"
# print(txt) # 출력: The price is 1180 dollars

# 변수에 대한 수학 연산:
price = 59
tax = 0.25
# # 예시: 가격을 표시하기 전에 세금(tax)을 추가
# # (가격 + 가격 * 세금) 연산 수행
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt) # 출력: The price is 73.75 dollars

# if...else 문: (삼항 연산자)
price = 49
# # 예시: 플레이스홀더 내에서 if...else 삼항 연산 수행
# # 가격이 50보다 크면 'Expensive', 아니면 'Cheap'을 반환
# txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
# print(txt) # 출력: It is very Cheap

# C. F-string 내에서 함수 실행 (Execute Functions)
# 플레이스홀더 내부에서 함수를 실행할 수 있습니다.
# 
fruit = "apples"
# # 예시: 문자열 메서드 upper()를 사용하여 값을 대문자로 변환
# txt = f"I love {fruit.upper()}"
# print(txt) # 출력: I LOVE APPLES

# 내장 메서드가 아닌 직접 정의한 함수도 사용할 수 있습니다.
# # 예시: 피트(feet)를 미터(meters)로 변환하는 함수 생성
def myconverter(x):
  return x * 0.3048
# # 함수를 플레이스홀더 내에서 실행
# txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
# print(txt) # 출력: The plane is flying at a 9144.0 meter altitude

# D. 추가 수정자 (More Modifiers)
# .2f 수정자 외에도 값을 형식화하는 데 사용할 수 있는 다양한 수정자들이 있습니다.
# 
price = 59000
# # 예시: 쉼표(,)를 천 단위 구분 기호로 사용
# # :, 수정자를 사용하여 천 단위 쉼표 추가
# txt = f"The price is {price:,} dollars"
# print(txt) # 출력: The price is 59,000 dollars

# # 형식 지정 타입 (Formatting Types) | 설명 (Description)
# # :< | 사용 가능한 공간 내에서 결과를 왼쪽 정렬
# # :> | 사용 가능한 공간 내에서 결과를 오른쪽 정렬
# # :^ | 사용 가능한 공간 내에서 결과를 가운데 정렬
# # := | 부호(sign)를 가장 왼쪽 위치에 배치
# # :+ | 결과가 양수 또는 음수임을 나타내기 위해 + 부호를 사용
# # :- | 음수 값에만 - 부호를 사용
# # : | 양수 앞에 공백 한 칸을 삽입하고, 음수 앞에는 - 부호를 삽입
# # :, | 쉼표를 천 단위 구분 기호로 사용
# # :_ | 언더바(_)를 천 단위 구분 기호로 사용
# # :b | 2진수 형식
# # :c | 값을 해당 유니코드 문자로 변환
# # :d | 10진수 형식
# # :e | 과학적 표기법 형식 (소문자 e 사용)
# # :E | 과학적 표기법 형식 (대문자 E 사용)
# # :f | 고정 소수점 형식
# # :F | 고정 소수점 형식 (INF 및 NAN을 INF 및 NAN으로 표시)
# # :g | 일반 형식
# # :G | 일반 형식 (과학적 표기법에 대문자 E 사용)
# # :o | 8진수 형식
# # :x | 16진수 형식 (소문자)
# # :X | 16진수 형식 (대문자)
# # :n | 숫자 형식
# # :% | 퍼센트 형식

# ------------------------------------------------------------------------------
# 2. format() 메서드
# ------------------------------------------------------------------------------

# Python 3.6 이전에는 format() 메서드를 사용하여 문자열 형식을 지정했습니다.
# format() 메서드 역시 **중괄호 {}**를 플레이스홀더로 사용하지만, 구문은 약간 다릅니다.

price = 49
txt = "The price is {} dollars"
# # 예시: 가격을 표시할 위치에 플레이스홀더 추가
# # 문자열의 format() 메서드를 호출하고 값을 인수로 전달
# print(txt.format(price)) # 출력: The price is 49 dollars

# 중괄호 안에 매개변수를 추가하여 값을 어떻게 변환할지 지정할 수 있습니다.
txt = "The price is {:.2f} dollars"
# # 예시: 가격을 소수점 이하 두 자리 숫자로 표시하도록 형식 지정
# # .2f 수정자는 format() 메서드의 인수로 전달된 값에 적용됨
# print(txt.format(49)) # 출력: The price is 49.00 dollars

# A. 여러 개의 값 (Multiple Values)
quantity = 3
itemno = 567
price = 49
# # 예시: 여러 개의 값을 사용
# # 플레이스홀더 {}의 개수와 format() 인수의 개수가 일치해야 함
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price)) # 출력: I want 3 pieces of item number 567 for 49.00 dollars.

# B. 인덱스 번호 (Index Numbers)
quantity = 3
itemno = 567
price = 49
# # 예시: 인덱스 번호를 사용하여 순서 지정
# # {0}, {1}, {2:.2f}가 format() 인수의 순서(0, 1, 2)를 지정
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price)) # 출력: I want 3 pieces of item number 567 for 49.00 dollars.

age = 36
name = "John"
# # 예시: 같은 값을 여러 번 참조
# # {1} (name)이 두 번 사용되고, {0} (age)가 한 번 사용됨
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name)) # 출력: His name is John. John is 36 years old.

# C. 이름 있는 인덱스 (Named Indexes)
# 중괄호 안에 이름을 입력하여 이름 있는 인덱스를 사용할 수 있습니다.
# format() 호출 시 이름과 값을 쌍으로 전달해야 합니다.
# 
# # 예시: 이름 있는 인덱스 사용
# # {carname}과 {model}이라는 이름을 사용
# myorder = "I have a {carname}, it is a {model}."
# # format() 호출 시 이름과 값을 쌍으로 전달
# print(myorder.format(carname = "Ford", model = "Mustang")) # 출력: I have a Ford, it is a Mustang.