"""
============================================================
📌 PIP란 무엇인가?
============================================================

● PIP (Package Installer for Python)
   - Python 패키지/모듈을 설치·관리하는 패키지 관리자
   - Python 3.4 이상은 기본 포함
"""

"""
============================================================
📌 패키지란?
============================================================

● Python 코드 라이브러리가 포함된 파일 묶음
● 모듈(module) = 재사용 가능한 Python 코드 파일
● 패키지(package) = 모듈을 포함한 폴더 구조
"""

"""
============================================================
📌 1. PIP 설치 여부 확인
============================================================

명령어:
    pip --version

예:
    C:\...\Scripts> pip --version
"""
# pip 버전 확인 예제
# 명령 프롬프트에서 실행
# pip --version
# pip 25.0.1 from C:\Users\권나현\AppData\Local\Programs\Python\Python313\Lib\site-packages\pip (python 3.13)

"""
============================================================
📌 2. PIP 설치 (필요한 경우)
============================================================

다운로드:
    https://pypi.org/project/pip/
"""

"""
============================================================
📌 3. 패키지 설치
============================================================

명령어:
    pip install 패키지명

예:
    pip install camelcase
"""
# 패키지 설치 예제
# 명령 프롬프트에서 실행
# pip install camelcase
# Collecting camelcase
#   Downloading camelcase-0.2.tar.gz (1.3 kB)
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... done
# Building wheels for collected packages: camelcase
#   Building wheel for camelcase (pyproject.toml) ... done
#   Created wheel for camelcase: filename=camelcase-0.2-py3-none-any.whl size=1804 sha256=4a65580f325f6547db79aebed681433cfca20bf3a511f26ac48e39120fd753f7
#   Stored in directory: c:\users\권나현\appdata\local\pip\cache\wheels\05\ec\2d\8af1da08772881c30648a3fc62453a9437ab3b1bfea15e4df6
# Successfully built camelcase
# Installing collected packages: camelcase
# Successfully installed camelcase-0.2

# [notice] A new release of pip is available: 25.0.1 -> 25.3
# [notice] To update, run: python.exe -m pip install --upgrade pip
"""
============================================================
📌 4. 패키지 사용 방법
============================================================

예:
    import camelcase

    c = camelcase.CamelCase()
    print(c.hump("hello world"))
    # → "Hello World"
"""
# 파이썬 패키지 사용 예제

import camelcase
c = camelcase.CamelCase()
print(c.hump("hello world"))
# 결과 : Hello World

"""
============================================================
📌 5. 패키지 검색
============================================================

● Python 공식 패키지 저장소 (PyPI)
    https://pypi.org/
"""

"""
============================================================
📌 6. 패키지 제거(uninstall)
============================================================

명령어:
    pip uninstall 패키지명

예:
    pip uninstall camelcase

사용자 확인 메시지 후 y 입력 시 삭제됨
"""
# 패키지 제거 예제
# 명령 프롬프트에서 실행
# pip uninstall camelcase
# Found existing installation: camelcase 0.2
# Uninstalling camelcase-0.2:
#   Would remove:
#     c:\users\권나현\appdata\local\programs\python\python313\lib\site-packages\camelcase-0.2.dist-info\*
#     c:\users\권나현\appdata\local\programs\python\python313\lib\site-packages\camelcase\*
# Proceed (Y/n)? Y
#   Successfully uninstalled camelcase-0.2

"""
============================================================
📌 7. 설치된 패키지 목록 조회
============================================================

명령어:
    pip list

출력 예:
    Package         Version
    -----------------------
    camelcase       0.2
    mysql-connector 2.1.6
    pip             18.1
    pymongo         3.6.1
    setuptools      39.0.1
"""
# 설치된 패키지 목록 조회 예제
# 명령 프롬프트에서 실행
# pip list
# Package Version
# ------- -------
# pip     25.0.1

"""
============================================================
📌 중요 요약
============================================================

✔ pip install → 패키지 설치  
✔ pip uninstall → 패키지 제거  
✔ pip list → 설치된 패키지 목록  
✔ pip --version → pip 버전 확인  
✔ pip는 Python의 공식 패키지 관리자  

============================================================
"""
