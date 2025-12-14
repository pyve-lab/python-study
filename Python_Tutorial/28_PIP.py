####################################################################################
# 파이썬 PIP
####################################################################################

#######################################
# PIP란 무엇인가요?
#######################################
# PIP는 Python 패키지 또는 모듈에 대한 패키지 관리자입니다.

# 참고: Python 버전 3.4 이상을 사용하는 경우 PIP가 기본적으로 포함되어 있습니다.

#######################################
# 패키지란 무엇인가요?
#######################################
# 패키지에는 모듈에 필요한 모든 파일이 들어 있습니다.
# 모듈은 프로젝트에 포함할 수 있는 Python 코드 라이브러리입니다.

#######################################
# PIP가 설치되어 있는지 확인하세요
#######################################
# 명령줄을 사용하여 Python 스크립트 디렉터리 위치로 이동하고 다음을 입력합니다.

# 예
# PIP 버전 확인:

# pip --version

#######################################
# PIP 설치
#######################################
# PIP가 설치되어 있지 않으면 이 페이지에서 다운로드하여 설치할 수 있습니다: https://pypi.org/project/pip/

#######################################
# 패키지 다운로드
#######################################
# 패키지를 다운로드하는 것은 매우 쉽습니다.
# 명령줄 인터페이스를 열고 PIP에 원하는 패키지를 다운로드하라고 지시합니다.
# 명령줄을 사용하여 Python 스크립트 디렉터리 위치로 이동하고 다음을 입력합니다.

# 예
# "camelcase"라는 패키지를 다운로드하세요:
# pip install camelcase
# 이제 첫 번째 패키지를 다운로드하고 설치했습니다!

#######################################
# 패키지 사용
#######################################
# 패키지를 설치하면 사용할 준비가 됩니다.
# "camelcase" 패키지를 프로젝트에 가져옵니다.

# 예
# "camelcase"를 가져와서 사용하세요:
import camelcase

c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt))
# Hello World

#######################################
# 패키지 찾기
#######################################
# 더 많은 패키지는 https://pypi.org/ 에서 찾아보세요.

#######################################
# 패키지 제거
#######################################
# 다음 명령을 사용하여 uninstall패키지를 제거합니다.

# 예
# "camelcase"라는 패키지를 제거합니다.

# pip uninstall camelcase

# PIP 패키지 관리자는 camelcase 패키지를 제거할 것인지 확인하라는 메시지를 표시합니다.

# Uninstalling camelcase-02.1:
#   Would remove:
#     c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
#     c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
# Proceed (y/n)?
# 누르면 y패키지가 제거됩니다.

#######################################
# 패키지 목록
#######################################
# 다음 명령을 사용하여 list시스템에 설치된 모든 패키지를 나열합니다.

# 예
# 설치된 패키지 나열:
# pip list
# 결과:
# ham@janghyemin-ui-MacBookPro Python_Tutorial % pip list
# Package Version
# ------- -------
# pip     25.3

# Package         Version
# -----------------------
# camelcase       0.2
# mysql-connector 2.1.6
# pip             18.1
# pymongo         3.6.1
# setuptools      39.0.1


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# In the world of Python, what describes PIP best?

# PIP is a module used for drawing
# PIP is a module used for handling large amounts of data
# PIP is a package manager for Python modules               # Correct Answer!