"""
==========================================================
📌 자기 매개변수 (self)
==========================================================

self 매개변수는 '클래스의 현재 인스턴스(객체)'를 가리키는 참조이다.
즉, 객체 자신의 속성과 메서드에 접근할 때 사용된다.

모든 인스턴스 메서드의 첫 번째 매개변수여야 한다.
"""

"""
==========================================================
📌 1. self를 사용해 속성에 접근하기
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

✔ self.name → 현재 객체의 name 속성을 의미한다.
"""
# 파이썬 self를 사용한 속성 접근

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()  # Hello, my name is Emil

"""
==========================================================
📌 2. 왜 self가 필요한가?
==========================================================

self가 없다면 Python은 어떤 객체의 속성에 접근해야 하는지 알 수 없다.

예:

class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

✔ 각 객체마다 다른 name 값을 가진다.
✔ self는 메서드가 특정 객체와 연결되어 실행된다는 의미이다.
"""
# 파이썬 self의 필요성 예시

class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")
p1.printname()  # Tobias
p2.printname()  # Linus

"""
==========================================================
📌 3. self라는 이름은 고정이 아니다
==========================================================

첫 번째 매개변수의 이름은 무엇이든 가능하지만,
관례적으로 self를 사용한다.

예:

class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

✔ 어떤 이름도 가능하지만 self 사용이 가독성이 가장 좋다.
"""
# 파이썬 self 대체 이름 예시

class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()  # Hello, my name is Emil

"""
==========================================================
📌 4. self로 여러 속성에 접근하기
==========================================================

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

✔ self.brand, self.model, self.year → 모두 현재 객체의 속성에 접근.
"""
# 파이썬 self로 여러 속성 접근

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()  # 2020 Toyota Corolla

"""
==========================================================
📌 5. self로 메서드 간 호출하기
==========================================================

클래스 내부에서 다른 메서드를 호출할 때도 self를 사용한다.

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

✔ self.greet() → 현재 객체의 greet 메서드 호출.
"""
# 파이썬 self로 메서드 간 호출

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")
        
p1 = Person("Tobias")
p1.welcome()  # Hello, Tobias! Welcome to our website.

"""
==========================================================
📌 정리
----------------------------------------------------------
- self는 객체 자신을 의미한다.
- 속성 및 메서드 접근 시 반드시 self를 사용한다.
- 첫 번째 매개변수 이름은 자유지만 self가 관례이자 가장 추천되는 방식이다.
- 메서드 내부에서 다른 메서드를 호출할 때도 self를 사용한다.
"""
