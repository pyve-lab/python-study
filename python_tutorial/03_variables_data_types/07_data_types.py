# Data Types
# 1. 파이썬 데이터 유형
# 프로그래밍에서 데이터 유형은 중요한 개념입니다. 
# 변수는 다양한 유형의 데이터를 저장할 수 있으며, 각 데이터 유형은 서로 다른 작업을 수행할 수 있습니다.
# 파이썬에는 기본적으로 데이터유형이 내장되어 있습니다.
'''
Text Type:	str (문자열)
Numeric Types:	int, float, complex (정수, 부동소수점, 복소수)
Sequence Types:	list, tuple, range (리스트, 튜플, 범위)
Mapping Type:	dict (매핑)
Set Types:	set, frozenset (집합, 불변집합)
Boolean Type:	bool (참,거짓)
Binary Types:	bytes, bytearray, memoryview (바이트, 바이트배열, 메모리뷰)
None Type:	NoneType (널값)

'''

# 2. 데이터 유형 확인하기
# type() 함수를 사용하여 변수의 데이터 유형을 확인할 수 있습니다.
x = 5
y = "Hello, World!"
print(type(x)) # 출력 : <class 'int'>
print(type(y)) # 출력 : <class 'str'>

z = 3.1456
print(type(z)) # 출력 : <class 'float'>


# 3. 데이터 유형 설정
# 파이썬에서는 변수에 값을 할당할 때 데이터 유형이 자동으로 설정됩니다.
'''
str : x = "Hello World"
int : x = 20	
float : x = 20.5	
complex : x = 1j	
list : x = ["apple", "banana", "cherry"]	
tuple : x = ("apple", "banana", "cherry")	
range : x = range(6)	
dict : x = {"name" : "John", "age" : 36}	
set : x = {"apple", "banana", "cherry"}	
frozenset :  x = frozenset({"apple", "banana", "cherry"})		
bool x = True		
bytes x = b"Hello"		
bytearray x = bytearray(5)		
memoryview x = memoryview(bytes(5))		
NoneType : x = None	

'''


# 4. 특정 데이터 유형으로 변환하기
# 파이썬에서는 변수의 데이터 유형을 다른 유형으로 변환할 수 있습니다
'''
str : x = str("Hello World")		
int : x = int(20)		
float : x = float(20.5)		
complex : x = complex(1j)		
list : x = list(("apple", "banana", "cherry"))		
tuple : x = tuple(("apple", "banana", "cherry"))		
range : x = range(6)		
dict : x = dict(name="John", age=36)		
set : x = set(("apple", "banana", "cherry"))		
frozenset : x = frozenset(("apple", "banana", "cherry"))		
bool : x = bool(5)		
bytes : x = bytes(5)		
bytearray : x = bytearray(5)		
memoryview : x = memoryview(bytes(5))

'''


# 5. 데이터 자료형이 자동으로 설정되는것과 이미 선언된 변수의 자료형을 변환하는것의 차이점
# 자료형 자동 설정 (동적 타이핑)
'''
파이썬의 가장 큰 특징인 **동적 타이핑(Dynamic Typing)**을 보여줍니다.
방식: 변수에 특정 형태의 값(리터럴)을 할당하는 순간, 파이썬 인터프리터가 그 값의 형태를 분석하여 자동으로 자료형을 결정합니다.

예시:
x = "Hello World": 따옴표를 사용했으므로 자동으로 str (문자열)로 결정됩니다.

x = [1, 2, 3]: **대괄호([])**를 사용했으므로 자동으로 **list**로 결정됩니다.

'''

# 자료형 변환 (명시적 타이핑)
'''
이 방식은 자료형을 명시적으로 지정하거나 형 변환(Casting)을 할 때 사용합니다.
방식: str(), int(), list(), dict() 와 같은 생성자 함수 (Constructor)를 호출하여, 괄호 안의 값을 해당 자료형으로 변환하거나 새로운 객체를 생성합니다.

예시:

x = str("Hello World"): 문자열을 명시적으로 문자열로 지정합니다. (이 경우 첫 번째 방식과 결과는 같지만 의도가 명확해집니다.)

x = bool(5): 숫자 5를 bool 자료형으로 변환하여 True 값을 가지게 합니다. (만약 bool(0)이었다면 False가 됩니다.)

x = list(("apple", "banana")): tuple 형태의 값을 **list**로 명시적으로 형 변환합니다.

'''
