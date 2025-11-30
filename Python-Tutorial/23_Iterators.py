"""
============================================================
📌 Python 반복자(Iterator)
============================================================

반복자(iterator)란?
- 셀 수 있는 여러 값을 포함한 객체
- 순차적으로 값을 하나씩 꺼낼 수 있는 객체
- 반복자 프로토콜을 구현해야 함

반복자 프로토콜:
1) __iter__()  → 반복자를 반환
2) __next__() → 다음 값을 반환
"""

"""
============================================================
📌 1. 반복자 vs 반복 가능한 객체(Iterable)
============================================================

반복 가능한 객체(iterable):
- 리스트(list)
- 튜플(tuple)
- 딕셔너리(dict)
- 세트(set)
- 문자열(str)
→ iter() 를 사용해 반복자로 변환 가능

예:
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)

    print(next(myit))  # apple
    print(next(myit))  # banana
    print(next(myit))  # cherry

문자열도 iterable:
    mystr = "banana"
    myit = iter(mystr)
    print(next(myit))
"""
# 파이썬 반복자 예제

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry

mystr = "banana"
myit = iter(mystr)
print(next(myit))  # b
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a

"""
============================================================
📌 2. for 루프는 내부적으로 반복자를 사용한다
============================================================
for x in mytuple:
    print(x)

위 코드는 내부적으로 아래와 같음:
    it = iter(mytuple)
    while True:
        print(next(it))
"""
# 파이썬 for 루프와 반복자

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)
# 결과 : apple banana cherry

"""
============================================================
📌 3. 사용자 정의 반복자 만들기
============================================================
클래스에 __iter__() 와 __next__() 를 구현하면 직접 반복자를 만들 수 있음.

예: 1, 2, 3, 4, ... 무한 반복자

    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            return x

    myclass = MyNumbers()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
"""
# 파이썬 사용자 정의 반복자 예제

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3
print(next(myiter))  # 4
print(next(myiter))  # 5

"""
============================================================
📌 4. StopIteration 으로 반복 종료시키기
============================================================
무한 반복을 막기 위해 __next__() 에서 StopIteration 예외를 발생시킬 수 있음.

예: 1~20까지만 반복하는 반복자

    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration

    for x in MyNumbers():
        print(x)

→ 1부터 20까지 출력 후 자동 종료
"""
# 파이썬 StopIteration 예제

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
for x in MyNumbers():
    print(x)
# 결과 : 1 2 3 ... 20

"""
============================================================
📌 핵심 요약
============================================================
- Iterable: 반복 가능한 객체(iter(), next()는 없음)
- Iterator: 반복자(iter(), next() 둘 다 구현됨)
- iter(obj) → obj에서 반복자 생성
- next(iterator) → 다음 요소 반환
- for 문은 내부적으로 반복자를 사용하여 순회함
- 반복자 클래스를 만들려면 __iter__(), __next__() 구현
- 반복 종료는 StopIteration 예외로 처리


============================================================
"""
