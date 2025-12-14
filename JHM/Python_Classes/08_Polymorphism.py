####################################################################################
# 파이썬 다향성
####################################################################################
# "다형성"이라는 단어는 "다양한 형태"를 의미하며, 프로그래밍에서는 동일한 이름을 가진 메서드/함수/연산자가 여러 객체나 클래스에서 실행될 수 있는 것을 가리킵니다.

#######################################
# 함수 다형성
#######################################
# 다양한 객체에 사용할 수 있는 파이썬 함수의 예로는 ` len()__init__` 함수가 있습니다.

# String
# 문자열의 경우 len()문자 수를 반환합니다.

# 예
x = "Hello World!"

print(len(x))


# 튜플
# 튜플의 경우 len()튜플에 포함된 항목의 개수를 반환합니다.

# 예
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))
# 3

# 딕셔너리
# 딕셔너리의 경우, len()딕셔너리에 있는 키/값 쌍의 개수를 반환합니다.

# 예
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
# 3

#######################################
# 클래스 다형성
#######################################
# 다형성은 클래스 메서드에서 자주 사용되며, 동일한 메서드 이름을 가진 클래스가 여러 개 있을 수 있습니다.

# Car예를 들어, 세 개의 클래스( , Boat, ) 가 있고 Plane, 이 클래스들 모두 라는 메서드를 가지고 있다고 가정해 봅시다 move().

# 예
# 동일한 메서드를 가진 다른 클래스:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# Drive!
# Sail!
# Fly!

# 마지막에 있는 for 루프를 보세요. 다형성 덕분에 세 클래스 모두에 대해 동일한 메서드를 실행할 수 있습니다.

#######################################
# 상속 클래스 다형성
#######################################
# 자식 클래스의 이름이 같은 클래스는 어떻게 되나요? 그런 경우에도 다형성을 사용할 수 있나요?

# 네. 위 예시를 사용하여 부모 클래스를 만들고 Vehicle, 자식 클래스 로 Car, , 를 만들면 Boat, 자식 클래스는 부모 클래스의 메서드를 상속받지만, 오버라이드할 수도 있습니다.PlaneVehicleVehicle

# 예
# 라는 클래스를 만들고 , , , 와 같은 자식 클래스를 Vehicle만드세요 :CarBoatPlaneVehicle
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
# Ford
# Mustang
# Move!
# Ibiza
# Touring 20
# Sail!
# Boeing
# 747
# Fly!

# 자식 클래스는 부모 클래스의 속성과 메서드를 상속받습니다.
# 위 예시에서 Car클래스가 비어 있지만 brand, , model, 및 move()를 상속받는 것을 볼 수 있습니다 Vehicle.
# 및 클래스는 또한 에서 , , 및 Boat를 상속받지만 , 둘 다 메서드를 재정의합니다.Planebrandmodelmove()Vehiclemove()
# 다형성 덕분에 모든 클래스에 대해 동일한 메서드를 실행할 수 있습니다.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# True or False. One object cannot have a method with the same name as another object's method.

# True
# False

# Correct Answer!