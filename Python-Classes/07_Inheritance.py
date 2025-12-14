"""
==========================================================
📌 파이썬 상속(Inheritance)
==========================================================

상속을 사용하면 한 클래스(부모 클래스, 기본 클래스)의 모든
속성과 메서드를 다른 클래스(자식 클래스, 파생 클래스)가 물려받을 수 있다.

✔ 부모 클래스 (Parent / Base Class)
✔ 자식 클래스 (Child / Derived Class)
"""

"""
==========================================================
📌 1. 부모 클래스 정의하기
==========================================================

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# 부모 클래스 사용
x = Person("John", "Doe")
x.printname()

✔ 일반 클래스와 동일하게 작성하면 부모 클래스로 사용할 수 있다.
"""
# 파이썬 부모 클래스 정의

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# 부모 클래스 사용
x = Person("John", "Doe")
x.printname()  # John Doe

"""
==========================================================
📌 2. 자식 클래스 생성하기 (부모 클래스 상속)
==========================================================

class Student(Person):
    pass

✔ Student 클래스는 Person의 모든 속성과 메서드를 그대로 상속받는다.


예:

x = Student("Mike", "Olsen")
x.printname()

✔ printname()은 Person에서 상속받은 메서드
"""
# 파이썬 자식 클래스 생성 (상속)

class Student(Person):
    pass

# 자식 클래스 사용
x = Student("Mike", "Olsen")
x.printname()  # Mike Olsen

"""
==========================================================
📌 3. 자식 클래스에 __init__() 추가하기
==========================================================

자식 클래스에 __init__()을 추가하면 부모 클래스의 __init__()을 덮어쓴다.

class Student(Person):
    def __init__(self, fname, lname):
        # 새로운 속성 추가 가능
        pass

✔ 이 상태에서는 부모의 __init__()이 실행되지 않음
"""
# 파이썬 자식 클래스에 __init__() 추가

class Student(Person):
    def __init__(self, fname, lname):
        # 부모의 __init__()이 호출되지 않음
        pass

# 자식 클래스 사용
x = Student("Mike", "Olsen")
# x.printname()  # → 에러 발생 : AttributeError: 'Student' object has no attribute 'firstname'

"""
==========================================================
📌 4. 부모 클래스의 __init__()을 유지하려면?
----------------------------------------------------------
방법 1) 부모 이름을 직접 호출

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

✔ 명시적으로 부모의 __init__() 호출


방법 2) super() 사용 (가장 권장)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

✔ super()는 부모 클래스 이름을 직접 쓰지 않아도 됨
✔ 다중 상속에서도 안전하게 동작
"""
# 파이썬 부모 클래스의 __init__() 호출 방법

# 방법 1) 부모 이름 직접 호출
class Student1(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# 방법 2) super() 사용
class Student2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# 자식 클래스 사용
x1 = Student1("Anna", "Smith")
x1.printname()  # Anna Smith
x2 = Student2("David", "Brown")
x2.printname()  # David Brown

"""
==========================================================
📌 5. 자식 클래스에 속성 추가하기
==========================================================

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

✔ 부모의 속성 + 자식만의 속성 모두 사용 가능


예: 매개변수 받도록 확장

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
"""
# 파이썬 자식 클래스에 속성 추가

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

# 자식 클래스 사용
x = Student("Mike", "Olsen", 2019)
print(x.firstname)        # Mike
print(x.lastname)         # Olsen
print(x.graduationyear)   # 2019

"""
==========================================================
📌 6. 자식 클래스에 메서드 추가하기
==========================================================

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear
        )

✔ 자식 클래스만의 동작 구현 가능
"""
# 파이썬 자식 클래스에 메서드 추가

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear
        )

x = Student("Mike", "Olsen", 2019)
x.welcome() # Welcome Mike Olsen to the class of 2019
"""
==========================================================
📌 7. 부모 메서드를 자식 클래스에서 재정의(Override)
==========================================================

자식 클래스에서 부모와 동일한 이름의 메서드를 만들면 부모의 메서드를 덮어쓴다.

예)

class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hi, I'm a student")

✔ Student().greet() → "Hi, I'm a student"
"""
# 파이썬 메서드 재정의(Override)

class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hi, I'm a student")

x = Student()
x.greet()  # Hi, I'm a student

"""
==========================================================
📌 정리
----------------------------------------------------------
- 상속은 기존 클래스를 재사용하고 확장하기 위한 기능이다.
- 자식 클래스는 부모의 속성과 메서드를 그대로 물려받는다.
- __init__()을 자식 클래스에서 정의하면 부모의 것을 재정의하므로 super()로 호출 가능.
- 자식 클래스에 속성이나 메서드를 자유롭게 추가할 수 있다.
- 메서드 재정의(Override)를 통해 기능을 변경할 수 있다.
"""
