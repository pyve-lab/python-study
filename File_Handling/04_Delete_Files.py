####################################################################################
# 파이썬 파일 삭제
####################################################################################

#######################################
# 파일 삭제
#######################################
# 파일을 삭제하려면 OS 모듈을 가져와서 해당 os.remove()함수를 실행해야 합니다.

# 예
# "demofile.txt" 파일을 삭제하세요.

# import os
# os.remove("demofile.txt")

#######################################
# 파일이 존재하는지 확인하세요:
#######################################
# 오류가 발생하는 것을 방지하려면 파일을 삭제하기 전에 파일이 존재하는지 확인하는 것이 좋습니다.

# 예
# 파일이 존재하는지 확인한 후 , 존재 한다면 삭제하십시오.

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# The file does not exist

#######################################
# 폴더 삭제
#######################################
# 폴더 전체를 삭제하려면 다음 os.rmdir()방법을 사용하세요.

# 예
# "myfolder" 폴더를 삭제하세요:
# import os
# os.rmdir("myfolder")
# 나한테 그런 거 없삼 오류만남
# 참고: 비어 있는 폴더 만 삭제할 수 있습니다 .


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# To remove a file you can import the os module, but which function removes the file?

# os.delete()
# os.drop()
# os.remove()           # Correct Answer!