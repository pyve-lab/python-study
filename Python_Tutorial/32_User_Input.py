####################################################################################
# 파이썬 사용자 입력
####################################################################################

#######################################
# 사용자 입력
#######################################
# Python에서는 사용자 입력이 가능합니다.
# 즉, 사용자에게 입력을 요청할 수 있다는 뜻입니다.

# 다음 예에서는 이름을 입력하라는 메시지가 표시되고, 이름을 입력하면 화면에 이름이 출력됩니다.
# 예
# 사용자 의견을 요청하세요:
print("Enter your name:")
name = input()
print(f"Hello {name}")
# Enter your name:
# Ham
# Hello Ham

# Python은 함수에 도달하면 실행을 멈추고 input(), 사용자가 입력을 하면 실행을 계속합니다.

#######################################
# 프롬프트 사용
#######################################
# 위 예에서 사용자는 새 줄에 이름을 입력해야 했습니다. Python input()함수에는 매개변수가 있는데 prompt, 이 매개변수는 같은 줄에 사용자 입력 앞에 넣을 수 있는 메시지 역할을 합니다.

# 예
# 사용자 입력 앞에 메시지를 추가합니다.
name = input("Enter your name:")
print(f"Hello {name}")
# Enter your name:Ham
# Hello Ham

#######################################
# 다중 입력
#######################################
# 원하는 만큼 많은 입력을 추가할 수 있으며, Python은 각 입력에서 실행을 멈추고 사용자 입력을 기다립니다.

# 예
# 다중 입력:
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
# Enter your name:Ham
# Hello Ham
# What is your favorite animal:Tiger
# What is your favorite color:Violet
# What is your favorite number:3
# Do you want a Violet Tiger with 3 legs?

#######################################
# 입력 번호
#######################################
# 사용자 입력은 문자열로 처리됩니다. 위 예제에서 숫자를 입력하더라도 Python 인터프리터는 여전히 숫자를 문자열로 처리합니다.
# 다음 함수 를 사용하여 입력을 숫자로 변환할 수 있습니다 float().

# 예
# 제곱근을 구하려면 입력값을 숫자로 변환해야 합니다.
import math

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")
# Enter a number:3
# The square root of 3 is 1.7320508075688772

#######################################
# 입력 검증
#######################################
# 사용자의 모든 입력을 검증하는 것이 좋습니다. 위 예에서 사용자가 숫자가 아닌 다른 값을 입력하면 오류가 발생합니다.
# 오류를 방지하기 위해 입력을 테스트할 수 있으며, 숫자가 아닌 경우 사용자는 "잘못된 입력입니다. 다시 시도해 보세요"와 같은 메시지를 받고 새로운 입력을 할 수 있습니다.

# 예
# 번호를 받을 때까지 계속 물어보세요.
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")
# 좋은 예
# Enter a number:3
# Thank you!

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the name of the method used to ask for user input?

# prompt()
# input()     # Correct Answer!
# user()