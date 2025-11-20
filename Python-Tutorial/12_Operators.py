"""
📌 파이썬 연산자 (Python Operators)
===================================

연산자는 변수와 값에 대해 연산을 수행하는 데 사용됩니다.

예:
    print(10 + 5)

Python 연산자 종류:
--------------------
1) 산술 연산자 (Arithmetic Operators)
2) 할당 연산자 (Assignment Operators)
3) 비교 연산자 (Comparison Operators)
4) 논리 연산자 (Logical Operators)
5) 항등 연산자 (Identity Operators)
6) 멤버십 연산자 (Membership Operators)
7) 비트 연산자 (Bitwise Operators)


=====================================
📌 1. 산술 연산자 (Arithmetic Operators)
=====================================

    +   Addition(덧셈)            x + y
    -   Subtraction(뺄셈)         x - y
    *   Multiplication(곱셈)      x * y
    /   Division(나눗셈, float)   x / y
    %   Modulus(나머지)           x % y
    **  Exponentiation(거듭제곱)   x ** y
    //  Floor Division(내림 나눗셈) x // y

예:
    x = 15
    y = 4
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)
    print(x ** y)
    print(x // y)

📌 나눗셈 종류
-------------------
    /  → 항상 float 반환
    // → 정수로 내림 처리

예:
    print(12 / 5)   # 2.4
    print(12 // 5)  # 2


=====================================
📌 2. 할당 연산자 (Assignment Operators)
=====================================

    =     x = 5
    +=    x += 3    (x = x + 3)
    -=    x -= 3
    *=    x *= 3
    /=    x /= 3
    %=    x %= 3
    //=   x //= 3
    **=   x **= 3
    &=    x &= 3
    |=    x |= 3
    ^=    x ^= 3
    >>=   x >>= 3
    <<=   x <<= 3

📌 바다코끼리 연산자 (:=)
Python 3.8에서 도입. 표현식 안에서 변수에 값을 할당 가능.

예:
    if (count := len(numbers)) > 3:
        print(count)


=====================================
📌 3. 비교 연산자 (Comparison Operators)
=====================================

    ==   Equal
    !=   Not equal
    >    Greater than
    <    Less than
    >=   Greater or equal
    <=   Less or equal

예:
    x = 5
    y = 3
    print(x == y)
    print(x != y)
    print(x > y)


📌 비교 연산자 체이닝
-----------------------
    print(1 < x < 10)
    print(1 < x and x < 10)


=====================================
📌 4. 논리 연산자 (Logical Operators)
=====================================

    and   두 조건이 모두 True
    or    두 조건 중 하나 이상 True
    not   결과를 반대로

예:
    x = 5
    print(x > 0 and x < 10)
    print(x < 5 or x > 10)
    print(not(x > 3 and x < 10))


=====================================
📌 5. 항등 연산자 (Identity Operators)
=====================================

    is      두 변수가 같은 객체(메모리 동일)인가?
    is not  두 변수가 다른 객체인가?

예:
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x

    print(x is z)   # True
    print(x is y)   # False
    print(x == y)   # True


📌 is vs ==
------------
    is   → 객체(메모리) 비교
    ==   → 값 비교


=====================================
📌 6. 멤버십 연산자 (Membership Operators)
=====================================

    in        값이 시퀀스 내부에 존재?
    not in    값이 시퀀스 내부에 없음?

예:
    fruits = ["apple", "banana", "cherry"]
    print("banana" in fruits)
    print("pineapple" not in fruits)

문자열에서도 가능:
    text = "Hello World"
    print("H" in text)
    print("hello" in text)
    print("z" not in text)


=====================================
📌 7. 비트 연산자 (Bitwise Operators)
=====================================

    &   AND
    |   OR
    ^   XOR
    ~   NOT (비트 반전)
    <<  왼쪽 시프트
    >>  오른쪽 시프트

예:
    print(6 & 3)  # 2
    print(6 | 3)  # 7
    print(6 ^ 3)  # 5


=====================================
📌 연산자 우선순위 (Operator Precedence)
=====================================

우선순위(높은 → 낮은):

    ()                      괄호
    **                      거듭제곱
    +x  -x  ~x              단항 연산자
    *  /  //  %             곱셈/나눗셈/나머지
    +  -                    덧셈/뺄셈
    <<  >>                  비트 시프트
    &                       비트 AND
    ^                       비트 XOR
    |                       비트 OR
    비교, is, in, not in     비교/항등/멤버십
    not                     논리 NOT
    and                     논리 AND
    or                      논리 OR

📌 같은 우선순위 연산자들은 왼쪽에서 오른쪽으로 평가됩니다.

예:
    print(5 + 4 - 7 + 3)

"""
