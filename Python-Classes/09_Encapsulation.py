"""
==========================================================
📌 파이썬 캡슐화 (Encapsulation)
==========================================================

캡슐화는 클래스 내부의 데이터를 보호하는 기법이다.

✔ 속성과 메서드를 클래스 내부에 감춰 외부 접근을 제한  
✔ 데이터를 실수로 변경하는 것을 방지  
✔ 내부 구현을 숨기고 데이터 접근 방식을 제어  
"""

"""
==========================================================
📌 1. 비공개 속성 (Private Attribute)
==========================================================

파이썬에서는 속성 이름 앞에 이중 밑줄 __ 를 붙여 비공개 속성을 만든다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # Private property

p1 = Person("Emil", 25)

print(p1.name)
print(p1.__age)    # 에러 발생 (외부에서 접근 불가)

✔ __age 는 클래스 외부에서 직접 접근 불가  
✔ 데이터 보호를 위한 캡슐화 핵심 기능
"""
# 파이썬 비공개 속성

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # 비공개 속성

p1 = Person("Emil", 25)

print(p1.name)      # Emil
# print(p1.__age)   # 에러 발생 : AttributeError: 'Person' object has no attribute '__age'

"""
==========================================================
📌 2. Getter 메서드로 비공개 속성 읽기
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())

✔ get_age() 를 통해서만 비공개 속성에 접근 가능
"""
# 파이썬 Getter 메서드 비공개 속성 읽기

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
p1 = Person("Tobias", 25)
print(p1.get_age())   # 25

"""
==========================================================
📌 3. Setter 메서드로 비공개 속성 수정하기
==========================================================

setter 메서드로 값 변경을 허용하고, 유효성 검사를 추가할 수 있다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

✔ 잘못된 값 방지 → 데이터 보호 강화  
✔ set_age를 통해서만 속성 변경 제어 가능
"""
# 파이썬 Setter 메서드 비공개 속성 수정하기

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())  # 25

p1.set_age(26)
print(p1.get_age())  # 26

"""
==========================================================
📌 4. 왜 캡슐화를 사용하는가?
==========================================================

- 데이터 보호 (외부에서 실수로 변경할 위험 제거)
- 유효성 검사 가능
- 내부 구조 변경해도 외부 코드에 영향 없음
- 데이터 접근을 제어할 수 있음

예:

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        return "Passed" if self.__grade >= 60 else "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
"""
# 파이썬 캡슐화 실제 사례

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        return "Passed" if self.__grade >= 60 else "Failed"
    
student = Student("Emil")
student.set_grade(85)
print(student.get_grade())   # 85
print(student.get_status())  # Passed

"""
==========================================================
📌 5. 보호된 속성 (Protected Attribute)
==========================================================

밑줄 한 개 _ 는 “외부에서 사용하지 않는 것이 좋다”는 관례를 의미한다.

class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # Protected property

p1 = Person("Linus", 50000)

print(p1.name)
print(p1._salary)    # 접근 가능하지만 권장되지 않음

✔ 단지 관례일 뿐 파이썬은 강제하지 않는다  
✔ 내부 용도로 사용되는 속성을 표시하는 목적
"""
# 파이썬 보호된 속성

class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # 보호된 속성

p1 = Person("Linus", 50000)
print(p1.name)        # Linus
print(p1._salary)     # 50000 (접근 가능하지만 권장되지 않음)

"""
==========================================================
📌 6. 비공개 메서드 (Private Method)
==========================================================

이중 밑줄로 시작하는 메서드는 외부에서 호출할 수 없다.

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)

# calc.__validate(5)  # 에러 발생 (외부 접근 X)

✔ __validate() 는 내부에서만 사용하도록 제한된 메서드
"""
# 파이썬 비공개 메서드

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)    # 15
# calc.__validate(5)  # 에러 발생 : AttributeError: 'Calculator' object has no attribute '__validate'

"""
==========================================================
📌 7. 이름 망글링(Name Mangling)
----------------------------------------------------------
이중 밑줄을 사용하면 파이썬이 속성 이름을 내부적으로 변환한다.

예) __age → _Person__age 로 내부 이름 변경

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Emil", 30)

print(p1._Person__age)   # 가능하지만 사용 비추천!

✔ 내부적으로 바뀐 이름을 사용하면 접근은 가능  
✔ 그러나 캡슐화 취지에 어긋나므로 절대 추천하지 않음
"""
# 파이썬 이름 망글링

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Emil", 30)
print(p1._Person__age)   # 30 (가능하지만 사용 비추천!)

"""
==========================================================
📌 정리
----------------------------------------------------------
- __로 시작하면 비공개 속성/메서드 → 외부 접근 금지
- _로 시작하면 보호된 속성 → 내부 사용 권장
- Getter/Setter로 안전한 접근 방식 제공
- 이름 망글링을 통해 내부 보호 기능 작동
- 캡슐화는 안전하고 견고한 코드를 위한 핵심 원칙

"""
