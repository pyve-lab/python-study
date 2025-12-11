
# =================================================================
# [1] 파이썬 내부 클래스 개념
# =================================================================

# 내부 클래스는 다른 클래스 안에 정의된 클래스를 말하며, 내부 클래스는 외부 클래스의 속성과 메서드에 접근할 수 있습니다.
# 내부 클래스는 특정 한 곳에서만 사용되는 클래스를 묶어서 코드를 더 체계적으로 만드는 데 유용합니다.

# =================================================================
# [2] 내부 클래스 생성 예제
# =================================================================

# 예:
# 내부클래스를 생성하세요.
class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)

# =================================================================
# [3] 외부에서 내부 클래스 접근하기
# =================================================================

# 내부 클래스에 접근하려면 먼저 외부 클래스의 객체를 생성한 후, 그 객체를 통해 내부 클래스의 객체를 생성해야 합니다.

# 예:
# 내부 클래스에 접근하여 객체 생성하기
class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

# =================================================================
# [4] 내부 클래스에서 외부 클래스 접근하기
# =================================================================

# 파이썬 내부 클래스는 자동으로 외부 클래스 인스턴스에 접근하지 못합니다.
# 내부 클래스가 외부 클래스에 접근하려면, 외부 클래스 인스턴스를 매개변수로 전달해야 합니다.

# 예:
# 외부 클래스 인스턴트를 내부 클래스에 전달하기

class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

# =================================================================
# [5] 실용적인 예제: 자동차 엔진을 표현하는 내부 클래스
# =================================================================

# 내부 클래스는 외부 클래스의 문맥 내에서만 사용되는 헬퍼 클래스를 생성할 때 유용합니다.
# 예 : 
# 자동차 엔진을 나타내기 위해 내부클래스를 사용하세요

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()

# =================================================================
# [6] 다중 내부 클래스
# =================================================================

# 하나의 클래스 내에 여러 내부 클래스를 정의할 수 있습니다.
# 예 :
# 여러 개의 내부 클래스를 생성합니다.
class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()
