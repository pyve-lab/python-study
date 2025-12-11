
# =================================================================
# [1] 클래스 메서드 기본 개념
# =================================================================

# 메서드는 클래스에 속한 함수이며,
# 해당 클래스로부터 생성된 객체의 동작(behavior)을 정의합니다.
# 모든 메서드는 첫 번째 매개변수로 self를 가져야 합니다.



# =================================================================
# [2] 기본 메서드 정의 및 호출
# =================================================================

# 예:
# 클래스에 메서드를 정의하고 호출하는 기본 구조

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

print("\n--- [기본 메서드 정의 및 호출] ---")
p1 = Person("Emil")
p1.greet()



# =================================================================
# [3] 매개변수가 있는 메서드
# =================================================================

# 메서드는 일반 함수처럼 매개변수를 받을 수 있습니다.

# 예:
# 두 수를 더하고 곱하는 메서드를 정의한 클래스

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

print("\n--- [매개변수가 있는 메서드] ---")
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))



# =================================================================
# [4] 객체 속성에 접근하는 메서드
# =================================================================

# 메서드는 self를 통해 객체의 속성에 접근하고 값을 반환할 수 있습니다.

# 예:
# 이름과 나이를 반환하는 메서드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

print("\n--- [객체 속성 접근 메서드] ---")
p1 = Person("Tobias", 28)
print(p1.get_info())



# =================================================================
# [5] 객체 속성을 수정하는 메서드
# =================================================================

# 메서드는 객체의 속성을 수정할 수도 있습니다.

# 예:
# 나이를 증가시키는 메서드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

print("\n--- [객체 속성 수정 메서드] ---")
p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()



# =================================================================
# [6] __str__() 메서드
# =================================================================

# __str__() 메서드는 객체를 print()로 출력할 때
# 어떤 문자열을 보여줄지를 정의하는 특별한 메서드입니다.

# 예:
# __str__() 미구현 시

print("\n--- [__str__() 미구현 예시] ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1)  # 메모리 주소 형태 출력


# 예:
# __str__() 구현 시

print("\n--- [__str__() 구현 예시] ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)



# =================================================================
# [7] 여러 메서드를 가진 클래스
# =================================================================

# 클래스는 서로 연동되는 여러 메서드를 가질 수 있습니다.

# 예:
# 노래 추가/삭제/목록 조회 기능을 가진 Playlist 클래스

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

print("\n--- [여러 메서드를 가진 클래스] ---")
my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()



# =================================================================
# [8] 메서드 삭제 (del 키워드)
# =================================================================

# del 키워드를 사용하면 클래스에서 메서드를 삭제할 수 있습니다.

# 예:
# greet 메서드를 삭제한 후 호출하면 오류 발생

print("\n--- [메서드 삭제] ---")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")

del Person.greet  # 클래스에서 greet 메서드 삭제

# p1.greet()  # 삭제되었기 때문에 실행 시 오류 발생
