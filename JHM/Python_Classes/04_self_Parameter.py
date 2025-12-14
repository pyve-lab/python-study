####################################################################################
# 파이썬 자체 매개변수
####################################################################################

#######################################
# 자체 매개변수
#######################################
# 해당 self매개변수는 클래스의 현재 인스턴스에 대한 참조입니다.
# 클래스에 속하는 속성과 메서드에 접근하는 데 사용됩니다.

# 예
# self클래스 속성에 접근하는 데 사용합니다.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()
# Hello, my name is Emil
# 참고: 해당 self매개변수는 클래스 내 모든 메서드의 첫 번째 매개변수여야 합니다.

#######################################
# 왜 자기 자신을 사용해야 할까요?
#######################################
# ` --`가 없으면 self파이썬은 어떤 객체의 속성에 접근하려는지 알 수 없습니다.

# 예
# 이 self매개변수는 메서드를 특정 객체와 연결합니다.
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()
# Tobias
# Linus

#######################################
# 자아는 반드시 "자아"라고 명명될 필요는 없습니다.
#######################################
# 반드시 이름을 붙일 필요는 없으며 self, 원하는 이름으로 지정할 수 있지만,
# 클래스 내 모든 메서드의 첫 번째 매개변수여야 합니다.

# 예
# self 대신 myobject 와 abc라는 단어를 사용하세요.
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()
# Hello, my name is Emil
# 참고: 다른 이름을 사용할 수도 있지만 , self파이썬의 관례에 따라 사용하는 것이 좋으며, 이렇게 하면 다른 사람이 코드를 더 쉽게 읽을 수 있습니다.

#######################################
# 셀프를 사용하여 속성에 액세스
#######################################
# 클래스의 모든 속성은 다음을 사용하여 접근할 수 있습니다 self.

# 예
# 다음을 사용하여 여러 속성에 액세스합니다 self.
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()
# 2020 Toyota Corolla

#######################################
# self를 사용하여 메서드 호출
#######################################
# 클래스 내의 다른 메서드를 다음과 같이 호출할 수도 있습니다 self.

# 예
# 메서드 내에서 다른 메서드를 호출하려면 다음을 사용하세요 self.
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()
# Hello, Tobias! Welcome to our website.

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What does the self parameter represent in a Python class?

# The class name
# A reference to the current instance of the class. # Correct Answer!
# A global variable

# 클래스의 현재 인스턴스에 대한 참조입니다. -> 이게 무슨 말이야..
# - self는 클래스 이름도 아니고
# - self는 전역 변수도 아니고
# - self는 -> “이 메서드를 호출한 객체 자기 자신”