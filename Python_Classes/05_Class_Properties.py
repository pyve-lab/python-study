####################################################################################
# 파이썬 클래스 속성
####################################################################################

#######################################
# 클래스 속성
#######################################
# 속성은 클래스에 속하는 변수입니다. 속성은 해당 클래스에서 생성된 각 객체에 대한 데이터를 저장합니다.

# 예
# 속성을 가진 클래스를 생성하세요:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
# Emil
# 36

#######################################
# 접근 속성
#######################################
# 점 표기법을 사용하여 객체의 속성에 접근할 수 있습니다.

# 예
# 객체의 속성에 접근합니다:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)
# Toyota
# Corolla

#######################################
# 속성 수정
#######################################
# 객체의 속성 값을 수정할 수 있습니다.

# 예
# 나이 속성을 변경하세요:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)
# 25

p1.age = 26
print(p1.age)
# 26

#######################################
# 속성 삭제
#######################################
# 키워드를 사용하여 객체의 속성을 삭제할 수 있습니다 del.
#
# 예
# 나이 속성을 삭제하세요:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# Linus
# print(p1.age) # This would cause an error
# Traceback (most recent call last):
#   File "05_Class_Properties.py", line 81, in <module>
#     print(p1.age) # This would cause an error
#           ^^^^^^
# AttributeError: 'Person' object has no attribute 'age'

#######################################
# 클래스 속성과 객체 속성 비교
#######################################
# 내부에 정의된 속성은 __init__()각 객체에 속합니다(인스턴스 속성).
# 메서드 외부에서 정의된 속성은 클래스 자체에 속하며(클래스 속성) 모든 객체가 공유합니다.

# 예
# 클래스 속성과 인스턴스 속성 비교:
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
# Emil
# Tobias
# Human
# Human

#######################################
# 클래스 속성 수정
#######################################
# 클래스 속성을 수정하면 모든 객체에 영향을 미칩니다.

# 예
# 클래스 속성을 변경합니다.
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)
# Refsnes
# Refsnes

#######################################
# 새 속성 추가
#######################################
# 기존 개체에 새 속성을 추가할 수 있습니다.

# 예
# 객체에 새 속성을 추가합니다.
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
# Tobias
# 25
# Oslo

# 참고: 이런 방식으로 속성을 추가하면 해당 특정 객체에만 속성이 추가되고, 클래스의 모든 객체에는 추가되지 않습니다.

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# How do you access a property of an object?

# Using parentheses: object(property)
# Using brackets: object[property]
# Using dot notation: object.property    # Correct Answer!


# 객체 속성 어렵다
# 객체 속성 = “그 객체가 가지고 있는 정보(특징)”
# 구분      예시
# 객체      혜민
# 속성      이름, 나이, 키, 직업
#