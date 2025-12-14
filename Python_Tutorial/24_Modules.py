####################################################################################
# 파이썬 모듈
####################################################################################

#######################################
# 모듈이란 무엇인가요?
#######################################
# 모듈은 코드 라이브러리와 동일하다고 생각하세요.
# 애플리케이션에 포함하려는 함수 집합이 들어 있는 파일입니다.

#######################################
# 모듈 만들기
#######################################
# 모듈을 만들려면 원하는 코드를 파일 확장자로 저장하기만 하면 됩니다 .py.

# 예
# 이 코드를 다음 이름의 파일에 저장하세요.mymodule.py
def greeting(name):
  print("Hello, " + name)


#######################################
# 모듈 사용
#######################################
# 이제 다음 명령문을 사용하여 방금 만든 모듈을 사용할 수 있습니다 import.

# 예
# mymodule이라는 모듈을 가져오고 greeting 함수를 호출합니다.
import mymodule

mymodule.greeting("Jonathan")
# Hello, Jonathan

# 참고: 모듈의 함수를 사용할 때는 다음 구문을 사용하세요: module_name.function_name .

#######################################
# 모듈의 변수
#######################################
# 모듈은 이미 설명한 대로 함수를 포함할 수 있지만 모든 유형의 변수(배열, 사전, 객체 등)도 포함할 수 있습니다.

# 예
# 이 코드를 파일에 저장하세요 mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# 예
# mymodule이라는 모듈을 가져와서 person1 사전에 접근합니다.
import mymodule

a = mymodule.person1["age"]
print(a)
# 36

#######################################
# 모듈 이름 지정
#######################################
# 모듈 파일의 이름은 원하는 대로 지정할 수 있지만 파일 확장자는 다음과 같아야 합니다. .py

#######################################
# 모듈 이름 바꾸기
#######################################
# 모듈을 가져올 때 다음 as키워드를 사용하여 별칭을 만들 수 있습니다.

# 예
# mymodule호출된 항목 에 대한 별칭을 만듭니다 mx.
import mymodule as mx

a = mx.person1["age"]
print(a)
# 36

#######################################
# 내장 모듈
#######################################
# Python에는 여러 개의 내장 모듈이 있어서 언제든지 가져올 수 있습니다.

# 예
# 모듈을 가져와서 사용하세요 platform:
import platform

x = platform.system()
print(x)
# Darwin

#######################################
# dir() 함수 사용하기
#######################################
# 모듈에 있는 모든 함수 이름(또는 변수 이름)을 나열하는 내장 함수가 있습니다. dir()함수의 내용은 다음과 같습니다.

# 예
# 플랫폼 모듈에 속하는 정의된 이름을 모두 나열하세요.
import platform

x = dir(platform)
print(x)
# # ['AndroidVer', 'IOSVersionInfo', '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_java_getprop', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', '_os_release_candidates', '_parse_os_release', '_platform', '_platform_cache', '_sys_version', '_sys_version_cache', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_stages', '_win32_ver', '_wmi', '_wmi_query', 'android_ver', 'architecture', 'collections', 'freedesktop_os_release', 'functools', 'ios_ver', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']

# 참고: 이 기능은 모든dir() 모듈 에서 사용할 수 있으며 , 사용자가 직접 만든 모듈에서도 사용할 수 있습니다.

#######################################
# 모듈에서 가져오기
#######################################
# 키워드를 사용하여 모듈에서 일부만 가져오도록 선택할 수 있습니다 from.

# 예
# 명명된 모듈에는 mymodule하나의 함수와 하나의 사전이 있습니다.
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# 예
# 모듈에서 person1 사전만 가져옵니다.
from mymodule import person1

print (person1["age"])
# 36

# 참고: 키워드를 사용하여 가져올 때 from 모듈의 요소를 참조할 때 모듈 이름을 사용하지 마세요. 예: person1["age"], not mymodule.person1["age"]

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# True or False. A module can only contain one function or object.

# True
# False      # Correct Answer!