# Modity Strings
# 파이썬은 문자열(string)에 사용할 수 있는 일련의 내장 메서드(built-in methods)를 제공합니다.

# 1. 대문자로 변환 (Upper Case)
# upper() 메서드는 문자열 전체를 대문자로 변환하여 반환합니다.

# 예시:
'''
a = "Hello, World!"
print(a.upper())
# 출력: HELLO, WORLD!

'''


# 2. 소문자로 변환 (Lower Case)
# lower() 메서드는 문자열 전체를 소문자로 변환하여 반환합니다.

# 예시:
'''
a = "Hello, World!"
print(a.lower())
# 출력: hello, world!
'''


# 3. 공백 제거 (Remove Whitespace)
# 공백(Whitespace)은 실제 텍스트 앞이나 뒤에 있는 빈 공간을 의미하며, 종종 이 공간을 제거해야 할 필요가 있습니다. 
# strip() 메서드는 문자열의 시작과 끝에 있는 모든 공백을 제거합니다.

# 예시:
'''
a = " Hello, World! "
print(a.strip())
# 출력: "Hello, World!"
'''


# 4. 문자열 교체 (Replace String)
# replace() 메서드는 문자열 내의 특정 문자열을 다른 문자열로 교체합니다.

# 예시:
'''
a = "Hello, World!"
print(a.replace("H", "J"))
# 출력: Jello, World!
'''


# 5. 문자열 분할 (Split String)
# split() 메서드는 지정된 구분자(separator)를 기준으로 문자열을 나누어, 나누어진 텍스트 조각들이 리스트(list)의 항목이 되도록 반환합니다.
# 이 메서드는 구분자의 인스턴스를 찾으면 문자열을 하위 문자열로 분할합니다.

# 예시:
'''
a = "Hello, World!"
print(a.split(","))
# 출력: ['Hello', ' World!']
'''