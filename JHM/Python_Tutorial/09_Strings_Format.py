####################################################################################
# 파이썬 - 향ㅅ;ㄱ - 믄지얄
####################################################################################

#######################################
# 문자열 형식
#######################################
# Python 변수 장에서 배웠듯이 문자열과 숫자를 다음과 같이 결합할 수 없습니다.

# 예 (오류)
# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)
# Traceback (most recent call last):
#   File "09_Strings_Format.py", line 13, in <module>
#     txt = "My name is John, I am " + age
#           ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

# 하지만 f-string 이나 메서드를 사용하면 문자열과 숫자를 결합할 수 있습니다 format()!

#######################################
# F-스트링
#######################################
# F-String은 Python 3.6에서 도입되었으며, 현재는 문자열을 포맷하는 데 선호되는 방법입니다.
# 문자열을 f-문자열로 지정하려면 f문자열 리터럴 앞에 을 넣고 {}변수와 다른 연산에 대한 자리 표시자로 중괄호를 추가하기만 하면 됩니다.

# 예
# f-문자열을 만듭니다.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# My name is John, I am 36

#######################################
# 플레이스홀더와 수정자
#######################################
# 플레이스홀더에는 값을 형식화하기 위한 변수, 연산, 함수 및 수정자가 포함될 수 있습니다.

# 예
# 변수 에 대한 플레이스홀더를 추가합니다 price.
price = 59
txt = f"The price is {price} dollars"
print(txt)
# The price is 59 dollars

# 플레이스홀더에는 값의 형식을 지정하는 수정자가 포함될 수 있습니다.
# 수정자는 콜론을 추가하고 :그 뒤에 합법적인 서식 유형을 지정하여 포함됩니다.
# 즉, .2f소수점 이하 두 자리로 이루어진 고정 소수점 숫자를 의미합니다.

# 예
# 소수점 이하 2자리까지 가격을 표시하세요:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# The price is 59.00 dollars

# 플레이스홀더에는 수학 연산과 같은 Python 코드가 포함될 수 있습니다.

# 예
# 플레이스홀더에서 수학 연산을 수행하고 결과를 반환합니다.
txt = f"The price is {20 * 59} dollars"
print(txt)
# The price is 1180 dollars

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# If x = 9, what is a correct syntax to print 'The price is 9.00 dollars'?

# print(f'The price is {x:.2f} dollars')            # Correct Answer!
# print(f'The price is {x:2} dollars')
# print(f'The price is {x:format(2)} dollars')