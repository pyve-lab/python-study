
# =================================================================
# [1] 캡슐화 기본 개념
# =================================================================

# 캡슐화는 클래스 내부의 데이터를 보호하는 개념입니다.
# 이는 데이터(속성)와 메서드를 하나의 클래스 안에 함께 두고, 클래스 외부에서 해당 데이터에 어떻게 접근할 수 있는지를 통제하는 것을 의미합니다.
# 이를 통해 데이터가 실수로 변경되는 것을 방지하고, 클래스가 내부적으로 어떻게 동작하는지에 대한 세부 구현을 숨길 수 있습니다.



# =================================================================
# [2] 비공개(Private) 속성
# =================================================================

# 파이썬에서는 이중 밑줄(__)을 접두사로 사용하여 속성을 비공개로 만들 수 있습니다.

# 예 : 
# __age라는 비공개 클래스 속성을 생성하세요.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)   # 오류 발생

# 참고: 비공개 속성은 클래스 외부에서 직접 접근할 수 없습니다.

# =================================================================
# [3] 비공개 속성값 가져오기
# =================================================================

# 비공개 속성은 getter 메서드를 통해 접근할 수 있습니다.

# 예 : 
# getter 메서드를 사용하여 비공개 속성에 접근합니다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())



# =================================================================
# [4] 비공개 속성 수정: Setter 메서드
# =================================================================

# 비공개 속성을 수정하려면 세터(setter) 메서드를 만들어 사용할 수 있습니다.
# 세터 메서드에서는 값을 설정하기 전에 유효성 검사를 수행할 수도 있습니다.

# 예 : 
# 세터 메서드를 사용해 비공개 속성을 변경하는 방법:

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



# =================================================================
# [5] 캡슐화를 사용하는 이유
# =================================================================

# 캡슐화(encapsulation)는 다음과 같은 이점을 제공합니다:
# - 데이터 보호: 내부 데이터가 실수로 변경되는 것을 방지
# - 유효성 검사: 값을 설정하기 전에 검증 가능
# - 유연성: 내부 구현을 바꿔도 외부 코드에 영향을 주지 않음
# - 제어권: 데이터 접근 및 수정 방식을 개발자가 완전히 통제 가능



# =================================================================
# [6] 캡슐화 예제: 성적 관리 클래스
# =================================================================

# 예 : 
# 캡슐화를 사용하여 데이터 보호 및 유효성 검사 구현

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
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())



# =================================================================
# [7] 보호된(Protected) 속성
# =================================================================

# Python에서는 단일 밑줄(_) 접두사를 사용하여 보호된 속성을 표현하는 관례도 있습니다.

# 예 : 
# 보호된(protected) 속성을 생성하세요:
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)  # 접근 가능하지만 권장되지 않음

# 참고: 단일 밑줄(_)은 단순한 관례일 뿐입니다. 이는 "내부에서 사용하기 위한 속성"이라는 의미이며 강제 규칙은 아닙니다.

# =================================================================
# [8] 비공개(Private) 메서드
# =================================================================

# 이중 밑줄(__) 접두사를 사용하여 메서드를 비공개로 만들 수도 있습니다.
# 비공개 메서드는 클래스 내부에서만 호출할 수 있습니다.

# 예 :
# 비공개(Private) 메서드를 생성하세요.
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
# calc.__validate(5)  # 비공개 메서드 호출 → 오류 발생

# 참고: 이중 밑줄을 사용하는 비공개 속성과 마찬가지로, 비공개 메서드는 클래스 외부에서 직접 호출할 수 없습니다. 
# __validate 메서드는 클래스 내부의 다른 메서드에서만 사용할 수 있습니다.

# =================================================================
# [9] 이름 망글링(Name Mangling)
# =================================================================

# 이름 망글링(Name mangling)은 파이썬이 비공개 속성과 메서드를 구현하는 방식입니다.
# 이중 밑줄(__)을 사용할 때, 파이썬은 자동으로 내부적으로 앞에 _클래스이름을 붙여 이름을 변경합니다.
# 예를 들어, __age는 _Person__age로 변경됩니다.

# 예:
# 파이썬이 이름을 어떻게 변경하는지 확인해보세요.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Emil", 30)
print(p1._Person__age)  # 접근 가능하지만 권장되지 않음

# 참고: 변경된 이름을 사용해 비공개 속성에 접근할 수는 있지만, 권장되지 않습니다.
# 이는 캡슐화의 목적에 어긋나기 때문입니다.