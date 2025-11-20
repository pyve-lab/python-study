# Variable Exercises
# 1. 변수 연습 문제 풀기 
# 다음중 python 변수를 선언하는 올바른 방법은 무엇입니까? 
'''
var x = 5
#x = 5
$x = 5
x = 5

정답 : x = 5

'''

# 문자열 변수는 작은따옴표나 큰 따옴표로 선언할 수 있다. (O,X 문제)
'''
a = 'Hello'
b = "World"

정답 : O

'''

# 변수 이름은 대소문자를 구분하지 않습니다. (O,X 문제)
'''
a = 10
A = 20

정답 : X (대소문자를 구분합니다.)

'''

# 변수의 데이터 유형이 무엇인지 출력하기 위해 1번과 2번에 들어갈 올바른 함수를 선택하세요 
'''
( 1번 ( 2번 (myvar))

보기 : typ, type, var, print, echo

정답 : 1번 -print / 2번 - type

'''


# 2. 변수이름 연습문제
# 다음중 올바르지 않은 변수 이름은 무엇입니까?
'''
my-var = 20
my_var = 20
Myvar = 20
_myvar = 20

정답 : my-var = 20 (하이픈(-)은 변수 이름에 사용할 수 없습니다.)

'''

# carname이라는 변수를 만들고 Volvo라는 값을 할당하는 올바른 코드를 작성하세요.
'''
정답 : carname = "Volvo"

'''

# x라는 변수를 만들고 50을 할당하는 올바른 코드를 작성하세요.
'''
정답 : x = 50

'''


# 3. 여러 변수에 값 할당 연습문제
# 한 문장으로 3개의 변수에 'Hello World' 값을 추가하는 올바른 구문은 무엇입니까?
'''
x, y, z = 'Hello World'
x = y = z = 'Hello World'
x|y|z = 'Hello World'

정답 : x = y = z = 'Hello World'
'''

# 한 줄에 여러 변수에 값을 할당하기 위해 올바른 구문을 삽입하세요.
'''
x()y()z() = "orange" "banana" "cherry"
정답 : x, y, z = "orange", "banana", "cherry" (쉼표로 구분)

'''

# 다음 코드의 출력 결과는 무엇입니까?
'''
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)

정답 : apple

'''


# 4. 변수 출력 연습문제
# 다음 코드의 출력 결과는 무엇입니까?
'''
print('Hello', 'World')

정답 : Hello World (쉼표로 구분된 값들은 공백으로 구분되어 출력됩니다.)

'''

# 다음 코드의 출력 결과는 무엇입니까?
'''
a = 'Hello'
b = 'World'
print(a + b)

정답 : HelloWorld (문자열 연결 시 공백이 없음)

'''

# 다음 코드의 출력 결과는 무엇입니까?
'''
a = 4
b = 5
print(a + b)

정답 : 9 (숫자는 덧셈 연산이 수행됩니다.)

'''


# 5. 전역 변수 연습문제
# 다음 코드의 출력 결과는 무엇입니까?
'''
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

정답 : Python is awesome (함수 내에서 지역 변수 x가 생성되었지만 myfunc() 호출 후 print함수로 출력할 때는 전역 변수 x가 사용됩니다.)

'''

# 변수 x를 전역 범위에 속하게 하려면 괄호안에 어떤 키워드를 사용해야 합니까?
'''
def myfunc():
  
(   ) x
  x = "fantastic"
  
정답 : global

'''

# 다음 코드의 출력 결과는 무엇입니까?
'''
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

정답 : Python is fantastic (myfunc() 내에서 global 키워드를 사용하여 전역 변수 x를 수정하였기 때문에 출력 시 변경된 값이 반영됩니다.)

'''