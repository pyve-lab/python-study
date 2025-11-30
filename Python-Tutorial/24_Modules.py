"""
============================================================
📌 Python 모듈(Module)
============================================================
모듈이란?
- 함수, 변수, 클래스 등을 모아놓은 “코드 라이브러리”
- .py 파일 하나가 하나의 모듈이 됨
- 다른 파일에서 import 하여 사용할 수 있음
"""

"""
============================================================
📌 1. 모듈 만들기
============================================================
원하는 코드를 .py 파일로 저장하면 그것이 모듈이 됨.

예: mymodule.py
    def greeting(name):
        print("Hello, " + name)
"""
# 파이썬 모듈 만들기 예제

def greeting(name):
    print("Hello, " + name)
# mymodule.py 파일로 저장

"""
============================================================
📌 2. 모듈 사용하기 (import)
============================================================
기본 import 방식:
    import mymodule
    mymodule.greeting("Jonathan")

사용법:  module_name.function_name
"""
# 파이썬 모듈 사용 예제

import mymodule
mymodule.greeting("Jonathan")
# 결과 : Hello, Jonathan

"""
============================================================
📌 3. 모듈에 변수 포함하기
============================================================
모듈은 함수뿐 아니라 여러 데이터도 포함할 수 있음.

mymodule.py:
    person1 = {
        "name": "John",
        "age": 36,
        "country": "Norway"
    }

사용:
    import mymodule
    print(mymodule.person1["age"])
"""
# 파이썬 모듈에 변수 포함 예제

import mymodule
print(mymodule.person1["age"])
# 결과 : 36

"""
============================================================
📌 4. 모듈 이름 바꾸기 (alias)
============================================================
import mymodule as mx
print(mx.person1["age"])
"""
# 파이썬 모듈 별칭(alias) 사용 예제

import mymodule as mx
print(mx.person1["age"])
# 결과 : 36

"""
============================================================
📌 5. 파이썬 내장 모듈 사용하기
============================================================
예: platform 모듈
    import platform
    print(platform.system())
"""
# 파이썬 내장 모듈 사용 예제

import platform
print(platform.system())
# 결과 : Windows

"""
============================================================
📌 6. dir() 함수 — 모듈 내부 구성 확인
============================================================
모듈의 모든 함수/변수 이름을 리스트로 반환함.

예:
    import platform
    print(dir(platform))

→ 사용자 정의 모듈에도 사용 가능
"""
# 파이썬 dir() 함수로 모듈 구성 확인 예제

import platform
print(dir(platform))
# 결과 : platform 모듈의 모든 속성 리스트 출력
# ['AndroidVer', 'IOSVersionInfo', '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
# '__spec__', '__version__', '_comparable_version', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_java_getprop', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', '_os_release_candidates',
#  '_parse_os_release', '_platform', '_platform_cache', '_sys_version', '_sys_version_cache', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_stages', '_win32_ver', '_wmi', '_wmi_query', 'android_ver',
#  'architecture', 'collections', 'freedesktop_os_release', 'functools', 'ios_ver', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler',
#  'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']

"""
============================================================
📌 7. 모듈에서 일부만 가져오기 (from)
============================================================
mymodule.py 내용:
    def greeting(name): ...
    person1 = {...}

특정 항목만 가져오기:
    from mymodule import person1
    print(person1["age"])

📌 특징:
- module_name 없이 바로 사용 가능
- 단, 이름 충돌에 주의!
"""
# 파이썬 모듈에서 일부만 가져오기 예제

from mymodule import person1
print(person1["age"])
# 결과 : 36

"""
============================================================
📌 핵심 요약
============================================================
- .py 파일 한 개가 모듈
- import module  
- import module as alias  
- from module import name  
- dir(module) → 모듈의 모든 기능 확인
- 모듈 안에는 함수, 변수, 클래스 등 어떤 코드든 포함 가능

============================================================
"""
