# Booleans
# 1. 파이썬 불리언(참/거짓) 값
# 프로그래밍에서 우리는 어떤 표현식(expression)이 참(True)인지 거짓(False)인지를 알아야 할 때가 많습니다.
# 파이썬에서는 어떤 표현식이든 평가(evaluate)하면, 그 결과로 참(True) 또는 거짓(False) 중 하나의 불리언(Boolean) 값을 얻게 됩니다.
# 예를 들어, 두 값을 비교할 때, 파이썬은 해당 표현식을 평가하여 그 결과에 해당하는 불리언 값을 반환합니다.
# 예제에서 첫 번째 표현식은 참(True)이므로 True를 출력하고, 두 번째와 세 번째 표현식은 거짓(False)이므로 False를 출력합니다.
print(10 > 9)
print(10 == 9)
print(10 < 9)


# 2. 조건문에서의 불리언 값
# 불리언 값은 조건문(if 문)에서 매우 자주 사용됩니다.
# 조건문은 특정 조건이 참인지 거짓인지에 따라 코드 블록을 실행할지 여부를 결정합니다.
# True일 경우: if 블록 안의 코드가 실행됩니다.
# False일 경우: if 블록 안의 코드는 건너뛰어집니다.
# 즉, 조건문은 조건의 평가 결과가 True인지 False인지에 따라 특정 메시지를 출력하거나, 특정 동작을 수행할지 여부를 결정합니다.

a = 200
b = 33

if b > a: # 조건식: b가 a보다 큰가? (False)
  print("b is greater than a") # 이 코드는 실행되지 않음
else:
  print("b is not greater than a") # 이 코드는 실행됨
  
  
# 3. 값 및 변수의 불리언 평가
# 파이썬의 bool() 함수를 사용하면 어떤 값이든 평가하여 참(True) 또는 거짓(False) 중 하나의 불리언 값을 얻을 수 있습니다.

# 값(Value) 평가
# bool() 함수는 숫자나 문자열 리터럴 자체를 평가할 수 있습니다.
print(bool("Hello"))    # True	비어 있지 않은(Non-empty) 문자열은 True로 평가됩니다.
print(bool(15))         # True	0이 아닌(Non-zero) 숫자는 True로 평가됩니다.

# 변수(Variable) 평가
# 변수에 할당된 값을 bool() 함수로 평가할 수도 있습니다.
x = "Hello" # 비어 있지 않은 문자열
y = 15      # 0이 아닌 숫자

print(bool(x)) # 출력: True
print(bool(y)) # 출력: True


# 4. 불리언 값 평가 규칙 : 참(True) 또는 거짓(False)
# 참(True)이 되는 값 (Most values are True)
'''
어떤 형태든 '내용'을 가지고 있는 값은 모두 True로 평가됩니다.

문자열 (str): 빈 문자열 ("")을 제외한 모든 문자열.

예: bool("abc") → True

숫자 (int, float 등): 숫자 0을 제외한 모든 숫자 (양수, 음수).

예: bool(123) → True

컬렉션 (List, Tuple, Set, Dict): 비어 있는 컬렉션을 제외한 모든 리스트, 튜플, 세트, 딕셔너리.

예: bool(["apple", "cherry"]) → True

'''

# 거짓(False)이 되는 값 (Few Values are False)
# False로 평가되는 값은 그 종류가 많지 않으며, 대부분 '비어 있음' 또는 '없음'을 나타내는 값들입니다.
'''
예약어 및 없음 : 불리언 자체인 False, 값이 없음을 나타내는 None
숫자 : 정수 0 (또는 실수 0.0)
빈 자료구조 (컬렉션) : 빈 문자열: "" / 빈 리스트: [] / 빈 튜플: () / 빈 세트 또는 딕셔너리: {}

'''

# 클래스 인스턴트 평가
# 클래스로 만든 객체(Object)도 불리언으로 평가될 수 있습니다.
# 클래스 내부에 정의된 특별한 메서드인 __len__ 메서드가 0 또는 False를 반환하도록 정의되어 있다면
# 해당 객체는 False로 평가됩니다. 이는 객체가 '내용이 없음'을 명시적으로 시스템에 알리는 방식입니다.

class myclass():
    def __len__(self):
        # 객체를 평가했을 때, 길이가 0임을 반환하도록 설정
        return 0

myobj = myclass()
print(bool(myobj)) # 출력: False


# 5. 함수를 이용한 불리언 값 반환 및 활용
# 파이썬에서는 함수를 정의할 때, 특정 조건에 따라 불리언 값을 반환하도록 만들 수 있습니다.
# return True 또는 return False 구문을 사용하여 함수가 불리언 값을 직접 반환하도록 만들 수 있습니다.
def myFunction():
  return True       # 함수 실행 결과(True)를 직접 출력
print(myFunction()) # 출력: True


# 6. 불리언 결과에 따라 코드 실행하기 (조건문 활용)
# 함수가 반환한 불리언 값에 따라 조건문을 사용하여 다른 코드를 실행할 수 있습니다.
def myFunction():
  return True # 함수는 True를 반환

if myFunction(): # if 조건식이 True이므로
  print("YES!") # 이 블록 실행
else:
  print("NO!") 
# 출력: YES!


# 7. 내장함수 isinstance() 활용
# 파이썬에는 객체가 특정 자료형인지 확인하는 isinstance() 함수와 같이, 불리언 값을 반환하는 다양한 내장 함수가 있습니다.
# isinstance(객체, 자료형) 함수는 객체가 주어진 자료형의 인스턴스(instance)이면 True를, 아니면 False를 반환합니다.
x = 200
print(isinstance(x, int)) # 출력: True (x는 정수형이므로)
print(isinstance(x, str)) # 출력: False (x는 문자열형이 아니므로)

# 이 함수는 코드의 안정성을 높일 때 유용합니다. 
# 예를 들어, 어떤 함수가 반드시 숫자만 입력받아야 할 때, 입력된 값이 숫자가 맞는지 미리 확인하고 싶을 때 isinstance()를 사용합니다. 
def add_only_numbers(a, b): # add_only_numbers 함수는 두 값 a와 b를 받아서 더하는 것. 단, a는 반드시 정수(int)여야 한다.
    if not isinstance(a, int): # 만약 a가 정수(int)가 아니라면
        print("경고: 첫 번째 값은 정수여야 합니다.")
        return 0 # 결과로 0을 돌려주면서 함수 실행을 거기서 끝냅니다
    return a + b # 만약 a가 정수(int)라면, 함수는 아무 경고 없이 원래 하려던 일, 즉 a와 b를 더한 값을 깔끔하게 돌려줍니다.