####################################################################################
# 파이썬 Try Except
####################################################################################

# 블록 try을 사용하면 코드 블록의 오류를 테스트할 수 있습니다.
# 블록 except을 사용하면 오류를 처리할 수 있습니다.
# 이 else블록을 사용하면 오류가 없을 때 코드를 실행할 수 있습니다.
# 이 finally블록을 사용하면 try 및 except 블록의 결과에 관계없이 코드를 실행할 수 있습니다.

#######################################
# 예외 처리
#######################################
# 오류가 발생하거나 예외라고 부르는 경우 Python은 일반적으로 중지되고 오류 메시지를 생성합니다.
# 이러한 예외는 다음 명령문을 사용하여 처리할 수 있습니다 try.

# 예
# 블록 은 정의되지 않았기 try때문에 예외를 생성합니다 .x

try:
  print(x)
except:
  print("An exception occurred")
# An exception occurred

# try 블록에서 오류가 발생하므로 except 블록이 실행됩니다.
# try 블록이 없으면 프로그램이 충돌하고 오류가 발생합니다.

# 예
# x이 문장은 정의되지 않았기 때문에 오류를 발생시킵니다 .
# print(x)     오류임

#######################################
# 많은 예외
#######################################
# 원하는 만큼 많은 예외 블록을 정의할 수 있습니다. 예를 들어, 특정 종류의 오류에 대해 특수 코드 블록을 실행하려는 경우:

# 예
# try 블록에서 오류가 발생하면 하나의 메시지를 출력하고 NameError다른 오류가 발생하면 다른 메시지를 출력합니다.
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# Variable x is not defined

# Python 내장 예외 참조 에서 더 많은 오류 유형을 확인하세요.

#######################################
# 또 다른 else
#######################################
# else오류가 발생하지 않은 경우 실행할 코드 블록을 정의하려면 키워드를 사용할 수 있습니다 .

# 예
# 이 예에서 try블록은 어떠한 오류도 생성하지 않습니다.
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Hello
# Nothing went wrong

#######################################
# 마지막으로 finally
#######################################
# finally블록이 지정된 경우, try 블록에서 오류가 발생하는지 여부에 관계없이 해당 블록이 실행됩니다.

# 예
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# Something went wrong
# The 'try except' is finished

# 이는 객체를 닫고 리소스를 정리하는 데 유용할 수 있습니다.

# 예
# 쓰기가 불가능한 파일을 열어서 써보세요.
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
# Something went wrong when opening the file

# 프로그램은 파일 객체를 열어두지 않고도 계속 진행될 수 있습니다.

#######################################
# 예외를 발생시키다
#######################################
# Python 개발자는 조건이 발생하면 예외를 발생시키도록 선택할 수 있습니다.
# 예외를 발생시키려면 raise키워드를 사용합니다.

# 예
# x가 0보다 작으면 오류를 발생시키고 프로그램을 중지합니다.

# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")
# 오류남;;;;;;;;;;;

# 키워드 raise는 예외를 발생시키는 데 사용됩니다.
# 어떤 종류의 오류를 발생시킬지 정의하고, 사용자에게 인쇄할 텍스트를 지정할 수 있습니다.

# 예
# x가 정수가 아닌 경우 TypeError를 발생시킵니다.

# x = "hello"
#
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")
# 위에랑 똑같은 오류남;;;;;;;;;;;;


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# In a try...except block, there is a certain block that if specified,
# will be executed regardless if the try block raises an error or not.
# What is the name of this block?

# finally          # Correct Answer!
# last
# allways