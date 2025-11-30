"""
============================================================
📌 Python 가상환경(virtual environment)란?
============================================================

파이썬 가상환경은 **특정 프로젝트만을 위한 독립된 실행 공간**.
● 프로젝트마다 별도의 Python 인터프리터 사용
● 프로젝트마다 서로 다른 패키지 버전 유지 가능
● 시스템 전체 Python 환경을 오염시키지 않음
● 패키지 충돌 방지, 재현성 향상

즉, "프로젝트별로 분리된 컨테이너" 역할.
"""

"""
============================================================
📌 1. 가상환경 만들기 (venv)
============================================================

윈도우 / macOS / 리눅스 공통:
    python -m venv myproject

생성된 구조:
    myproject/
        ├─ Lib/
        ├─ Scripts/ (또는 bin/)
        ├─ Include/
        ├─ pyvenv.cfg
"""

"""
============================================================
📌 2. 가상환경 활성화
============================================================

Windows:
    myproject\Scripts\activate

macOS / Linux:
    source myproject/bin/activate

활성화되면:
    (myproject) C:\Users\...>
"""
# 파이썬 가상환경 활성화 예제
# PS C:\Users\권나현\Desktop\python-study> myproject\Scripts\activate
# (myproject) PS C:\Users\권나현\Desktop\python-study> 

"""
============================================================
📌 3. 패키지 설치 (가상환경 안에서만 설치됨)
============================================================

예:
    pip install cowsay

→ 시스템 전체가 아닌 가상환경 내부에만 설치됨.
"""
# 가상환경 내 패키지 설치 예제
# (myproject) PS C:\Users\권나현\Desktop\python-study> pip install cowsay
# Collecting cowsay
#   Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1

# [notice] A new release of pip is available: 25.0.1 -> 25.3
# [notice] To update, run: python.exe -m pip install --upgrade pip

"""
============================================================
📌 4. 패키지 사용 예 (test.py)
============================================================

test.py:
    import cowsay
    cowsay.cow("Good Mooooorning!")

실행:
    python test.py

터미널 출력:
    ________________
    | Good Mooooorning! |
    ...
"""
# 가상환경 내 패키지 사용 예제 (test.py)

# test.py
# import cowsay
# cowsay.cow("Good Mooooorning!")

# (myproject) PS C:\Users\권나현\Desktop\python-study\myproject> cd C:\Users\권나현\Desktop\python-study\myproject
# >> .\Scripts\activate
# >> python test.py
#   _________________
# | Good Mooooorning! |
#   =================
#                  \
#                   \
#                     ^__^
#                     (oo)\_______
#                     (__)\       )\/\
#                         ||----w |
#                         ||     ||
"""
============================================================
📌 5. 가상환경 비활성화
============================================================

    deactivate

→ 다시 일반 시스템 환경으로 돌아옴.
"""
# 파이썬 가상환경 비활성화 예제

# (myproject) PS C:\Users\권나현\Desktop\python-study\myproject> deactivate
# PS C:\Users\권나현\Desktop\python-study\myproject> 

"""
============================================================
📌 6. 가상환경 밖에서 실행 시 오류
============================================================

가상환경 바깥에서:
    python test.py

오류:
    ModuleNotFoundError: No module named 'cowsay'

→ 해당 패키지는 가상환경 안에만 존재하기 때문.
"""
# 가상환경 밖에서 패키지 사용 시도 예제

# test.py
# import cowsay
# cowsay.cow("Good Mooooorning!")

# PS C:\Users\권나현\Desktop\python-study\myproject> python test.py
# Traceback (most recent call last):
#   File "C:\Users\권나현\Desktop\python-study\myproject\test.py", line 1, in <module>
#     import cowsay
# ModuleNotFoundError: No module named 'cowsay'

"""
============================================================
📌 7. 가상환경 삭제
============================================================

가상환경 폴더 자체를 삭제하면 끝.

Windows:
    rmdir /s /q myproject

macOS/Linux:
    rm -rf myproject
"""
# 파이썬 가상환경 삭제 예제
# Windows:
# rmdir /s /q myproject

# myproject 내부에서 실행 시 오류 발생
# PS C:\Users\권나현\Desktop\python-study\myproject> rmdir /s /q myproject
# Remove-Item : '/q' 인수를 허용하는 위치 매개 변수를 찾을 수 없습니다.
# 위치 줄:1 문자:1
# + rmdir /s /q myproject
# + ~~~~~~~~~~~~~~~~~~~~~
#     + CategoryInfo          : InvalidArgument: (:) [Remove-Item], ParameterBindingException
#     + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.RemoveItemCo  
#    mmand

# 올바른 위치에서 실행(cmd 사용)
# PS C:\Users\권나현\Desktop\python-study> cmd /c rmdir /s /q myproject
# cmd /c rmdir /s /q myproject

# PowerShell에서는 다음 명령어 사용
# # PS C:\Users\권나현\Desktop\python-study> Remove-Item -Recurse -Force .\myproject
# Remove-Item -Recurse -Force .\myproject

"""
============================================================
📌 핵심 요약
============================================================

✔ venv는 프로젝트별로 분리된 Python 환경  
✔ 패키지 버전 충돌 방지  
✔ 시스템 Python을 깨끗하게 유지  
✔ activate / deactivate 로 사용 여부 제어  
✔ 삭제는 폴더 삭제로 끝  

============================================================
"""
