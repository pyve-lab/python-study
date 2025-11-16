####################################################################################
# 파이썬 구문
####################################################################################

#######################################
# Python 구문 실행
#######################################
# 이전 페이지에서 배웠듯이 Python 구문은 명령줄에 직접 작성하여 실행할 수 있습니다.

print("Hello, World!")
# Hello, World!

# 또는 서버에 .py 파일 확장자를 사용하여 Python 파일을 만들고 명령줄에서 실행합니다.

#######################################
# 파이썬 들여쓰기
#######################################
# 들여쓰기는 코드 줄의 시작 부분에 있는 공백을 말합니다.

# 다른 프로그래밍 언어에서는 코드의 들여쓰기가 가독성을 위한 것일 뿐이지만, Python에서는 들여쓰기가 매우 중요합니다.
# 파이썬은 들여쓰기를 사용하여 코드 블록을 나타냅니다.

# 예나만의 Python 서버를 얻으세요
if 5 > 2:
    print("Five is greater than two!")
# Five is greater than two!

# 들여쓰기를 건너뛰면 Python에서 오류가 발생합니다.

# 예
# 구문 오류:
# if 5 > 2:
# print("Five is greater than two!")
# File "03_Python_Syntax.py", line 30
# print("Five is greater than two!")
# ^^^^^
# IndentationError: expected an indented block after 'if' statement on line 29

# 공백의 개수는 프로그래머의 선택에 달려 있습니다. 가장 일반적인 사용은 4개이지만, 최소한 1개는 있어야 합니다.

# 예 (오류)
if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")
# Five is greater than two!
# Five is greater than two!

# 동일한 코드 블록에서 동일한 수의 공백을 사용해야 합니다. 그렇지 않으면 Python에서 오류가 발생합니다.

# 예 (오류)
# 구문 오류:
#  if 5 > 2:
#  print("Five is greater than two!")
#     print("Five is greater than two!")
#   File "03_Python_Syntax.py", line 50
#     if 5 > 2:
#              ^
# IndentationError: unindent does not match any outer indentation level

#######################################
# 파이썬 변수
#######################################
# Python에서는 변수에 값을 할당하면 변수가 생성됩니다.

# 예
# Python의 변수:
x = 5
y = "Hello, World!"

# Python에는 변수를 선언하는 명령이 없습니다.
# 변수에 대해서는 Python 변수 장 에서 자세히 알아볼 수 있습니다.

# HAM : print(x) 5 그냥 나온다는 건가?? 따로 var, string x 이런 게 없다는 거 같은데?
# GPT : Python에서는 변수를 선언할 때 var, int, string 같은 키워드를 사용하지 않습니다.
#       값을 그냥 할당(=) 하면, 그 즉시 변수와 데이터 타입이 함께 생성돼요.
#       Python은 동적 타입 언어라서 변수 타입을 미리 지정하지 않아도 됩니다.
#       변수에 값을 처음 대입할 때 타입이 자동으로 결정되고, 이후 값에 따라 언제든 타입이 바뀔 수도 있습니다.

#######################################
# 댓글
#######################################
# Python은 코드 내에서 문서를 작성하기 위한 주석 기능을 가지고 있습니다.
# 주석은 .으로 시작하고 #, Python은 줄의 나머지 부분을 주석으로 처리합니다.

# 예
# Python의 주석:

# #This is a comment.
print("Hello, World!")
# Hello, World!