####################################################################################
# 파이썬 주석
####################################################################################
# 주석은 Python 코드를 설명하는 데 사용될 수 있습니다.
# 주석을 사용하면 코드를 더 읽기 쉽게 만들 수 있습니다.
# 코드를 테스트할 때 실행을 방지하는 데 주석을 사용할 수 있습니다.

#######################################
# 댓글 만들기
#######################################
# 주석은 .로 시작 #하며 Python은 이를 무시합니다.

# 예
# #This is a comment
print("Hello, World!")
# Hello, World!

# 주석은 줄의 끝에 넣을 수 있으며, Python은 줄의 나머지 부분을 무시합니다.

# 예
print("Hello, World!") #This is a comment
# Hello, World!

# 주석은 코드를 설명하는 텍스트일 필요는 없으며, Python이 코드를 실행하지 못하도록 하는 데에도 사용할 수 있습니다.

# 예
#print("Hello, World!")
print("Cheers, Mate!")
# Cheers, Mate!

#######################################
# 여러 줄 주석
#######################################
# 파이썬에는 실제로 다중줄 주석에 대한 구문이 없습니다.
# #여러 줄로 된 주석을 추가하려면 각 줄에 다음을 삽입하면 됩니다 .

# 예
#This is a comment
#written in
#more than just one line
print("Hello, World!")
# Hello, World!

# 또는 의도한 대로는 아니지만 여러 줄로 된 문자열을 사용할 수도 있습니다.
# Python은 변수에 할당되지 않은 문자열 리터럴을 무시하므로 코드에 여러 줄로 된 문자열(삼중 따옴표)을 추가하고 그 안에 주석을 넣을 수 있습니다.

# 예
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
# Hello, World!

# 문자열이 변수에 할당되지 않는 한 Python은 코드를 읽지만 무시하고 여러 줄로 된 주석을 만듭니다.

# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Exercise
# QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ #
# Which character is used to define a Python comment:
# '
# //
# #         # Correct Answer!
# /*