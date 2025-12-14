####################################################################################
# 파이썬 캡슐화
####################################################################################

#######################################
# 파이썬 캡슐화
#######################################
# 캡슐화는 클래스 내부의 데이터를 보호하는 것입니다.

# 이는 데이터(속성)와 메서드를 클래스 안에 함께 유지하면서 클래스 외부에서 데이터에 접근하는 방식을 제어하는 것을 의미합니다.
# 이렇게 하면 데이터가 실수로 변경되는 것을 방지하고 클래스가 작동하는 방식에 대한 내부 세부 정보를 숨길 수 있습니다.

#######################################
# 개인 소유지  Private Properties
#######################################
# 파이썬에서는 이중 밑줄 __접두사를 사용하여 속성을 비공개로 설정할 수 있습니다.

# 예
# 다음과 같은 이름의 비공개 클래스 속성을 생성합니다 __age.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
# Emil
# print(p1.__age) # This will cause an error
# Traceback (most recent call last):
#   File "09_Encapsulation.py", line 27, in <module>
#     print(p1.__age) # This will cause an error
#           ^^^^^^^^
# AttributeError: 'Person' object has no attribute '__age'

# 참고: 비공개 속성은 클래스 외부에서 직접 접근할 수 없습니다.

#######################################
# 개인 소유 부동산 가치를 알아보세요 Get Private Property Value
#######################################
# 비공개 속성에 접근하려면 getter 메서드를 만들 수 있습니다.

# 예
# 비공개 속성에 접근하려면 getter 메서드를 사용하세요.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())
# 25

#######################################
# 사유재산 가치 설정 Set Private Property Value
#######################################
# 비공개 속성을 수정하려면 setter 메서드를 만들 수 있습니다.
# setter 메서드는 값을 설정하기 전에 유효성을 검사할 수도 있습니다.

# 예
# private 속성을 변경하려면 setter 메서드를 사용하세요.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())
# 25

p1.set_age(26)
print(p1.get_age())
# 26

#######################################
# 캡슐화를 사용하는 이유는 무엇일까요?
#######################################
# 캡슐화는 다음과 같은 여러 가지 이점을 제공합니다.

# 데이터 보호: 데이터의 우발적인 변경을 방지합니다.
# 유효성 검사: 데이터를 설정하기 전에 유효성을 검사할 수 있습니다.
# 유연성: 내부 구현을 변경해도 외부 코드에 영향을 미치지 않습니다.
# 제어: 데이터에 접근하고 수정하는 방식을 완벽하게 제어할 수 있습니다.

# 예
# 캡슐화를 사용하여 데이터를 보호하고 유효성을 검사하세요.
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
# 85
# Passed

#######################################
# 보호 대상 재산 Private Properties
#######################################
# 파이썬은 또한 보호된 속성에 대해 하나의 밑줄 접두사를 사용하는 관례를 가지고 있습니다 _.

# 예
# 보호된 속성을 생성하세요:
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't
# Linus
# 50000

# 참고: 밑줄 하나는 _단지 관례일 뿐입니다. 다른 프로그래머에게 해당 속성이 내부용으로만 사용될 것임을 알려주는 역할을 하지만, 파이썬은 이러한 제한을 강제하지는 않습니다.

#######################################
# 비공개 메서드
#######################################
# 메서드를 비공개로 설정하려면 이중 밑줄 접두사를 사용할 수도 있습니다.

# 예
# 비공개 메서드를 생성하세요:
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# 15

# calc.__validate(5) # This would cause an error
# 참고: 이중 밑줄로 표시되는 비공개 속성과 마찬가지로 비공개 메서드는 클래스 외부에서 직접 호출할 수 없습니다. 해당 __validate메서드는 클래스 내부의 다른 메서드에서만 사용할 수 있습니다.

#######################################
# 이름 망글링 Name Mangling
#######################################
# 이름 변환은 파이썬이 비공개 속성과 메서드를 구현하는 방식입니다.
# 이중 밑줄을 사용하면 파이썬은 자동으로 내부적으로 앞에 __를 추가하여 이름을 변경합니다 ._ClassName
# 예를 들어, __age는 로 바뀝니다 _Person__age.

# 예
# 파이썬이 이름을 어떻게 왜곡하는지 보세요:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!
# 참고: 변형된 이름을 사용하여 비공개 속성에 접근 할 수는 있지만 권장하지 않습니다. 이는 캡슐화의 목적에 어긋나기 때문입니다.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# How do you make a property private in Python?

# Use a single underscore prefix: _property
# Use a double underscore prefix: __property     # Correct Answer!
# Use the private keyword