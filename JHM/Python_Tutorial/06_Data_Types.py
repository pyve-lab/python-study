####################################################################################
# 파이썬 데이터 유형
####################################################################################

#######################################
# 내장 데이터 유형
#######################################
# 프로그래밍에서 데이터 유형은 중요한 개념입니다.
# 변수는 다양한 유형의 데이터를 저장할 수 있으며, 다양한 유형은 서로 다른 작업을 수행할 수 있습니다.
# Python에는 기본적으로 다음 범주에 속하는 데이터 유형이 내장되어 있습니다.

# 텍스트 유형:	str
# 숫자형 유형:	int, float, complex
# 시퀀스 유형:	list, tuple, range
# 매핑 유형:	dict
# 세트 유형:	set,frozenset
# 부울 유형:	bool
# 이진 유형:	bytes, bytearray, memoryview
# 없음 유형:	NoneType

#######################################
# 데이터 유형 가져오기
#######################################
# 다음 함수를 사용하면 모든 객체의 데이터 유형을 얻을 수 있습니다 type().

# 예
# 변수 x의 데이터 유형을 출력하세요.
x = 5
print(type(x))
# <class 'int'>

#######################################
# 데이터 유형 설정
#######################################
# Python에서는 변수에 값을 할당할 때 데이터 유형이 설정됩니다.
#
# Example	Data Type	Try it
x = "Hello World"  # <class 'str'>
x = 20             # <class 'int'>
x = 20.5           # <class 'float'>
x = 1j             # <class 'complex'>
x = ["apple", "banana", "cherry"]           # <class 'list'>
x = ("apple", "banana", "cherry")           # <class 'tuple'>
x = range(6)       # <class 'range'>
x = {"name" : "John", "age" : 36}           # <class 'dict'>
x = {"apple", "banana", "cherry"}           # <class 'set'>
x = frozenset({"apple", "banana", "cherry"})# <class 'frozenset'>
x = True            # <class 'bool'>
x = b"Hello"        # <class 'bytes'>
x = bytearray(5)    # <class 'bytearray'>
x = memoryview(bytes(5))    # <class 'memoryview'>
x = None            # <class 'NoneType'>

# HAM : set과 frozenset의 차이가 뭐야?
# GPT : set → 수정할 수 있다
#       s = {1, 2, 3}
#       s.add(4)   # OK
#       s.remove(2)  # OK
#       frozenset → 수정 자체가 불가능
#       fs = frozenset([1, 2, 3])
#       fs.add(4)  # ❌ Error
#       fs.remove(2) # ❌ Error
#       fozenset이 필요한 이유는?
#       1) dict의 key로 사용할 수 있다
#       set은 mutable이라 key로 못 쓰지만, frozenset은 immutable이라 key 가능!
#       d = {frozenset([1,2,3]): "값"}  # 가능
#       2) set 안에 set을 넣고 싶을 때
#       s = {1, 2, frozenset([3, 4])}  # OK
#       3) “변경되면 안 되는 집합”을 표현할 때
#       데이터 보호용으로 사용하기도 해.