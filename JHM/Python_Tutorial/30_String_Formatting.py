####################################################################################
# 파이썬 String Formatting
####################################################################################

# F-String은 Python 3.6에서 도입되었으며, 현재는 문자열을 포맷하는 데 선호되는 방법입니다.
# Python 3.6 이전에는 이 메서드를 사용해야 했습니다 format().

#######################################
# F-스트링
#######################################
# F-문자열을 사용하면 문자열의 선택한 부분을 서식 지정할 수 있습니다.
# 문자열을 f-문자열로 지정하려면 f다음과 같이 문자열 리터럴 앞에 을 붙이면 됩니다.

# 예
# f-문자열을 만듭니다.
txt = f"The price is 49 dollars"
print(txt)
# The price is 49 dollars

#######################################
# 플레이스홀더와 수정자 Placeholders and Modifiers
#######################################
# f-문자열의 값을 형식화하려면 플레이스홀더를 추가합니다 {}. 플레이스홀더에는 값을 형식화하기 위한 변수, 연산, 함수 및 수정자가 포함될 수 있습니다.

# 예
# 변수 에 대한 플레이스홀더를 추가합니다 price.
price = 59
txt = f"The price is {price} dollars"
print(txt)
# The price is 59 dollars

# 플레이스홀더에는 값의 형식을 지정하는 수정자가 포함될 수도 있습니다.

# 수정자는 콜론을 추가하고 :그 뒤에 합법적인 서식 유형을 지정하여 포함됩니다.
# 즉, .2f소수점 이하 두 자리로 이루어진 고정 소수점 숫자를 의미합니다.

# 예
# 소수점 이하 2자리까지 가격을 표시하세요:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# The price is 59.00 dollars

# 변수에 보관하지 않고도 값을 직접 포맷할 수 있습니다.
# 예
# 소수점 이하 두 자리까지 값을 표시합니다 95.
txt = f"The price is {95:.2f} dollars"
print(txt)
# The price is 95.00 dollars

#######################################
# F-String에서 작업 수행
#######################################
# 플레이스홀더 내부에서 Python 작업을 수행할 수 있습니다.
# 수학 연산을 수행할 수 있습니다.

# 예
# 플레이스홀더에서 수학 연산을 수행하고 결과를 반환합니다.
txt = f"The price is {20 * 59} dollars"
print(txt)
# The price is 1180 dollars

# 변수에 대한 수학 연산을 수행할 수 있습니다.

# 예
# 가격을 표시하기 전에 세금을 추가하세요:
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
# The price is 73.75 dollars

# if...else플레이스홀더 내부에서 명령문을 수행할 수 있습니다 .

# 예
# 가격이 50을 넘으면 "Expensive"를 반환하고, 그렇지 않으면 "Cheap"를 반환합니다.
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)
# It is very Cheap

#######################################
# F-String에서 함수 실행
#######################################
# 플레이스홀더 내부에서 함수를 실행할 수 있습니다.

# 예
# 문자열 메서드를 사용하여 upper()값을 대문자로 변환합니다.
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)
# I love APPLES

# 함수는 내장된 Python 메서드일 필요는 없으며, 사용자 정의 함수를 만들어 사용할 수 있습니다.

# 예
# 피트를 미터로 변환하는 함수를 만듭니다.
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
# The plane is flying at a 9144.0 meter altitude

#######################################
# 더 많은 수정자
#######################################
# 이 장의 시작 부분에서는 .2f수정자를 사용하여 숫자를 소수점 이하 두 자리로 고정된 소수점 숫자로 포맷하는 방법을 설명했습니다.
# 값을 형식화하는 데 사용할 수 있는 몇 가지 다른 수정자가 있습니다.

# 예
# 쉼표를 천 단위 구분 기호로 사용하세요.
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
# The price is 59,000 dollars

# 모든 서식 유형 목록은 다음과 같습니다.

# Formatting Types
# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding Unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format

#######################################
# 문자열 형식()
#######################################
# Python 3.6 이전에는 문자열을 포맷하기 위해 이 메서드를 사용했습니다 format().
# 이 format()방법은 여전히 ​​사용할 수 있지만, f-문자열이 더 빠르고 문자열을 포맷하는 데 선호되는 방법입니다.
# 이 페이지의 다음 예제에서는 해당 format()메서드를 사용하여 문자열을 포맷하는 방법을 보여줍니다.
# 이 format()방법에서는 중괄호를 플레이스홀더로 사용 {}하지만 구문은 약간 다릅니다.

# 예
# 가격을 표시할 위치에 자리 표시자를 추가합니다.
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# The price is 49 dollars

# 중괄호 안에 매개변수를 추가하여 값을 변환하는 방법을 지정할 수 있습니다.

# 예
# 가격을 소수점 이하 두 자리 숫자로 표시하려면 다음과 같이 형식을 지정하세요.
txt = "The price is {:.2f} dollars"
# 모든 포맷 유형은 String format() 참조 에서 확인하세요 .

#######################################
# 여러 값
#######################################
# 더 많은 값을 사용하려면 format()메서드에 값을 더 추가하기만 하면 됩니다.
# print(txt.format(price, itemno, count))
# 그리고 더 많은 플레이스홀더를 추가합니다:

# 예
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item number 567 for 49.00 dollars.

#######################################
# 색인 번호
#######################################
# 인덱스 번호(중괄호 안의 숫자 {0})를 사용하면 값이 올바른 자리 표시자에 배치되었는지 확인할 수 있습니다.

# 예
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item number 567 for 49.00 dollars.

# 또한, 동일한 값을 두 번 이상 참조하려면 인덱스 번호를 사용하세요.

# 예
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# His name is John. John is 36 years old.

#######################################
# 명명된 인덱스
#######################################
# 중괄호 안에 이름을 입력하여 명명된 인덱스를 사용할 수도 있지만 {carname}, 매개변수 값을 전달할 때 이름을 사용해야 합니다 txt.format(carname = "Ford").

# 예
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
# I have a Ford, it is a Mustang.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What placeholders are used when dealing with f-strings?

# []
# ()
# {}     # Correct Answer!