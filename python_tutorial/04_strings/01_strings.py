# Strings
# 1. 파이썬 문자열
# 파이썬에서 문자열은 작은따옴표(' ') 또는 큰따옴표(" ")로 묶습니다.
string1 = 'Hello, World!'
string2 = "Python is fun."
print(string1)
print(string2)


# 2. 인용문 안의 인용문
# 문자열 안에 작은따옴표와 큰따옴표를 혼합하여 사용할 수 있습니다.
str = "He said, 'Python is awesome!'"
print(str)
str2 = 'She replied, "I love programming."'
print(str2)


# 3. 변수에 문자열 할당
# 변수에 문자열을 할당하려면 변수 이름 뒤에 등호와 문자열을 붙여야 합니다.
a = "Hello"
b = "World"
print(a)
print(b)


# 4. 여러 줄 문자열
# 여러 줄 문자열을 만들려면 삼중 따옴표 (''' 또는 """)를 사용합니다.
# 결과적으로 줄 바꿈은 코드와 같은 위치에 삽입됩니다. (코드에 있는 줄 바꿈이 문자열에 포함됨)
multi_line_str = """This is a string
that spans multiple
lines."""
print(multi_line_str)

multi_line_str2 = '''Another way to create
a multi-line string.'''
print(multi_line_str2)


# 5. 문자열은 배열(Array)과 같다
# 다른 인기 있는 프로그래밍 언어와 마찬가지로, 파이썬에서 문자열(Strings)은 유니코드 문자들의 배열로 취급됩니다.
# 문자형(Character Type)은 없습니다: 파이썬에는 별도의 문자(Character) 자료형이 없습니다.
# 길이가 1인 문자열: 단일 문자는 길이가 1인 문자열로 간주됩니다.
# 문자열을 배열처럼 다룰 수 있기 때문에, 대괄호([])를 사용하여 문자열 내의 개별 문자에 접근할 수 있습니다.
# 인덱스(Index): 문자열의 위치를 나타내는 번호이며, 첫 번째 문자는 항상 0번 위치를 가집니다.
a = "Hello, World!" 
print(a[1]) # 1번 위치의 문자 가져오기 (H=0, e=1 이므로 'e'가 됩니다)


# 6. 문자열 반복 (Looping Through a String)
# 문자열은 여러 문자로 이루어진 배열(Array)과 같기 때문에, for 반복문을 사용하여 문자열 내의 개별 문자를 하나씩 순회(Looping)할 수 있습니다.
# for 반복문 활용
# for 반복문은 문자열에 있는 모든 문자를 처음부터 끝까지 순서대로 실행합니다.
# 단어 "banana"의 각 문자를 반복하여 출력
for x in "banana":
  print(x)
  # 각 문자를 한 줄에 하나씩 출력합니다.
# 출력 결과:
'''
b
a
n
a
n
a
'''


# 7. 문자열 길이 (String Length)
# 문자열의 길이를 측정하려면 내장 함수 len()을 사용합니다.
# len() 함수는 괄호 안에 전달된 문자열의 길이를 정수(integer)로 반환합니다.
a = "Hello, World!"
# 문자열 a의 길이를 반환 (공백과 특수문자(!) 포함)
print(len(a)) 
# 출력: 13

# len() 함수를 사용하여 문자열의 길이를 계산하는 원칙
'''
시작점은 1: 길이는 사람이 숫자를 세듯이 1부터 시작합니다. (길이가 0인 문자열은 ""뿐입니다.)

모든 문자 포함: 눈에 보이는 모든 글자, 숫자, 공백, 특수 문자 (마침표, 쉼표, 느낌표 등)는 각각 하나의 길이(1)로 계산됩니다.

'''

# 헷갈리기 쉬운 개념 비교
# 길이(len())는 1부터 세지만, 문자열 요소에 접근하는 인덱스(Index)는 0부터 시작한다는 점을 꼭 구분하셔야 합니다.
# 길이 (len()) : 시작점이1, 문자열이 얼마나 긴지 (총 몇 개인지)
# 인덱스 (a[n]) : 시작점이 0, 특정 문자가 몇 번째 칸에 있는지 (위치)


# 8. 문자열 포함 여부 확인 (Checking String)
# 파이썬에서 특정 구문이나 문자가 문자열에 포함되어 있는지(present) 확인하려면 in 키워드를 사용합니다.
# in 키워드를 사용하면 그 결과로 불리언 값인 True 또는 False를 즉시 반환받을 수 있습니다.
txt = "The best things in life are free!"

print("free" in txt) # "free"가 txt 변수 안에 있는지 확인


# 9. 조건문(if) 활용
# 불리언 결과를 if 조건문과 결합하여, 특정 구문이 있을 때만 코드를 실행하도록 만들 수 있습니다.
txt = "The best things in life are free!"

if "free" in txt:
  print("Yes, 'free' is present.")
  
# 반대로 특정 구문이 문자열에 포함되어 있지 않은지 확인하려면 not in 키워드를 사용합니다.
txt = "The best things in life are free!"

if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

