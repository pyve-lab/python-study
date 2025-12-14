####################################################################################
# 파이썬 파일 열기
####################################################################################

#######################################
# 서버에서 파일을 엽니다
#######################################
# 파이썬 파일이 있는 폴더에 다음과 같은 파일이 있다고 가정해 보겠습니다.

# 데모파일.txt
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# 파일을 열려면 내장 open()함수를 사용하십시오.
# 이 open()함수는 파일 객체를 반환하며, 이 객체에는 read()파일 내용을 읽는 메서드가 있습니다.

# 예
f = open("demofile.txt")
print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# 파일이 다른 위치에 있는 경우 다음과 같이 파일 경로를 지정해야 합니다.
# 예
# 다른 위치에 있는 파일을 엽니다.
# f = open("D:\\myfiles\welcome.txt")
# print(f.read())
# ㄴ 이건 없으니까 오류남

# with다음 문장을 사용하여
# with파일을 열 때 다음 구문을 사용할 수도 있습니다 .

# 예
# 키워드 사용 with:
with open("demofile.txt") as f:
  print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# 그러면 파일을 닫는 것에 대해 걱정할 필요가 없습니다. 해당 with명령문이 알아서 처리해 줍니다.

#######################################
# 파일 닫기
#######################################
# 파일 작업을 마친 후에는 항상 파일을 닫는 것이 좋습니다.
# 해당 구문을 사용하지 않는 경우 with, 파일을 닫기 위해 close 문을 작성해야 합니다.

# 예
# 파일 사용이 끝나면 닫으세요.
f = open("demofile.txt")
print(f.readline())
f.close()
# Hello! Welcome to demofile.txt

# 참고: 파일을 열 때는 항상 닫아야 합니다. 버퍼링 문제로 인해 파일을 닫기 전까지는 변경 사항이 반영되지 않을 수 있습니다.

#######################################
# 파일의 읽기 전용 부분
#######################################
# 기본적으로 이 read()메서드는 전체 텍스트를 반환하지만, 반환할 문자 수를 지정할 수도 있습니다.

# 예
# 파일의 처음 5개 문자를 반환합니다.
with open("demofile.txt") as f:
  print(f.read(5))
# Hello

#######################################
# 줄을 읽으세요
#######################################
# 다음 메서드를 사용하면 한 줄을 반환할 수 있습니다 readline().

# 예
# 파일에서 한 줄을 읽으세요:
with open("demofile.txt") as f:
  print(f.readline())
# Hello! Welcome to demofile.txt

# 두 번 전화를 걸면 readline()처음 두 줄을 읽을 수 있습니다.

# 예
# 파일에서 두 줄을 읽으세요:
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())
# This file is for testing purposes.

# 파일의 각 줄을 순회하면 파일 전체를 한 줄씩 읽을 수 있습니다.

# 예
# 파일을 한 줄씩 순회합니다.
with open("demofile.txt") as f:
  for x in f:
    print(x)
# Hello! Welcome to demofile.txt
#
# This file is for testing purposes.
#
# Good Luck!
# 신기한게 이렇게 한 줄씩 띄어쓰기 된다 ㅇㅅㅇ


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# After opening a file with the open() function, which method can be used to read the content?

# list()
# read()        # Correct Answer!
# show()