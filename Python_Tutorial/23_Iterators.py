####################################################################################
# 파이썬 반복자
####################################################################################

#######################################
# 파이썬 반복자
#######################################
# 반복자는 셀 수 있는 개수의 값을 담고 있는 객체입니다.
# 반복자는 반복 가능한 객체로, 모든 값을 탐색할 수 있다는 의미입니다.
# 기술적으로, 파이썬에서 반복자는 반복자 프로토콜을 구현하는 객체이며,
# 이 프로토콜은 . __iter__() 과 . 메서드로 구성됩니다 __next__().

#######################################
# 반복자 vs 반복 가능
#######################################
# 리스트, 튜플, 딕셔너리, 그리고 세트는 모두 반복 가능한 객체입니다. 이들은 반복 가능한 컨테이너 이며, 반복자를 가져올 수 있습니다.
# 이러한 모든 객체에는 iter()반복자를 가져오는 데 사용되는 메서드가 있습니다.

# 예
# 튜플에서 반복자를 반환하고 각 값을 인쇄합니다.
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# apple
# banana
# cherry

# 문자열도 반복 가능한 객체이며 반복자를 반환할 수 있습니다.

# 예
# 문자열은 문자 시퀀스를 포함하는 반복 가능한 객체이기도 합니다.
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# b
# a
# n
# a
# n
# a

#######################################
# 반복자를 통한 루프
#######################################
# for반복 가능한 객체를 반복하기 위해 루프를 사용할 수도 있습니다.

# 예
# 튜플의 값을 반복합니다.
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
# apple
# banana
# cherry

# 예
# 문자열의 문자를 반복합니다.
mystr = "banana"

for x in mystr:
  print(x)
# b
# a
# n
# a
# n
# a

# 루프는 for실제로 반복자 객체를 생성하고 next() 각 루프에 대한 메서드를 실행합니다.

#######################################
# 반복자 만들기
#######################################
# 객체/클래스를 반복자로 생성하려면 해당 객체에 대한 __iter__()메서드 를 구현해야 합니다. __next__()
# Python 클래스/객체 장 에서 배우게 되겠지만 , 모든 클래스 __init__()에는 객체가 생성될 때 초기화를 수행할 수 있는 함수가 있습니다.
# 이 __iter__()메서드는 비슷하게 동작합니다. 초기화 등의 작업을 수행할 수 있지만 항상 반복자 객체 자체를 반환해야 합니다.
# 이 __next__()메서드를 사용하면 작업을 수행할 수 있으며 시퀀스의 다음 항목을 반환해야 합니다.

# 예
# 1부터 시작하여 각 시퀀스가 ​​1씩 증가하는(1, 2, 3, 4, 5 등을 반환하는) 숫자를 반환하는 반복자를 만듭니다.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# b
# a
# n
# a
# n
# a
# 1
# 2
# 3
# 4
# 5

#######################################
# 반복 중지
#######################################
# 위의 예제는 next() 문이 충분하거나 for루프에서 사용되는 경우 영원히 계속됩니다.
#
# 반복이 영원히 계속되는 것을 방지하려면 다음 StopIteration명령문을 사용할 수 있습니다.
#
# 이 __next__()방법에서는 반복이 지정된 횟수만큼 수행되면 오류를 발생시키는 종료 조건을 추가할 수 있습니다.
#
# 예
# 20번 반복 후 중지:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
# 1
# 2
# 3
# 4
# 5
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# There are two methods that you have to implement when you create an iterator, which two?

# __iter__() and __next__()      # Correct Answer!
# __next__() and __prev__()
# __init__() and __end__()