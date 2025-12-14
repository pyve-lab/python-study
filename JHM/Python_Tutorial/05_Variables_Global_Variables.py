####################################################################################
# 파이썬 - 전역 변수
####################################################################################

#######################################
# 전역 변수 Global Variables
#######################################
# 함수 외부에서 생성된 변수(이전 페이지의 모든 예제처럼)를 전역 변수라고 합니다.
# 전역 변수는 함수 내부와 외부 모두에서 누구나 사용할 수 있습니다.

# 예
# 함수 외부에서 변수를 생성하고 함수 내부에서 사용합니다.
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
#Python is awesome

# 함수 내에서 같은 이름의 변수를 생성하면 해당 변수는 지역 변수가 되어 함수 내에서만 사용할 수 있습니다.
# 같은 이름의 전역 변수는 원래 값을 그대로 유지하며 전역 변수로 사용됩니다.

# 예
# 전역 변수와 동일한 이름으로 함수 내부에 변수를 생성합니다.
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
# Python is fantastic
# Python is awesome

#######################################
# 글로벌 키워드
#######################################
# 일반적으로 함수 내부에 변수를 생성하면 해당 변수는 지역 변수가 되어 해당 함수 내부에서만 사용할 수 있습니다.
# 함수 내부에 전역 변수를 생성하려면 global키워드를 사용하면 됩니다.

# 예
# 키워드를 사용하면 global변수는 전역 범위에 속합니다.
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
# Python is fantastic

# 또한, global함수 내에서 전역 변수를 변경하려면 키워드를 사용하세요.
# 예
# 함수 내에서 전역 변수의 값을 변경하려면 global다음 키워드를 사용하여 변수를 참조합니다.
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
# Python is fantastic
# HAM : 처음 x 로 선언했는데 global 로 함수 안에서 선언했고 결과값이 global 로 덮어 씌워진 것 같다

# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Exercise
# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Consider the following code:
x = 'awesome'
def myfunc():
    x = 'fantastic'
myfunc()
print('Python is ' + x)
# What will be the printed result?

# Python is awesome         # Correct Answer!
# Python is fantastic
