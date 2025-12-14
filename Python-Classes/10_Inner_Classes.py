"""
==========================================================
📌 파이썬 내부 클래스 (Inner Class)
==========================================================

내부 클래스는 다른 클래스 내부에 정의된 클래스이다.

✔ 외부 클래스에 논리적으로 속하는 기능을 그룹화할 때 유용  
✔ 외부 클래스 내부에서만 사용되는 보조(헬퍼) 클래스를 만들 때 사용  
✔ 외부 클래스의 메서드/속성과 연관된 구조를 만들기 편함  
"""

"""
==========================================================
📌 1. 기본 내부 클래스 생성
==========================================================

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

✔ Inner 클래스는 Outer 클래스 내부에 정의됨  
✔ Outer와 Inner는 서로 다른 클래스지만 구조적으로 결합되어 있음
"""
# 파이썬 기본 내부 클래스 생성

class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)   # Outer Class

"""
==========================================================
📌 2. 외부에서 내부 클래스 객체 생성하기
==========================================================

class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")

outer = Outer()
inner = outer.Inner()   # 내부 클래스 객체 생성
inner.display()

✔ 외부 인스턴스 outer를 통해 내부 클래스 Inner에 접근  
✔ Inner는 Outer 내부의 독립된 클래스
"""
# 파이썬 외부에서 내부 클래스 객체 생성

class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")

outer = Outer()
inner = outer.Inner()   # 내부 클래스 객체 생성
inner.display()        # Hello from inner class

"""
==========================================================
📌 3. 내부 클래스 → 외부 클래스 속성 접근하기
==========================================================

파이썬에서는 내부 클래스가 자동으로 외부 인스턴스에 접근하지 못한다.

따라서 외부 인스턴스를 명시적으로 전달해야 한다.

class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer   # 외부 객체 저장

        def display(self):
            print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

✔ outer 인스턴스를 Inner에 전달하여 외부 속성 name에 접근 가능
"""
# 파이썬 내부 클래스에서 외부 클래스 속성 접근

class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer   # 외부 객체 저장

        def display(self):
            print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()   # Outer class name: Emil

"""
==========================================================
📌 4. 실제 사례 — 엔진을 내부 클래스로 구현
==========================================================

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()   # 내부 클래스 인스턴스 포함

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

✔ Car 내부에서만 의미 있는 Engine 클래스를 내부 클래스로 구성  
✔ car.engine 으로 접근 가능
"""
# 파이썬 내부 클래스를 활용한 실제 사례

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()   # 내부 클래스 인스턴스 포함

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
car.drive()          # Start the engine first!
car.engine.start()   # Engine started
car.drive()         # Driving the Toyota Corolla

"""
==========================================================
📌 5. 여러 개의 내부 클래스 사용하기
==========================================================

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

✔ CPU, RAM 같은 구성 요소를 내부 클래스로 나눠 구조적 표현 가능
"""
# 파이썬 여러 개의 내부 클래스 사용

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
computer.cpu.process()   # Processing data...
computer.ram.store()    # Storing data...

"""
==========================================================
📌 정리
----------------------------------------------------------
- 내부 클래스는 다른 클래스 내부에 정의된 클래스
- 논리적으로 관련된 기능을 묶어 코드 구조를 깔끔하게 유지
- 외부 클래스 인스턴스에 직접 접근하지 않으므로 필요하면 명시적으로 전달해야 함
- 실제 시스템 구성 요소(엔진, CPU 등) 표현에 유용
- 여러 개의 내부 클래스를 가질 수도 있음

"""
