# Print_Text
# 1. 파이썬 텍스트 출력
# print()함수를 사용하여 텍스트를 표시하거나 값을 출력할 수 있습니다.
print("Hello, World!")


# 2. 여러줄 출력
# print() 함수는 원하는 만큼 사용할 수 있습니다. 각 호출은 기본적으로 새 줄에 텍스트를 출력합니다.
print("파이썬 출력 예제입니다.")
print("Python Study - Basic Syntax and Output")
print("화이팅!")


# 3. 따옴표 사용
# Python에서 텍스트는 따옴표로 묶어야 합니다. "(큰따옴표나) '(작은따옴표)를 사용할 수 있습니다.
print('작은따옴표로 묶인 텍스트입니다.')
print("큰따옴표로 묶인 텍스트입니다.")
# 혼합하여 사용할 수도 있습니다.
print("작은따옴표(')를 포함한 텍스트입니다.")
print('큰따옴표(")를 포함한 텍스트입니다.')
# 여러 줄의 텍스트를 출력하려면 세 개의 따옴표를 사용할 수 있습니다.
print("""이 텍스트는
여러 줄에 걸쳐 출력됩니다.
파이썬은 매우 유용한 언어입니다.""")
# print() 함수는 여러 개의 인수를 받아서 한 줄에 출력할 수도 있습니다.
print("파이썬", "출력", "함수", "예제")

# 텍스트를 따옴표로 묶는 것을 잊어버리면 Python에서 오류가 발생합니다.
# 오류발생 예 : print(Hello, World!)
# 올바른 예 : print("Hello, World!")


# 4. 줄바꿈 없이 출력하기
# print() 함수는 기본적으로 출력 후에 줄바꿈을 추가합니다.
# 줄바꿈 없이 출력하려면 end 매개변수를 사용할 수 있습니다.
print("Hello World!", end="")
print("I will print on the same line.")


# Print_Number
# 1. 파이썬 숫자 출력
# print() 함수를 사용하여 숫자를 출력할 수 있습니다.
print(42)
print(3.14)
print(-7)
print(0)


# 2. 함수 내부에서 수학 연산을 수행
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(8 / 4)


# 3. 텍스트와 숫자 혼합하여 출력하기
print("The answer is", 42)
print("I am", 35, "years old.")
print("크리스마스는",12,"월",25,"일입니다.")


