####################################################################################
# 파이썬 내부 클래스
####################################################################################

#######################################
# 파이썬 내부 클래스
#######################################
# 내부 클래스는 다른 클래스 내부에 정의된 클래스입니다. 내부 클래스는 외부 클래스의 속성과 메서드에 접근할 수 있습니다.
# 내부 클래스는 특정 위치에서만 사용되는 클래스들을 그룹화하여 코드를 더욱 체계적으로 정리하는 데 유용합니다.

# 예
# 내부 클래스를 생성합니다.
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
# Outer Class

#######################################
# 외부에서 내부 계층에 접근하기
#######################################
# 내부 클래스에 접근하려면 먼저 외부 클래스의 객체를 생성한 다음, 내부 클래스의 객체를 생성해야 합니다.
# 예
# 내부 클래스에 접근하여 객체를 생성합니다.
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
# Hello from inner class

#######################################
# 실제 사례
#######################################
# 내부 클래스는 외부 클래스의 컨텍스트 내에서만 사용되는 헬퍼 클래스를 만드는 데 유용합니다.
# 예
# 자동차 엔진을 나타내기 위해 내부 클래스를 사용하세요.
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
# Start the engine first!
# Engine started
# Driving the Toyota Corolla

#######################################
# 다수의 내부 클래스
#######################################
# 클래스는 여러 개의 내부 클래스를 가질 수 있습니다.

# 예
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
# Processing data...
# Storing data...

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# How do you make a property private in Python?

# Use a single underscore prefix: _property
# Use a double underscore prefix: __property     # Correct Answer!
# Use the private keyword