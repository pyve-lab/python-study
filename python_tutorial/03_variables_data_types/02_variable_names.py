# Variable names
# 1. 파이썬 변수 이름 규칙
#변수는 짧은 이름(예: x 및 y)을 가질 수도 있고, 더 설명적인 이름(예: age, carname, total_volume)을 가질 수도 있습니다.
'''
Python 변수에 대한 규칙:
변수 이름은 문자 또는 밑줄 문자로 시작해야 합니다.
변수 이름은 숫자로 시작할 수 없습니다.
변수 이름에는 영숫자 문자와 밑줄(Az, 0-9, _)만 포함될 수 있습니다.
변수 이름은 대소문자를 구분합니다(age, Age 및 AGE는 세 개의 다른 변수입니다)
변수 이름은 Python 키워드 중 하나가 될 수 없습니다.
'''

# 2. 올바른 변수 이름 예제
myvar = 10
my_var = 20
_my_var = 30
myVar = 40
MYVAR = 50
myvar2 = 60

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# 3. 잘못된 변수 이름 예제(주석 처리된 부분은 오류를 발생시킵니다)
# 2myvar = 10    # 숫자로 시작하는 변수 이름
# my-var = 20   # 하이픈(-)이 포함된 변수 이름
# my var = 30   # 공백이 포함된 변수 이름
# my@var = 40   # 특수 문자(@)가 포함된 변수 이름
