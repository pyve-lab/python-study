"""
==========================================================
📌 클래스 속성 & 객체(인스턴스) 속성
==========================================================

속성(property)은 클래스 또는 객체에 저장되는 변수이다.

✔ 인스턴스 속성(instance property)
    - __init__() 내부에서 self로 정의됨
    - 각 객체마다 개별적으로 존재

✔ 클래스 속성(class property)
    - 메서드 밖에서 정의됨
    - 모든 객체가 공유
"""

"""
==========================================================
📌 1. 기본 인스턴스 속성 정의하기
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

✔ self.name, self.age → 객체마다 고유한 속성
"""
# 파이썬 인스턴스 속성 정의

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1.name)  # Emil
print(p1.age)   # 36

"""
==========================================================
📌 2. 속성 접근 (점 표기법)
==========================================================

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

✔ 객체명.속성명 으로 접근
"""
# 파이썬 객체 속성 접근 (점 표기법)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)  # Toyota
print(car1.model)  # Corolla

"""
==========================================================
📌 3. 속성 수정하기
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tobias", 25)
print(p1.age)   # 25

p1.age = 26
print(p1.age)   # 26

✔ 객체 속성 값은 언제든 변경 가능
"""
# 파이썬 객체 속성 수정

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Tobias", 25)
print(p1.age)   # 25

p1.age = 26
print(p1.age)   # 26

"""
==========================================================
📌 4. 속성 삭제하기 (del 키워드)
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name)   # 정상 출력
# print(p1.age)  # 에러 발생 (삭제됨)

✔ 특정 객체에서만 속성이 제거됨
"""
# 파이썬 객체 속성 삭제

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 30)
del p1.age
print(p1.name)   # Linus
print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'

"""
==========================================================
📌 5. 클래스 속성과 인스턴스 속성의 차이
==========================================================

class Person:
    species = "Human"   # 클래스 속성

    def __init__(self, name):
        self.name = name  # 인스턴스 속성

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)     # Emil
print(p2.name)     # Tobias
print(p1.species)  # Human
print(p2.species)  # Human

✔ species는 클래스 속성이므로 모든 객체가 공유한다.
"""
# 파이썬 클래스 속성과 인스턴스 속성 차이

class Person:
    species = "Human"   # 클래스 속성

    def __init__(self, name):
        self.name = name  # 인스턴스 속성

p1 = Person("Emil")
p2 = Person("Tobias")
print(p1.name)     # Emil
print(p2.name)     # Tobias
print(p1.species)  # Human
print(p2.species)  # Human

"""
==========================================================
📌 6. 클래스 속성 수정하기 (모든 객체 영향)
==========================================================

class Person:
    lastname = ""   # 클래스 속성

    def __init__(self, name):
        self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)  # Refsnes
print(p2.lastname)  # Refsnes

✔ 클래스 속성 변경 → 모든 객체에서 값이 바뀜
"""
# 파이썬 클래스 속성 수정 (모든 객체 영향)

class Person:
    lastname = ""   # 클래스 속성

    def __init__(self, name):
        self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)  # Refsnes
print(p2.lastname)  # Refsnes

"""
==========================================================
📌 7. 객체에 새로운 속성 동적으로 추가
==========================================================

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

✔ 이렇게 추가한 속성은 그 객체에만 존재한다.
✔ 다른 객체는 해당 속성을 가지지 않는다.
"""
# 파이썬 객체에 동적으로 새로운 속성 추가

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Tobias")
p1.age = 25
p1.city = "Oslo"

print(p1.name) # Tobias
print(p1.age)  # 25
print(p1.city) # Oslo

"""
==========================================================
📌 정리
----------------------------------------------------------
- 인스턴스 속성: 객체마다 독립적, __init__ 내부에서 정의.
- 클래스 속성: 클래스가 공유하는 값, 메서드 밖에서 정의.
- 속성은 수정/삭제 가능하며 객체에 동적으로 추가할 수도 있다.
"""
