####################################################################################
# 파이썬 For 루프
####################################################################################

#######################################
# 파이썬 For 루프
#######################################
# for 루프 는 시퀀스(리스트, 튜플, 사전, 집합 또는 문자열)를 반복하는 데 사용됩니다.
# 이는 다른 프로그래밍 언어의 for 키워드와 덜 비슷하며, 다른 객체 지향 프로그래밍 언어에서 찾을 수 있는 반복자 메서드와 더 비슷하게 작동합니다.
# for 루프를 사용하면 목록, 튜플, 집합 등의 각 항목에 대해 한 번씩 명령문 세트를 실행할 수 있습니다.

# 예
# 과일 목록에 있는 각 과일을 인쇄하세요:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# apple
# banana
# cherry

# for 루프 는 인덱싱 변수를 미리 설정할 필요가 없습니다.

#######################################
# 문자열 반복
#######################################
# 문자열도 반복 가능한 객체이며, 문자열에는 일련의 문자가 포함됩니다.

# 예
# "banana"라는 단어의 글자를 반복하세요:
for x in "banana":
  print(x)
# b
# a
# n
# a
# n
# a

#######################################
# break 문
#######################################
# break 문을 사용하면 모든 항목을 반복하기 전에 루프를 중지할 수 있습니다.

# 예
# x"banana"가 나오면 루프를 종료합니다.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# apple
# banana

# 예
# "banana"가 나올 때 루프를 종료 x하지만 이번에는 break가 print보다 먼저 나옵니다.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# apple

#######################################
# continue 문
#######################################
# continue 문을 사용하면 루프의 현재 반복을 중지하고 다음 반복을 계속할 수 있습니다.
# 예
# 바나나를 인쇄하지 마세요:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# apple
# cherry

#######################################
# range() 함수
#######################################
# 지정된 횟수만큼 코드 세트를 반복하려면 다음 range()함수를 사용할 수 있습니다.
# 이 range()함수는 기본적으로 0부터 시작하여 1씩 증가하는(기본값) 숫자 시퀀스를 반환하고 지정된 숫자에서 끝납니다.

# 예
# range() 함수를 사용합니다.
for x in range(6):
  print(x)
# 0
# 1
# 2
# 3
# 4
# 5

# range(6)0~6의 값이 아니라 0~5의 값이라는 점에 유의하세요.

# 이 range()함수는 기본적으로 시작 값으로 0을 사용하지만 매개변수를 추가하여 시작 값을 지정할 수 있습니다.
# range(2, 6)즉, 2에서 6까지의 값(6은 제외)을 지정할 수 있습니다.

# 예
# 시작 매개변수 사용:
for x in range(2, 6):
  print(x)
# 2
# 3
# 4
# 5

# 이 range()함수는 기본적으로 시퀀스를 1씩 증가시키지만 세 번째 매개변수를 추가하여 증가 값을 지정할 수 있습니다 .range(2, 30, 3)

# 예
# 시퀀스를 3씩 증가시킵니다(기본값은 1):
for x in range(2, 30, 3):
  print(x)
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29

#######################################
# For 루프의 Else
#######################################
# else루프 의 키워드는 루프 for가 완료될 때 실행될 코드 블록을 지정합니다.

# 예
# 0부터 5까지의 모든 숫자를 출력하고, 루프가 끝나면 메시지를 출력합니다.
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

# 참고:else 루프가 명령문에 의해 중지되면 블록은 실행되지 않습니다 break.

# 예
# 3이 되면 루프를 끊고 블록 x에서 무슨 일이 일어나는지 살펴보세요 else.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2

#######################################
# 중첩 루프
#######################################
# 중첩 루프는 루프 안에 있는 루프입니다.
# "내부 루프"는 "외부 루프"의 각 반복마다 한 번씩 실행됩니다.

# 예
# 각 과일에 대한 형용사를 각각 출력하세요:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

#######################################
# 패스 진술 The pass Statement
#######################################
# for루프는 비어 있을 수 없지만, 어떤 이유로든 for내용이 없는 루프가 있는 경우 pass오류를 방지하기 위해 명령문을 넣으세요.

# 예
for x in [0, 1, 2]:
  pass


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What will be the result of the following code:
for x in range(3):
  print(x)

# Correct Answer!
# 0
# 1
# 2

# 0
# 1
# 2
# 3

# 1
# 2
# 3