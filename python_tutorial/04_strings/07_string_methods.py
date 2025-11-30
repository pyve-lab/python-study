# String Methods
# 파이썬 문자열 내장 메서드 (String Methods) 목록

# 참고: 모든 문자열 메서드는 새로운 값을 반환하며, 원래 문자열(original string)을 변경하지 않습니다.

# capitalize()        : 문자열의 첫 글자를 대문자로 변환하여 반환
# casefold()          : 문자열을 소문자로 변환 (lower()보다 강력한 유니코드 기반의 소문자 변환)
# center(width, fill) : 지정된 너비(width)의 중앙에 문자열을 배치하고, 남은 공간을 지정된 문자(fill)로 채워서 반환
# count(sub, start, end): 문자열에서 지정된 값(sub)이 나타나는 횟수를 반환
# encode(encoding, errors): 문자열의 인코딩된 버전을 반환
# endswith(suffix, start, end): 문자열이 지정된 접미사(suffix)로 끝나면 True를 반환
# expandtabs(tabsize) : 탭 문자(\t)의 크기(tabsize)를 설정하여 문자열을 반환
# find(sub, start, end): 문자열에서 지정된 값(sub)을 찾아, 처음 발견된 위치(인덱스)를 반환 (찾지 못하면 -1 반환)
# format(kwargs)      : 문자열의 형식을 지정된 값으로 지정하여 반환
# format_map(mapping) : 딕셔너리 매핑을 사용하여 문자열 형식을 지정하여 반환
# index(sub, start, end): 문자열에서 지정된 값(sub)을 찾아, 처음 발견된 위치(인덱스)를 반환 (찾지 못하면 오류 발생)
# isalnum()           : 문자열의 모든 문자가 영숫자(알파벳 A-z, 숫자 0-9)이면 True를 반환
# isalpha()           : 문자열의 모든 문자가 알파벳(A-z)이면 True를 반환
# isascii()           : 문자열의 모든 문자가 ASCII 문자이면 True를 반환
# isdecimal()         : 문자열의 모든 문자가 10진수이면 True를 반환
# isdigit()           : 문자열의 모든 문자가 숫자이면 True를 반환
# isidentifier()      : 문자열이 유효한 식별자(변수명 등)이면 True를 반환
# islower()           : 문자열의 모든 문자가 소문자이면 True를 반환
# isnumeric()         : 문자열의 모든 문자가 숫자(numeric)이면 True를 반환
# isprintable()       : 문자열의 모든 문자가 출력 가능한 문자이면 True를 반환
# isspace()           : 문자열의 모든 문자가 공백(whitespace)이면 True를 반환
# istitle()           : 문자열이 제목 규칙(각 단어의 첫 글자가 대문자)을 따르면 True를 반환
# isupper()           : 문자열의 모든 문자가 대문자이면 True를 반환
# join(iterable)      : 반복 가능한 객체(iterable)의 요소를 문자열로 결합하여 반환
# ljust(width, fill)  : 지정된 너비(width)의 왼쪽을 정렬하고, 남은 공간을 지정된 문자(fill)로 채워서 반환
# lower()             : 문자열을 소문자로 변환하여 반환
# lstrip(chars)       : 문자열의 왼쪽(시작)에서 지정된 문자(chars)들을 제거한 버전을 반환
# maketrans(x, y, z)  : 번역에 사용될 번역 테이블을 반환
# partition(separator): 문자열이 지정된 구분자(separator)를 기준으로 세 부분(튜플)으로 분할된 것을 반환
# replace(old, new, count): 지정된 문자열(old)을 다른 문자열(new)로 교체하여 반환 (교체 횟수 count 지정 가능)
# rfind(sub, start, end): 문자열에서 지정된 값(sub)을 오른쪽 끝에서부터 찾아, 마지막 발견 위치(인덱스)를 반환 (찾지 못하면 -1 반환)
# rindex(sub, start, end): 문자열에서 지정된 값(sub)을 오른쪽 끝에서부터 찾아, 마지막 발견 위치(인덱스)를 반환 (찾지 못하면 오류 발생)
# rjust(width, fill)  : 지정된 너비(width)의 오른쪽을 정렬하고, 남은 공간을 지정된 문자(fill)로 채워서 반환
# rpartition(separator): 문자열이 지정된 구분자(separator)를 기준으로 오른쪽 끝에서부터 세 부분(튜플)으로 분할된 것을 반환
# rsplit(separator, maxsplit): 지정된 구분자(separator)를 기준으로 오른쪽 끝에서부터 문자열을 분할하여 리스트로 반환
# rstrip(chars)       : 문자열의 오른쪽(끝)에서 지정된 문자(chars)들을 제거한 버전을 반환
# split(separator, maxsplit): 지정된 구분자(separator)를 기준으로 문자열을 분할하여 리스트로 반환
# splitlines(keepends): 줄 바꿈을 기준으로 문자열을 분할하고 리스트로 반환
# startswith(prefix, start, end): 문자열이 지정된 접두사(prefix)로 시작하면 True를 반환
# strip(chars)        : 문자열의 양쪽 끝에서 지정된 문자(chars)들을 제거한 버전을 반환
# swapcase()          : 대소문자를 서로 교체하여 반환 (대문자는 소문자로, 소문자는 대문자로)
# title()             : 문자열을 제목 형식(각 단어의 첫 글자만 대문자)으로 변환하여 반환
# translate(table)    : 지정된 번역 테이블(table)에 따라 문자열을 번역하여 반환
# upper()             : 문자열을 대문자로 변환하여 반환
# zfill(width)        : 문자열 시작 부분에 지정된 숫자(width)만큼 0을 채워서 반환