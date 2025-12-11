
# =================================================================
# [1] 상속 기본 개념
# =================================================================

# 상속(Inheritance)을 통해 우리는 다른 클래스의 모든 메서드와 속성을 물려받는 클래스를 정의할 수 있습니다.

# 부모 클래스 (Parent class): 상속을 해주는 클래스로, 기본 클래스(base class)라고도 합니다.
# 자식 클래스 (Child class): 다른 클래스로부터 상속을 받는 클래스로, 파생 클래스(derived class)라고도 합니다.


# =================================================================
# [2] 부모 클래스 생성
# =================================================================

# 어떤 클래스든 부모 클래스가 될 수 있으며, 구문은 다른 클래스를 생성하는 것과 동일합니다.
#
# 예:
# 클래스 이름은 Person으로 하고, firstname과 lastname 속성(properties)을 가지며, printname 메서드(method)를 생성하세요.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
        
# Person 클래스를 사용하여 객체를 생성한 다음, printname 메서드를 실행하세요.

x = Person("John", "Doe")
x.printname()



# =================================================================
# [3] 자식 클래스 생성 (상속)
# =================================================================

# 다른 클래스의 기능을 상속받는 클래스를 만들려면, 자식 클래스를 정의할 때
# 부모 클래스를 매개변수로 전달합니다.
#
# 예:
# Student 클래스가 Person 클래스를 상속받도록 생성

class Student(Person):
    pass

# 참고: 클래스에 다른 속성이나 메서드를 추가하지 않으려면 pass 키워드를 사용합니다.
# 이제 Student 클래스는 Person 클래스와 동일한 속성과 메서드를 갖게 되었습니다.


# 예 :
# 해당 Student클래스를 사용하여 객체를 생성한 다음 printname메서드를 실행하세요.

x = Student("Mike", "Olsen")
x.printname()



# =================================================================
# [4] 자식 클래스에 __init__() 함수 추가
# =================================================================

# 지금까지는 부모 클래스의 속성과 메서드를 그대로 상속받았습니다.
# 이제 자식 클래스에 __init__() 함수를 직접 추가해 보겠습니다.

# 참고: __init__() 함수는 클래스의 새 객체가 생성될 때 자동으로 호출됩니다.

# 예:
# tudent 클래스에 init() 함수를 추가하세요
class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.
        Person.__init__(self, fname, lname)

# 주의: 자식 클래스에서 __init__() 함수를 정의하면
# 부모 클래스의 __init__() 함수는 자동으로 상속되지 않으며 재정의됩니다.

# 예:
# 부모 클래스의 __init__() 함수 상속을 유지하려면 부모 클래스의 __init__()함수를 호출하는 코드를 추가하세요.
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# 이제 함수를 성공적으로 추가했고 __init__(), 부모 클래스의 상속도 유지했으므로, __init__()함수 내에 기능을 추가할 준비가 되었습니다.

# =================================================================
# [5] 부모 클래스의 __init__() 유지하기
# =================================================================

# 부모 클래스의 __init__() 함수 상속을 유지하려면
# 자식 클래스에서 부모 클래스의 __init__()을 명시적으로 호출해야 합니다.

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)



# =================================================================
# [6] super() 함수 사용
# =================================================================

# super() 함수를 사용하면 부모 클래스 이름을 직접 적지 않아도 되고,
# 부모 클래스의 메서드를 자동으로 상속받을 수 있습니다.

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# super() 함수를 사용하면 부모 클래스의 이름을 직접 지정할 필요가 없으며, 부모로부터 메서드와 속성을 자동으로 상속받습니다.

# =================================================================
# [7] 속성 추가
# =================================================================

# 예:
# Student 클래스에 graduationyear라는 속성을 추가하세요.

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

# 아래 예시에서 연도 2019는 변수로 사용되어야 하며, Student 객체를 생성할 때 해당 클래스에 전달되어야 합니다. 
# 이를 위해 init() 함수에 매개변수를 하나 더 추가하십시오.

# 예:
# year 매개변수를 추가하고, 객체를 생성할 때 올바른 연도를 전달하십시오.

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)



# =================================================================
# [8] 메서드 추가
# =================================================================

# 예:
# Student 클래스에 welcome 메서드를 추가합니다.

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)

# 참고: 자식 클래스에 부모 클래스와 동일한 이름의 메서드를 추가하면, 부모 메서드의 상속은 재정의되어 적용되지 않습니다.
