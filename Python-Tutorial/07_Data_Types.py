"""
📌 내장 데이터 유형 (Built-in Data Types)
=========================================

프로그래밍에서 데이터 유형(Data Type)은 매우 중요한 개념입니다.
변수는 다양한 유형의 데이터를 저장할 수 있으며,
데이터 유형에 따라 수행할 수 있는 연산이나 동작이 달라집니다.

Python에는 다음과 같은 기본 내장 데이터 유형이 있습니다:

텍스트 유형 (Text Type)
    - str

숫자형 유형 (Numeric Types)
    - int, float, complex

시퀀스 유형 (Sequence Types)
    - list, tuple, range

매핑 유형 (Mapping Type)
    - dict

세트 유형 (Set Types)
    - set, frozenset

부울 유형 (Boolean Type)
    - bool

이진 유형 (Binary Types)
    - bytes, bytearray, memoryview

없음 유형 (None Type)
    - NoneType
"""

"""
📌 데이터 유형 확인 (type 함수)
------------------------------
type() 함수를 사용하면 객체의 데이터 유형을 확인할 수 있습니다.

예:
    x = 5
    print(type(x))    # <class 'int'>


데이터 유형은 변수에 값을 할당할 때 결정됩니다
-----------------------------------------------
아래는 다양한 값과 해당 데이터 유형 예시입니다.

예:
    x = "Hello World"                         # str
    x = 20                                     # int
    x = 20.5                                   # float
    x = 1j                                     # complex
    x = ["apple", "banana", "cherry"]          # list
    x = ("apple", "banana", "cherry")          # tuple
    x = range(6)                               # range
    x = {"name": "John", "age": 36}            # dict
    x = {"apple", "banana", "cherry"}          # set
    x = frozenset({"apple", "banana", "cherry"}) # frozenset
    x = True                                   # bool
    x = b"Hello"                               # bytes
    x = bytearray(5)                           # bytearray
    x = memoryview(bytes(5))                   # memoryview
    x = None                                   # NoneType
"""

"""
📌 명시적으로 데이터 유형 설정 (Constructor 함수 사용)
---------------------------------------------------
생성자(Constructor)를 사용하면 데이터 유형을 명시적으로 설정할 수 있습니다.

예:
    x = str("Hello World")                     # str
    x = int(20)                                # int
    x = float(20.5)                            # float
    x = complex(1j)                            # complex
    x = list(("apple", "banana", "cherry"))    # list
    x = tuple(("apple", "banana", "cherry"))   # tuple
    x = range(6)                               # range
    x = dict(name="John", age=36)              # dict
    x = set(("apple", "banana", "cherry"))     # set
    x = frozenset(("apple", "banana", "cherry")) # frozenset
    x = bool(5)                                # bool
    x = bytes(5)                               # bytes
    x = bytearray(5)                           # bytearray
    x = memoryview(bytes(5))                   # memoryview
"""