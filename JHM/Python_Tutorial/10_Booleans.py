####################################################################################
# 파이썬 Boolean
####################################################################################
# Boolean 은 다음 두 값 중 하나를 나타냅니다. True또는 False.
#######################################
# Boolean 값
#######################################
# True프로그래밍에서는 표현식이 .인지 .인지 알아야 할 때가 많습니다 False.
# Python에서는 모든 표현식을 평가하여 두 가지 답 중 하나를 얻을 수 있습니다 True.False
# 두 값을 비교하면 표현식이 평가되고 Python은 부울 답을 반환합니다.

# 예
print(10 > 9)
print(10 == 9)
print(10 < 9)
# True
# False
# False

# if 문에서 조건을 실행하면 Python은 Trueor 를 반환합니다 False.
# 예
# 조건이 다음 True과 같은지 여부에 따라 메시지를 출력합니다 False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# b is not greater than a

#######################################
# 값과 변수 평가
#######################################
# 이 bool()기능을 사용하면 모든 값을 평가하고 그에 대한 대가를 받을 수 True있습니다 False .
# 예
# 문자열과 숫자를 평가합니다.
print(bool("Hello"))
print(bool(15))
# True
# True

# 예
# 두 가지 변수를 평가합니다.
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
# True
# True

# HAM : 뭘 평가하겠다는 거야 존재하냐 안 하냐야?
# GPT : 여기서 **“값을 평가한다”**는 말은 그 값이 True로 취급될지, False로 취급될지 판정한다는 뜻이야.
#       즉, 파이썬이 ‘이 값은 참인가? 거짓인가?’를 판단한다는 것이지.
#       그래서 정확히 뭘 평가하는 건데?
#       존재하냐 / 비어 있냐와 아주 비슷한 개념이야.
#       하지만 조금 더 넓어. 파이썬에서는 다음 규칙으로 True/False가 결정돼:
#       파이썬에서 False로 평가되는 값들
#       다음 값들은 모두 False가 돼:
#       1.	False
#       2.	None
#       3.	숫자 0 (0, 0.0, 0j 등)
#       4.	빈 문자열 ""
#       5.	빈 리스트 []
#       6.	빈 튜플 ()
#       7.	빈 딕셔너리 {}
#       8.	빈 집합 set()
#       9.	사용자 정의 객체에서 __bool__() 또는 __len__()이 0을 반환하는 경우
#       즉, 비어있거나(Empty) 값이 없을 때(False) → False
#       True로 평가되는 값들
#       그 외의 모든 값은 기본적으로 True야.
#       •	"Hello" → 빈 문자열이 아님 → True
#       •	15 → 숫자이고 0이 아님 → True
#       •	[1, 2, 3] → 비어있지 않음 → True
#       •	" " → 공백도 문자열이므로 비어있지 않음 → True

#######################################
# 대부분의 가치는 참입니다
#######################################
# True거의 모든 가치는 어떤 종류의 내용이 있는지 에 따라 평가됩니다.
# True빈 문자열을 제외한 모든 문자열은 .입니다.
# 모든 숫자는 True, 를 제외하고 입니다 0.
# True비어 있는 것을 제외한 모든 목록, 튜플, 집합 및 사전은 입니다.

# 예
# 다음은 True를 반환합니다.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# True
# True
# True

#######################################
# 일부 값은 거짓입니다
#######################################
# 실제로 , , , , 숫자 , 값 과 False같은 빈 값을 제외하고는 로 평가되는 값은 많지 않습니다 . 물론 값은 로 평가됩니다 .()[]{}""0NoneFalseFalse

# 예
# 다음은 False를 반환합니다.
print(bool(False))   # False
print(bool(None))    # False
print(bool(0))       # False
print(bool(""))      # False
print(bool(()))      # False
print(bool([]))      # False
print(bool({}))      # False

# 이 경우 또 다른 값 또는 객체는 로 평가되며 , 이는 또는 를 반환하는 함수가 False있는 클래스에서 만들어진 객체가 있는 경우입니다 .__len__0False
# 예
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# False

#######################################
# 함수는 Boolean 값을 반환할 수 있습니다.
#######################################
# Boolean 값을 반환하는 함수를 만들 수 있습니다.
# 예
# 함수의 답을 출력하세요:
def myFunction() :
  return True

print(myFunction())
# True

# 함수의 Boolean 답변을 기반으로 코드를 실행할 수 있습니다
# 예
# 함수가 True를 반환하면 "YES!"를 출력하고, 그렇지 않으면 "NO!"를 출력합니다.
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
# YES!

# isinstance() Python에는 또한 객체가 특정 데이터 유형인지 확인하는 데 사용할 수 있는 함수 와 같이 부울 값을 반환하는 많은 내장 함수가 있습니다 .

# 예
# 객체가 정수인지 아닌지 확인하세요.
x = 200
print(isinstance(x, int))
# True

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# IWhat will be the result of the following syntax:
# print(5 > 3)?

# True      # Correct Answer!
# False
# 5 > 3
