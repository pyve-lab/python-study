####################################################################################
# 파이썬 가상 환경
####################################################################################

#######################################
# 가상 환경이란 무엇인가요?
#######################################
# Python의 가상 환경은 Python 프로젝트를 실행하고 테스트할 수 있는 컴퓨터의 격리된 환경입니다.
# 다른 프로젝트나 원래 Python 설치를 방해하지 않고 프로젝트별 종속성을 관리할 수 있습니다.
# 가상 환경을 각 Python 프로젝트를 위한 별도의 컨테이너로 생각해 보세요. 각 컨테이너는 다음과 같습니다.

# 자체 Python 인터프리터가 있습니다
# 자체 설치된 패키지 세트가 있습니다.
# 다른 가상 환경과 분리되어 있습니다
# 동일한 패키지의 여러 버전을 가질 수 있습니다.

# 가상 환경을 사용하는 것이 중요한 이유는 다음과 같습니다.

# 프로젝트 간 패키지 버전 충돌을 방지합니다.
# 프로젝트를 더욱 휴대하기 쉽고 재현 가능하게 만듭니다.
# 시스템 Python 설치를 깨끗하게 유지합니다.
# 다양한 Python 버전으로 테스트 가능

#######################################
# 가상 환경 만들기
#######################################
# venvPython에는 가상 환경을 만드는 내장 모듈이 있습니다.
# 컴퓨터에 가상 환경을 만들려면 명령 프롬프트를 열고 프로젝트를 만들 폴더로 이동한 후 다음 명령을 입력하세요.
#
# 예
# 다음 명령을 실행하여 다음과 같은 이름의 가상 환경을 만듭니다 myfirstproject.

# 맥OS/리눅스
# $ python -m venv myfirstproject

# 이렇게 하면 가상 환경이 설정되고 다음과 같이 하위 폴더와 파일이 있는 "myfirstproject"라는 폴더가 생성됩니다.

# 결과
# 파일/폴더 구조는 다음과 같습니다.
# myfirstproject
#   Include
#   Lib
#   Scripts
#   .gitignore
#   pyvenv.cfg

#######################################
# 가상 환경 활성화
#######################################
# 가상 환경을 사용하려면 다음 명령을 사용하여 활성화해야 합니다.

# 예
# 가상 환경을 활성화합니다.

# 맥OS/리눅스
# $ source myfirstproject/bin/activate
# ham@janghyemin-ui-MacBookPro Python_Tutorial % source myfirstproject/bin/activate
# ((myfirstproject) ) ham@janghyemin-ui-MacBookPro Python_Tutorial %

# 활성화 후, 현재 활성 환경에서 작업 중이라는 메시지가 표시됩니다.

# 결과
# 가상 환경이 활성화되면 명령줄은 다음과 같습니다.
# 맥OS/리눅스
# (myfirstproject) ... $

#######################################
# 패키지 설치
#######################################
# 가상 환경이 활성화되면 .을 사용하여 패키지를 설치할 수 있습니다 pip.
# 'cowsay'라는 패키지를 설치하겠습니다.

# 예
# 가상 환경에 'cowsay'를 설치하세요:

# 맥OS/리눅스
# (myfirstproject) ... $ pip install cowsay

# 결과
# 'cowsay'는 가상 환경에만 설치됩니다.

# ((myfirstproject) ) ham@janghyemin-ui-MacBookPro Python_Tutorial % pip install cowsay
# Collecting cowsay
#   Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1
#
# [notice] A new release of pip is available: 25.0.1 -> 25.3
# [notice] To update, run: pip install --upgrade pip

#######################################
# 패키지 사용
#######################################
# 이제 가상 환경에 'cowsay' 모듈이 설치되었으므로 이를 사용하여 말하는 소를 표시해 보겠습니다.
# 컴퓨터에 '라는 파일을 만드세요 . 원하는 곳에 저장하셔도 되지만, 폴더 와test.py 같은 위치에 저장하겠습니다 . 폴더가 myfirstproject아니라 같은 위치에요.
# 파일을 열고 다음 세 줄을 삽입하세요.

# 예
# 두 줄을 삽입하세요 test.py:

# 테스트.py
# import cowsay
#
# cowsay.cow("Good Mooooorning!")
# 그런 다음 가상 환경에 있는 동안 파일을 실행해 보세요.

# 예
# test.py가상 환경에서 실행 :
#
# 맥OS/리눅스
# (myfirstproject) ... $ python test.py

# 결과적으로 터미널에 소가 나타납니다.

# 결과
# 'cowsay' 모듈의 목적은 입력된 내용을 말하는 소를 그리는 것입니다.

# ((myfirstproject) ) ham@janghyemin-ui-MacBookPro Python_Tutorial % python test.py
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

#######################################
# 가상 환경 비활성화
#######################################
# 가상 환경을 비활성화하려면 다음 명령을 사용하세요.

# 예
# 가상 환경 비활성화:

# 맥OS/리눅스
# (myfirstproject) ... $ deactivate

# 결과적으로 이제 일반 명령줄 인터페이스로 돌아왔습니다.
# 결과
# 일반 명령줄 인터페이스:

# 맥OS/리눅스
# $

# 가상 환경 외부에서 파일을 실행하려고 하면 test.py'cowsay'가 누락되어 오류가 발생합니다. 이 파일은 가상 환경에만 설치되었습니다.

# 예
# test.py가상 환경 외부에서 실행 :
# 맥OS/리눅스
# python test.py

# 결과
# 'cowsay'가 없어서 오류가 발생했습니다:
# Traceback (most recent call last):
#   File "/Users/ham/Desktop/PyLab/Python_Tutorial/test.py", line 1, in <module>
#     import cowsay
# ModuleNotFoundError: No module named 'cowsay'

# 참고: 가상 환경은 myfirstproject여전히 ​​존재하지만, 활성화되지 않았습니다. 가상 환경을 다시 활성화하면 파일 을 실행할 수 test.py 있으며 다이어그램이 표시됩니다.

#######################################
# 가상 환경 삭제
#######################################
# 가상 환경에서 작업하는 또 다른 장점은 어떤 이유로 가상 환경을 삭제하고 싶을 때 해당 가상 환경에 의존하는 다른 프로젝트가 없고, 지정된 가상 환경에 있는 모듈과 파일만 삭제된다는 것입니다.
# 가상 환경을 삭제하려면 모든 콘텐츠가 포함된 폴더를 삭제하면 됩니다. 파일 시스템에서 직접 삭제하거나 다음과 같이 명령줄 인터페이스를 사용할 수 있습니다.

# 예
# myfirstproject명령줄 인터페이스에서 삭제 :

# 맥OS/리눅스
# $ rm -rf myfirstproject

# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# What is the built-in Python module for creating virtual environments?

# virt
# environ
# vrlnv
# venv       # Correct Answer!