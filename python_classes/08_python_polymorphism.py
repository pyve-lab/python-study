
# =================================================================
# [1] 파이썬 다형성 기본 개념
# =================================================================

# "다형성"이란 "여러 형태를 가진다"는 의미이며,
# 동일한 이름의 메서드/함수/연산자가 서로 다른 객체나 클래스에서
# 각각 다르게 동작할 수 있는 특성을 의미합니다.



# =================================================================
# [2] 함수 다형성 - len() 함수 예시
# =================================================================

# len() 함수는 다양한 타입에 대해 서로 다르게 동작합니다.
# 예 : 

print("\n--- [문자열 len()] ---")
x = "Hello World!"
print(len(x))  # 문자열 길이


print("\n--- [튜플 len()] ---")
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # 항목 개수


print("\n--- [딕셔너리 len()] ---")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))  # key-value 키와 값의 쌍의 개수



# =================================================================
# [3] 클래스 다형성 - 동일한 메서드 이름 사용
# =================================================================

# 다형성(Polymorphism)은 주로 클래스 메서드에서 사용되며, 서로 다른 여러 클래스가 동일한 메서드 이름을 가질 수 있도록 합니다.
# 예를 들어, Car, Boat, Plane 이라는 세 개의 클래스가 있고, 이 클래스들은 모두 move() 라는 메서드를 가지고 있다고 가정해 보겠습니다.
# 예 :

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


print("\n--- [클래스 다형성 예시] ---")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()

# 마지막의 for 루프를 보면, 다형성 덕분에 세 클래스 모두에 대해 동일한 메서드를 실행할 수 있습니다.

# =================================================================
# [4] 상속 기반 클래스 다형성
# =================================================================

# 그렇다면 동일한 메서드 이름을 가진 자식 클래스를 포함하는 클래스의 경우는 어떨까요? 그 경우에도 다형성을 사용할 수 있을까요?
# 가능합니다. 위의 예시에서 Vehicle이라는 부모 클래스를 만들고, Car, Boat, Plane을 Vehicle의 자식 클래스로 만든다면, 
# 자식 클래스들은 Vehicle의 메서드를 상속받게 되지만, 이를 재정의(override) 할 수도 있습니다.
# Vehicle이라는 클래스를 만들고, Car, Boat, Plane을 Vehicle의 자식 클래스로 만드세요.
# 예 : 

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")


class Car(Vehicle):
  pass   # 부모의 move()를 그대로 사용


class Boat(Vehicle):
  def move(self):
    print("Sail!")  # 부모 메서드 오버라이드


class Plane(Vehicle):
  def move(self):
    print("Fly!")   # 부모 메서드 오버라이드


print("\n--- [상속 기반 다형성 예시] ---")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


# 자식 클래스는 부모 클래스의 속성과 메서드를 상속합니다.
# 위 예시에서 Car 클래스는 비어 있지만, Vehicle로부터 brand, model, move()를 상속받는 것을 볼 수 있습니다.
# Boat와 Plane 클래스도 Vehicle로부터 brand, model, move()를 상속받지만, 둘 다 move() 메서드를 재정의(override) 합니다.
# 다형성 덕분에 모든 클래스에 대해 동일한 메서드를 실행할 수 있습니다.
