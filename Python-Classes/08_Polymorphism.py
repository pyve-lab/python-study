"""
==========================================================
📌 파이썬 다형성 (Polymorphism)
==========================================================

"다형성"은 말 그대로 "많은 형태"를 의미하며,
프로그래밍에서는 동일한 이름의 함수/메서드/연산자가
여러 객체에서 서로 다른 방식으로 동작할 수 있음을 의미한다.

✔ 같은 이름의 기능이 서로 다른 클래스/객체에서 다른 동작을 수행한다.
"""

"""
==========================================================
📌 1. 함수 다형성 (예: len())
==========================================================

파이썬의 내장 함수 len()은 다양한 객체 타입에서 다르게 동작한다.

예1) 문자열 → 문자 길이 반환
------------------------------

x = "Hello World!"
print(len(x))   # 12


예2) 튜플 → 요소 개수 반환
------------------------------

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))   # 3


예3) 딕셔너리 → key-value 쌍 개수 반환
------------------------------

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))   # 3

✔ 같은 함수 이름(len)이 다양한 객체에서 다르게 동작 → 다형성의 대표 예
"""
# 파이썬 함수 다형성 예시 (len 함수)

# 문자열
x = "Hello World!"
print(len(x))   # 12

# 튜플
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))   # 3

# 딕셔너리
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))   # 3

"""
==========================================================
📌 2. 클래스 다형성 (동일 메서드 이름 사용)
==========================================================

여러 클래스가 동일한 이름의 메서드를 가질 수 있으며,
이를 호출하면 해당 클래스에 맞는 동작이 실행된다.

예:

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

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

출력:
Drive!
Sail!
Fly!

✔ 같은 메서드 이름 move() 호출 → 각 클래스마다 다른 동작 수행  
✔ 다형성의 전형적인 형태
"""
# 파이썬 클래스 다형성 예시 (동일 메서드 이름 사용)

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

car1 = Car("Ford", "Mustang")        
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747") 

for x in (car1, boat1, plane1):
    x.move()

# 결과
# Drive!
# Sail!
# Fly!

"""
==========================================================
📌 3. 상속 기반 다형성 (Override)
==========================================================

자식 클래스가 부모 클래스의 메서드를 상속받지만,
동일한 메서드 이름으로 재정의(override)하여 다르게 동작할 수 있다.

예:

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass    # move() 그대로 상속

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

✔ Car: 부모 메서드 그대로 사용 (Move!)
✔ Boat & Plane: 부모 메서드 재정의하여 다른 출력 실행
✔ 상속 + 재정의 → 다형성의 중요한 형태
"""
# 파이썬 상속 기반 다형성 예시 (메서드 재정의)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass    # move() 그대로 상속

class Boat(Vehicle):
    def move(self):
        print("Sail!")  

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# 결과
# Ford
# Mustang
# Move!
# Ibiza
# Touring 20
# Sail!
# Boeing
# 747
# Fly!

"""
==========================================================
📌 정리
----------------------------------------------------------
- 다형성은 동일한 이름의 기능이 여러 객체에서 다른 동작을 수행하는 것.
- 내장 함수 len(), 다양한 컬렉션 타입에서 다른 결과 반환 → 함수 다형성
- 여러 클래스가 동일한 메서드 이름을 가질 수 있음 → 클래스 다형성
- 부모 클래스 메서드를 자식이 재정의(override) → 상속 기반 다형성
- for 루프 등으로 여러 객체를 순회하며 동일한 메서드를 호출해도 올바르게 작동

"""
