# Output Variables
# 1. 파이썬 변수 출력
# 변수를 출력하려면 print() 함수를 사용합니다.
x = "Hello, Python!"
print(x)
# 함수에서는 쉼표 (,)를 사용하여 여러 변수를 한 번에 출력할 수 있습니다.
y = "Welcome to the world of programming."
print(x, y)

a = 10
b = 20
print("The value of a is", a, "and the value of b is", b)

# 2. 연산자를 사용한 변수 출력
# 변수와 함께 연산자를 사용하여 출력할 수도 있습니다.
x = "python "
y = "is "
z = "awesome"
print(x + y + z)  # 문자열 연결
# "Python "and 뒤에 있는 공백 문자에 주목하세요. 공백 문자 "is "가 없으면 결과는 "Pythonisawesome"이 됩니다.
#print(x + " " + y + " " + z)  # 공백을 직접 추가하여 문자열 연결

# 숫자의 경우 + 문자는 수학 연산자로 작동합니다.
x = 5
y = 10
print(x + y)  # 숫자 덧셈

# 문자열과 숫자를 결합하려고 하면 오류가 발생합니다.
x = "The answer is"
y = 42
# print(x + y)  # 오류 발생
# 함수 에서 여러 변수를 출력하는 가장 좋은 방법은 쉼표로 구분하는 것입니다. 쉼표는 다양한 데이터 유형을 지원합니다.
print(x,y)  # 올바른 출력