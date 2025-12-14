####################################################################################
# 파이썬 클래스 메서드
####################################################################################

#######################################
# 클래스 메서드
#######################################
# 메서드는 클래스에 속하는 함수입니다. 메서드는 해당 클래스로부터 생성된 객체의 동작을 정의합니다.

# 예
# 클래스에 메서드를 생성하세요:
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()
# Hello, my name is Emil

# 참고:self 모든 메서드는 첫 번째 매개변수로 를 가져야 합니다.

#######################################
# 매개변수가 있는 메서드
#######################################
# 메서드는 일반 함수처럼 매개변수를 받을 수 있습니다.

# 예
# 매개변수를 갖는 메서드를 생성하세요:
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
# 8
# 28

#######################################
# 속성에 접근하는 방법
#######################################
# 메서드는 다음을 사용하여 객체 속성에 접근하고 수정할 수 있습니다 self.

# 예
# 객체의 속성에 접근하는 메서드:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())
# Tobias is 28 years old

#######################################
# 속성을 수정하는 메서드
#######################################
# 메서드는 객체의 속성을 수정할 수 있습니다.

# 예
# 속성 값을 변경하는 메서드:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
# Happy birthday! You are now 26
# Happy birthday! You are now 27

#######################################
# __str__() 메서드
#######################################
# 이 __str__()메서드는 객체를 출력할 때 반환되는 값을 제어하는 특별한 메서드입니다.

# 예
# 해당 __str__()방법 없이:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)
# <__main__.Person object at 0x1027eb650>
# --> 클래스 이름, 메모리 주소 --> 자동 기본값으로 출력

# 예
# 다음과 같은 __str__()방법으로:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)
# Tobias (36)

#######################################
# 다양한 방법
#######################################
# 클래스는 서로 연동되는 여러 메서드를 가질 수 있습니다.

# 예
# 클래스에 여러 메서드를 생성하세요:
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
# Added: Bohemian Rhapsody
# Added: Stairway to Heaven
# Playlist 'Favorites':
# - Bohemian Rhapsody
# - Stairway to Heaven

#######################################
# 삭제 방법
#######################################
# `delete` 키워드를 사용하면 클래스에서 메서드를 삭제할 수 있습니다 del.

# 예
# 클래스에서 메서드를 삭제합니다:
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error
# Traceback (most recent call last):
#   File "06_Class_Methods.py", line 171, in <module>
#     p1.greet() # This will cause an error
#     ^^^^^^^^
# AttributeError: 'Person' object has no attribute 'greet'

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Insert the missing parts to make the code return: John(36):
#  ? Person:
#    ? ?(self, name, age):
#     self.name = name
#     self.age = age
#   def ? (self):
#     return f'{?.?}({self.?})
# p1 = Person('John', 36)
# print(p1)

# Correct Answer!
# __init__  3
# __str__   4
# name      6
# self      5
# age       7
# def       2
# class     1
# post