"""
==========================================================
📌 클래스 메서드 (Class Methods? → 정확히는 인스턴스 메서드)
==========================================================

메서드(method)는 클래스 내부에 정의된 함수로,
해당 클래스로부터 생성된 객체(인스턴스)의 '동작'을 정의한다.

✔ 모든 인스턴스 메서드는 첫 번째 매개변수로 self를 가져야 한다.
    → self는 메서드가 어떤 객체에 속해 실행되는지를 알려준다.
"""

"""
==========================================================
📌 1. 기본 메서드 정의하기
==========================================================

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

✔ p1.greet() 호출 → self는 자동으로 p1을 참조한다.
"""
# 파이썬 클래스 메서드 정의

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()  # Hello, my name is Emil

"""
==========================================================
📌 2. 매개변수가 있는 메서드
==========================================================

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

✔ 일반 함수처럼 파라미터 개수 제한 없이 사용 가능
"""
# 파이썬 매개변수가 있는 메서드

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
    
calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.multiply(4, 7))   # 28

"""
==========================================================
📌 3. 속성에 접근하는 메서드
==========================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

✔ self.name, self.age 로 속성값 접근 가능
"""
# 파이썬 속성에 접근하는 메서드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())  # Tobias is 28 years old

"""
==========================================================
📌 4. 속성을 수정하는 메서드
==========================================================

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

✔ self.age += 1 → 객체의 속성을 내부에서 변경
"""
# 파이썬 속성을 수정하는 메서드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()  # Happy birthday! You are now 26
p1.celebrate_birthday()  # Happy birthday! You are now 27

"""
==========================================================
📌 5. __str__() 메서드 (객체 출력 제어)
==========================================================

__str__() 메서드를 정의하면 print()로 객체를 출력할 때
반환되는 문자열을 직접 지정할 수 있다.

예1) __str__() 없을 때:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1)   # <__main__.Person object at 0x...>

예2) __str__() 있을 때:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)   # Tobias (36)

✔ 디버깅/로그/출력 용도로 매우 유용
"""
# 파이썬 __str__() 메서드 정의

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = Person("Tobias", 36)
print(p1)   # Tobias (36)

"""
==========================================================
📌 6. 여러 메서드를 가진 클래스 (메서드 간 상호작용)
==========================================================

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

✔ 여러 메서드가 하나의 객체 기능을 구성한다.
"""
# 파이썬 여러 메서드를 가진 클래스

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

"""
==========================================================
📌 7. 메서드 삭제하기 (del 키워드)
==========================================================

메서드를 클래스에서 완전히 삭제할 수 있다.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")

del Person.greet   # greet 메서드 삭제

p1.greet()         # → 에러 발생

✔ 클래스에서 메서드를 제거하면 모든 인스턴스에서 사용 불가
"""
# 파이썬 메서드 삭제하기

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")
del Person.greet   # greet 메서드 삭제
p1.greet()       # → 에러 발생: AttributeError: 'Person' object has no attribute 'greet'

"""
==========================================================
📌 정리
----------------------------------------------------------
- 메서드는 객체 동작을 정의하는 함수이다.
- 모든 인스턴스 메서드는 첫 번째 인자로 self를 가져야 한다.
- 메서드는 속성을 읽고 수정할 수 있다.
- __str__() 메서드는 객체 출력 시 표현을 제어한다.
- 메서드는 del 키워드로 삭제 가능하다.
- 클래스는 여러 메서드를 포함할 수 있으며 상호작용하며 동작한다.
"""
