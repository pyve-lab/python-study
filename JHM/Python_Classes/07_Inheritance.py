####################################################################################
# 파이썬 상속
####################################################################################

#######################################
# 파이썬 상속
#######################################
# 상속을 통해 우리는 다른 클래스의 모든 메서드와 속성을 상속받는 클래스를 정의할 수 있습니다.
# 부모 클래스 는 상속받는 클래스로, 기본 클래스라고도 합니다.
# 자식 클래스 는 다른 클래스로부터 상속받는 클래스이며, 파생 클래스라고도 합니다.

#######################################
# 부모 클래스를 생성하세요
#######################################
# 어떤 클래스든 부모 클래스가 될 수 있으므로 구문은 다른 클래스를 생성하는 것과 동일합니다.

# 예
# `<class>`라는 이름의 클래스를 만들고 Person, ` <property> firstname` 및 ` lastname<property>` 속성과 ` printname<method>` 메서드를 생성하세요.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
# John Doe

#######################################
# 자식 클래스를 생성합니다
#######################################
# 다른 클래스의 기능을 상속받는 클래스를 만들려면 자식 클래스를 생성할 때 부모 클래스를 매개변수로 전달하세요.

# 예
# Student클래스 의 속성과 메서드를 상속받는 라는 이름의 클래스를 생성하세요 Person.
class Student(Person):
  pass
# 참고:pass 클래스에 다른 속성이나 메서드를 추가하지 않으려는 경우 `--` 키워드를 사용하십시오 .

# 이제 Student 클래스는 Person 클래스와 동일한 속성과 메서드를 갖게 되었습니다.

# 예
# 해당 Student클래스를 사용하여 객체를 생성한 다음 printname메서드를 실행하세요.
x = Student("Mike", "Olsen")
x.printname()
# Mike Olsen

#######################################
# __init__() 함수를 추가하세요
#######################################
# 지금까지 우리는 부모 클래스의 속성과 메서드를 상속받는 자식 클래스를 만들었습니다.
# __init__()키워드 대신 자식 클래스에 함수를 추가하고 싶습니다 pass.

# 참고: 이 __init__()함수는 해당 클래스를 사용하여 새 객체를 생성할 때마다 자동으로 호출됩니다.

# 예
# __init__()클래스 에 함수를 추가하세요 Student:
# class Student(Person):
#   def __init__(self, fname, lname):
    #add properties etc.
# 해당 함수를 추가하면 __init__()자식 클래스는 더 이상 부모 클래스의 __init__()함수를 상속받지 않습니다.
# 참고: 자식 클래스의 __init__() 함수는 부모 클래스의 함수 상속을 재정의합니다 __init__() .

# 부모 클래스의 __init__() 함수 상속을 유지하려면 부모 클래스의 __init__()함수를 호출하는 코드를 추가하세요.

# 예
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# 이제 함수를 성공적으로 추가했고 __init__(), 부모 클래스의 상속도 유지했으므로, __init__()함수 내에 기능을 추가할 준비가 되었습니다.

#######################################
# super() 함수를 사용하세요
#######################################
# super()파이썬에는 자식 클래스가 부모 클래스의 모든 메서드와 속성을 상속받도록 하는 함수 도 있습니다.

# 예
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
# 이 함수를 사용하면 super()부모 요소의 이름을 지정할 필요가 없으며, 부모 요소로부터 메서드와 속성을 자동으로 상속받습니다.

#######################################
# 속성 추가
#######################################
# 예
# graduationyear클래스 에 라는 속성을 추가하세요 Student:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
# 아래 예시에서 연도는 2019변수여야 하며, Student학생 객체를 생성할 때 클래스에 전달되어야 합니다. 이를 위해 __init__()함수에 매개변수를 하나 더 추가하세요.

# 예
# 매개변수를 추가하고 year객체를 생성할 때 올바른 연도를 전달하세요.
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#######################################
# 메서드 추가
#######################################
# 예
# welcome클래스 에 다음과 같은 메서드를 추가하세요 Student:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# 자식 클래스에 부모 클래스의 함수와 동일한 이름의 메서드를 추가하면 부모 메서드의 상속이 덮어쓰여집니다.

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the correct keyword to use inside an empty class, to avoid getting an error?

# empty
# inherit
# pass     # Correct Answer!