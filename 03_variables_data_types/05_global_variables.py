# Global Variables
# 1. 전역 변수란?
# 함수 외부에서 생성된 변수이며, 전역 변수는 함수 내부와 외부 모두에서 누구나 사용할 수 있습니다.
# 전역 변수는 프로그램 전체에서 접근할 수 있는 변수를 의미합니다.

x = "awesome"
def myfunc():
  print("Python is " + x)
  
myfunc()

# 함수 내에서 같은 이름의 변수를 생성하면 해당 변수는 지역 변수가 되어 함수 내에서만 사용할 수 있습니다. 
# 같은 이름의 전역 변수는 원래 값을 그대로 유지하며 전역 변수로 사용됩니다.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
  
myfunc()

print("Python is " + x)