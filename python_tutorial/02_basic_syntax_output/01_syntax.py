# Syntax
# 1. 파이썬 구문 실행
print("Hello, Python!")
print("This is my first Python program.")
print("파이썬 공부를 시작해보자")
print('화이팅')


# 2. 파이썬 들여쓰기
# 들여쓰기는 파이썬에서 매우 중요합니다. 들여쓰기는 코드 블록을 정의하는 데 사용됩니다.
# 들여쓰기가 올바르지 않으면 오류가 발생합니다.
if 5 > 2 :
    print("5는 2보다 큽니다.")

if 10 < 20 :
    print("10은 20보다 작습니다.")
    
if 15 == 15 :
    print("15는 15와 같습니다.")
    
# 아래 코드는 들여쓰기가 되어 있지 않아 오류가 발생합니다.
# 오류발생 예
# if 8 != 5 :
# print("8은 5와 같지 않습니다.")
# 공백의 개수는 스페이스바 4칸 또는 탭키 1칸을 사용하는 것이 일반적입니다.


# 3. 파이썬 변수
x = 5
y = "Hello, World!"
p_name = "파이썬"

print(x)
print(y)
print(p_name)


# 4. 파이썬 주석처리
# 파이썬에서 주석은 # 기호로 시작합니다. 주석은 코드에 대한 설명이나 메모를 작성할 때 사용되며, 파이썬 인터프리터는 주석을 무시합니다.
#This is a comment
print("Hello, World!")
# 주석은 줄의 끝에도 넣을 수 있으며, Python은 줄의 나머지 부분을 무시합니다.
print("파이썬 주석처리 줄 끝에 넣어보기")  # This comment is ignored by Python


#Statements
# 5. 파이썬 
# 파이썬은 문장끝에 세미콜론(;)을 입력하는것이 필수가 아니며 선택사항 입니다.
print("python Statements")
print("파이썬은 문장 끝에 세미콜론을 필수로 입력하지 않아도 됩니다.")
print("하지만 원한다면 세미콜론을 사용할 수 있습니다.")
# 세미콜론으로 여러 문장을 구분하여 한 줄에 작성할 수 있지만 ;, 읽기 어려워서 거의 사용하지 않습니다.
print("Hello"); print("World");print("!")
# 그러나 구분 기호(줄 바꿈 또는 .) 없이 같은 줄에 두 개의 문장을 넣으면 ;Python에서 오류가 발생합니다.
# 오류발생 예 : print("Hello") print("World") 



