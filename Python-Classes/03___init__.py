"""
==========================================================
📌 __init__() 메서드란?
==========================================================

모든 클래스에는 객체가 생성될 때 자동으로 실행되는
내장 메서드 __init__()이 존재한다.

이 메서드는:
    - 객체 속성 초기화
    - 객체 생성 시 필요한 준비 작업 수행
을 위해 사용된다.
"""
# 파이썬 __init__() 메서드 기본 구조

class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        # 추가 초기화 작업 수행 가능

"""
==========================================================
📌 1. __init__() 기본 사용 예시
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

✔ 객체를 생성하는 순간 __init__()이 자동 호출됨.
"""
# 파이썬 __init__() 사용 예시

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1.name)  # Emil
print(p1.age)   # 36

"""
==========================================================
📌 2. __init__()를 사용하는 이유
==========================================================

__init__()이 없다면, 객체 생성 후 속성을 직접 설정해야 한다.

예:

class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

→ 속성 값을 매번 수동으로 설정해야 하므로 비효율적.
"""
# 파이썬 __init__() 미사용 예시

class Person:
    pass
p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)  # Tobias
print(p1.age)   # 25

"""
==========================================================
📌 3. __init__()가 있을 경우 — 초기값을 바로 설정
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

✔ 객체 생성과 동시에 속성 값을 설정할 수 있어 편리함.
"""
# 파이썬 __init__()가 있을 경우

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)
print(p1.name)  # Linus
print(p1.age)   # 28

"""
==========================================================
📌 4. __init__() 매개변수 기본값 설정
==========================================================

age 매개변수에 기본값을 줄 수도 있다.

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")          # age 기본값 18 사용
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

✔ 기본값 덕분에 일부 인자를 생략할 수 있다.
"""
# 파이썬 __init__() 매개변수 기본값 설정

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")     # age 기본값 18 사용
p2 = Person("Tobias", 25)
print(p1.name, p1.age)  # Emil 18
print(p2.name, p2.age)  # Tobias 25

"""
==========================================================
📌 5. __init__()는 여러 매개변수도 가능
==========================================================

필요한 만큼 매개변수를 늘려 다양한 속성을 한 번에 초기화할 수 있다.

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
"""
# 파이썬 __init__() 여러 매개변수 사용

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name)     # Linus
print(p1.age)      # 30
print(p1.city)     # Oslo
print(p1.country)  # Norway

"""
==========================================================
📌 정리
----------------------------------------------------------
- __init__()는 '생성자'로, 객체가 만들어지는 순간 자동 호출된다.
- 속성 초기화 및 객체 설정을 간단하고 안정적으로 수행할 수 있게 한다.
- 기본값 설정, 여러 매개변수 정의 등 유연하게 구성할 수 있다.
"""
