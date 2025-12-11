
# =================================================================
# [1] self 매개변수 기본 개념
# =================================================================

# self 매개변수는 클래스의 현재 인스턴스를 참조합니다.
# 이를 통해 클래스에 속한 속성과 메서드에 접근할 수 있습니다.


# =================================================================
# [2] self를 이용한 클래스 속성 접근
# =================================================================

# 예:
# self를 사용하여 클래스 속성에 접근합니다.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

print("\n--- [self로 클래스 속성 접근] ---")
p1 = Person("Emil", 25)
p1.greet()

# 참고: self 매개변수는 클래스 내 모든 메서드의 첫 번째 매개변수여야 합니다.



# =================================================================
# [3] 왜 self를 사용하는가?
# =================================================================

# self가 없다면, 파이썬은 어떤 객체의 속성에 접근하려는 것인지 알 수 없습니다.
# self는 메서드를 특정 객체와 연결하는 역할을 합니다.

# 예:

class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

print("\n--- [self가 필요한 이유] ---")
p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()



# =================================================================
# [4] self라는 이름은 반드시 "self"일 필요는 없음
# =================================================================

# self는 단지 관례(convention)일 뿐이며,
# 첫 번째 매개변수 이름은 원하는 대로 지정해도 됩니다.
# 하지만 읽기 쉽고 이해하기 쉬우므로 self를 사용하는 것이 강력히 권장됩니다.

# 예:
# self 대신 myobject, abc 사용

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

print("\n--- [self 대신 다른 이름 사용] ---")
p1 = Person("Emil", 36)
p1.greet()



# =================================================================
# [5] self를 사용하여 속성에 접근
# =================================================================

# self를 사용하면 클래스의 모든 속성에 접근할 수 있습니다.

# 예:
# 여러 속성에 접근

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

print("\n--- [self로 여러 속성 접근] ---")
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()



# =================================================================
# [6] self를 사용하여 메서드 호출
# =================================================================

# 클래스 내부에서 다른 메서드를 호출할 때도 self를 사용합니다.

# 예:
# 한 메서드에서 다른 메서드를 호출

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

print("\n--- [self로 메서드 호출] ---")
p1 = Person("Tobias")
p1.welcome()
