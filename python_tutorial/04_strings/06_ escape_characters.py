# Escape Characters
# 이스케이프 문자 (Escape Characters)
# 1. 이스케이프 문자란?
# 문자열 내부에 사용이 허용되지 않는 (illegal) 문자를 삽입하기 위해 사용하는 특수 문자입니다.
# 구성: 이스케이프 문자는 백슬래시 \ 뒤에 삽입하려는 문자가 오는 형식입니다.


# 2. 허용되지 않는 문자 처리 예시문제 상황: 
# 문자열을 큰따옴표(")로 둘러쌌는데, 그 안에 다시 큰따옴표를 사용하려고 하면 오류가 발생합니다.
# Python 오류 발생 예시:
# 문자열 안에 큰따옴표가 있어 구문 오류가 발생합니다.
# txt = "We are the so-called "Vikings" from the north."

# 해결책: 이스케이프 문자 **\"**를 사용하여 큰따옴표를 문자열의 일부로 인식하게 만듭니다.
# 이스케이프 문자로 문제를 해결하는 예시:
# \" 를 사용하여 문자열 내부에 큰따옴표를 허용
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# 출력: We are the so-called "Vikings" from the north.


# 파이썬에서 사용되는 주요 이스케이프 문자 목록

# \' : Single Quote (작은따옴표) - 작은따옴표로 둘러싸인 문자열 안에 작은따옴표 삽입
# \\ : Backslash (백슬래시) - 문자열 안에 백슬래시 문자 자체를 출력
# \n : New Line (줄 바꿈) - 커서를 다음 줄의 시작 위치로 이동
# \r : Carriage Return (캐리지 리턴) - 커서를 현재 줄의 맨 앞으로 이동
# \t : Tab (탭) - 수평 탭(일반적으로 4~8칸 공백) 삽입
# \b : Backspace (백스페이스) - 커서를 한 칸 뒤로 이동
# \f : Form Feed (폼 피드) - 다음 페이지의 시작 위치로 이동 (프린터 출력용)
# \ooo : Octal value (8진수 값) - 8진수 값에 해당하는 문자 삽입
# \xhh : Hex value (16진수 값) - 16진수 값에 해당하는 문자 삽입