####################################################################################
# 파이썬 파일 쓰기
####################################################################################

#######################################
# 기존 파일에 쓰기
#######################################
# 기존 파일에 쓰려면 함수에 매개변수를 추가해야 합니다 open().

# "a" - 추가 - 파일 끝에 내용을 추가합니다.
# "w" - 쓰기 - 기존 내용을 덮어씁니다.

# 예
# "demofile.txt" 파일을 열고 파일에 내용을 추가하세요.

# with open("demofile.txt", "a") as f:
  # f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!Now the file has more content!

#######################################
# 기존 콘텐츠 덮어쓰기
#######################################
# 파일의 기존 내용을 덮어쓰려면 다음 w매개변수를 사용하십시오.

# 예
# "demofile.txt" 파일을 열고 내용을 덮어쓰세요.

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
# Woops! I have deleted the content!

# 참고: "w" 메서드는 파일 전체를 덮어씁니다.

#######################################
# 새 파일 만들기
#######################################
# 파이썬에서 새 파일을 생성하려면 open()다음 매개변수 중 하나를 사용하여 해당 메서드를 사용합니다.

# "x"- 생성 - 파일을 생성하고, 파일이 이미 존재하는 경우 오류를 반환합니다.
# "a"- 추가 - 지정된 파일이 존재하지 않으면 파일을 생성합니다.
# "w"- 쓰기 - 지정된 파일이 존재하지 않으면 파일을 생성합니다.

# 예
# "myfile.txt"라는 이름의 새 파일을 만드세요:
f = open("myfile.txt", "x")
# 생겼다!
# myfile.txt

# 결과: 새로운 빈 파일이 생성됩니다.
# 참고: 파일이 이미 존재하는 경우 오류가 발생합니다.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What happens to the original file content if you open a file like this:
# open('demofile3.txt', 'w')

# The original content will be overwritten       # Correct Answer!
# Any new content will be added after the original content