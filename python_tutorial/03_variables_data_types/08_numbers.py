# Numbers
# 1. 파이썬 숫자 타입
# 파이썬에는 세 가지 주요 숫자 타입이 있습니다: 정수(int), 실수(float), 복소수(complex).
# 정수 (int): 소수점이 없는 숫자입니다. 예: -10, 0, 25
# 부동 소수점 (float): 소수점이 있는 숫자입니다. 예: -3.14, 0.0, 2.718
# 복소수 (complex): 실수부와 허수부로 구성된 숫자입니다. 예: 3 + 4j, 1 - 2j 

# 숫자형 변수는 다음과 같이 선언할 수 있습니다.
x = 10          # 정수형 변수
y = 3.14        # 실수형 변수
z = 2 + 3j     # 복소수형 변수

# 파이썬에서 숫자형 변수의 타입을 확인하려면 type() 함수를 사용할 수 있습니다.
print(type(x)) # 출력 : <class 'int'>
print(type(y)) # 출력 : <class 'float'>
print(type(z)) # 출력 : <class 'complex'>


# 2. 정수(Int)
# Int 또는 정수는 소수점이 없는 양수 또는 음수의 정수이며, 길이는 제한이 없습니다.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# 3. 실수(Float)
# 부동 소수점 숫자 또는 "부동 소수점 숫자"는 하나 이상의 소수점을 포함하는 양수 또는 음수 숫자입니다.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float는 10의 거듭제곱을 나타내는 "e"를 사용한 과학적 숫자일 수도 있습니다.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


# 4. 복소수(Complex)
# 복소수는 실수부와 허수부로 구성된 숫자입니다. 파이썬에서는 복소수를 나타내기 위해 "j" 또는 "J"를 사용합니다.
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# 5. 유형 변환
# 파이썬에서는 int(), float(), complex() 함수를 사용하여 숫자형 변수의 유형을 변환할 수 있습니다.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x) 

#convert from float to int:
b = int(y) 

#convert from int to complex:
c = complex(x) # c는 (1+0j)

print(a) # a는 1.0
print(b) # b는 2
print(c) # c는 (1+0j)

print(type(a)) # <class 'float'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'complex'>


# 6. 난수
# 파이썬에서는 random 모듈을 사용하여 난수를 생성할 수 있습니다.
import random
print(random.randint(1, 10))  # 1에서 10 사이의 임의의 정수 출력
print(random.random())        # 0.0에서 1.0 사이의 임의의 부동 소수점 숫자 출력
