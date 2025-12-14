####################################################################################
# 파이썬 문자열
####################################################################################

#######################################
# 문자열
#######################################
# 파이썬에서 문자열은 작은따옴표나 큰따옴표로 묶습니다.
# 'hello' 는 "hello" 와 같습니다.
# 다음 함수를 사용하여 문자열 리터럴을 표시할 수 있습니다 print().

# 예
print("Hello")
print('Hello')
# Hello
# Hello

#######################################
# 인용문 안의 인용문 Quotes
#######################################
# 문자열을 둘러싼 따옴표와 일치하지 않는 한 문자열 내부에 따옴표를 사용할 수 있습니다.

# 예
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# It's alright
# He is called 'Johnny'
# He is called "Johnny"

#######################################
# 변수에 문자열 할당
#######################################
# 변수에 문자열을 할당하려면 변수 이름 뒤에 등호와 문자열을 입력합니다.

# 예
a = "Hello"
print(a)
# Hello

#######################################
# 다중줄 문자열
#######################################
# 세 개의 따옴표를 사용하여 여러 줄의 문자열을 변수에 할당할 수 있습니다.

# 예
# 큰따옴표를 세 개 사용할 수 있습니다.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

# 또는 작은따옴표 세 개:
# 예
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

# 참고: 결과적으로 줄 바꿈은 코드와 같은 위치에 삽입됩니다.

#######################################
# 문자열은 배열입니다
#######################################
# 다른 많은 인기 프로그래밍 언어와 마찬가지로 Python의 문자열은 유니코드 문자의 배열입니다.
# 하지만 파이썬에는 문자 데이터 유형이 없습니다. 단일 문자는 길이가 1인 문자열일 뿐입니다.
# 대괄호를 사용하여 문자열의 요소에 접근할 수 있습니다.

# 예
# 위치 1에 있는 문자를 가져옵니다(첫 번째 문자는 위치 0에 있다는 것을 기억하세요):
a = "Hello, World!"
print(a[1])
# e

#######################################
# 문자열 반복
#######################################
# 문자열은 배열이므로 루프를 사용하여 문자열의 문자를 반복할 수 있습니다 for.

# 예
# "banana"라는 단어의 글자를 반복하세요:
for x in "banana":
    print(x)
# b
# a
# n
# a
# n
# a

#######################################
# 문자열 길이
#######################################
# 문자열의 길이를 구하려면 len()함수를 사용하세요.

# 예
# 이 len()함수는 문자열의 길이를 반환합니다.
a = "Hello, World!"
print(len(a))
# 13

#######################################
# 문자열 확인
#######################################
# 문자열에 특정 구문이나 문자가 있는지 확인하려면 키워드를 사용할 수 있습니다 in.

# 예
# 다음 텍스트에 "무료"가 있는지 확인하세요.
txt = "The best things in life are free!"
print("free" in txt)
# True

# 다음과 같은 문장에서 사용하세요 if:
# 예
# "free"가 있는 경우에만 인쇄합니다.
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
# Yes, 'free' is present.

#######################################
# 아닌 경우 체크하세요 Check if NOT
#######################################
# 문자열에 특정 구문이나 문자가 존재하지 않는지 확인하려면 키워드를 사용할 수 있습니다 not in.

# 예
# 다음 텍스트에 "expensive"가 없는지 확인하세요:
txt = "The best things in life are free!"
print("expensive" not in txt)
# True

# 다음과 같은 문장에서 사용하세요 if:
# 예
# "expensive"가 존재하지 않는 경우에만 인쇄합니다.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
# No, 'expensive' is NOT present.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What will be the result of the following code:
x = 'Welcome'
print(x[3])

# Wel
# c                         # Correct Answer!
# Welcome Welcome Welcome