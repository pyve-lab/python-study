####################################################################################
# 파이썬 매치
####################################################################################
# 이 match명령문은 다양한 조건에 따라 다양한 작업을 수행하는 데 사용됩니다.

#######################################
# 파이썬 매치 문
#######################################
# 여러 개의 문장을 쓰는 대신 문장을 if..else사용할 수 있습니다 match.
# 이 match명령문은 실행할 여러 코드 블록 중 하나를 선택합니다.

# Syntax
# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

# 작동 원리는 다음과 같습니다.

# 표현식 match은 한 번 평가됩니다.
# 표현식의 값은 각 값과 비교됩니다 case.
# 일치하는 것이 있으면 연관된 코드 블록이 실행됩니다.
# 아래 예에서는 요일 번호를 사용하여 요일 이름을 출력합니다.

# 예
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
# Thursday

#######################################
# 기본값
#######################################
# 다른 일치 항목이 없을 때 코드 블록을 실행하려면 밑줄 문자 _ 를 마지막 case 값으로 사용하세요.

# 예
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
# Looking forward to the Weekend

# 값 _ 는 항상 일치하므로 기본 케이스 처럼 동작하도록 하려면 마지막 케이스 에 배치하는 것이 중요합니다.

#######################################
# 값 결합
#######################################
# 케이스 평가에서 파이프 문자 |를 or 연산자로 사용하여 한 케이스 에서 두 개 이상의 값이 일치하는지 확인합니다 .

# 예
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
# Today is a weekday

#######################################
# 가드로서의 If 문
#######################################
# if케이스 평가에 추가 조건 검사로 문장을 추가할 수 있습니다.

# 예
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
# A weekday in May

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Which character can be used as a default case value in a match statement?

# %
# *
# _  # Correct Answer!
# |