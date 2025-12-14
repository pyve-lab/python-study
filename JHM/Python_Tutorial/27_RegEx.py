####################################################################################
# 파이썬 RegEx 정규식
####################################################################################

# 정규 표현식(RegEx)은 검색 패턴을 형성하는 문자 시퀀스입니다.
# 정규 표현식을 사용하면 문자열에 지정된 검색 패턴이 포함되어 있는지 확인할 수 있습니다.

#######################################
# 정규식 모듈
#######################################
# rePython에는 정규 표현식을 다루는 데 사용할 수 있는 이라는 내장 패키지가 있습니다.
# 모듈 가져오기 re:
import re

#######################################
# 파이썬의 정규식
#######################################
# 모듈 을 가져온 후 re정규 표현식을 사용할 수 있습니다.

# 예
# 문자열을 검색하여 "The"로 시작하고 "Spain"으로 끝나는지 확인하세요.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
# YES! We have a match!

#######################################
# 정규식 함수
#######################################
# 이 re모듈은 문자열에서 일치 항목을 검색할 수 있는 함수 세트를 제공합니다.

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

#######################################
# 메타문자
#######################################
# 메타문자는 특별한 의미를 지닌 문자입니다.

# Character	Description	Example
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he.{2}o"
# |	Either or	"falls|stays"
# ()	Capture and group

#######################################
# 깃발
#######################################
# 정규 표현식을 사용할 때 패턴에 플래그를 추가할 수 있습니다.

# Flag	Shorthand	Description
# re.ASCII	re.A	Returns only ASCII matches
# re.DEBUG		Returns debug information
# re.DOTALL	re.S	Makes the . character match all characters (including newline character)
# re.IGNORECASE	re.I	Case-insensitive matching
# re.MULTILINE	re.M	Returns only matches at the beginning of each line
# re.NOFLAG		Specifies that no flag is set for this pattern
# re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches
# re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable

#######################################
# 특수 시퀀스
#######################################
# 특수 시퀀스는 \아래 목록에 있는 문자 중 하나가 뒤에 오는 것으로, 특별한 의미를 갖습니다.

# Character	Description	Example
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
#
# r"ain\b"
#
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
#
# r"ain\B"
#
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

#######################################
# 세트
#######################################
# 집합은 대괄호 안에 []특수한 의미를 지닌 문자들의 집합입니다.

# Set	Description	Try it
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

#######################################
# findall() 함수
#######################################
# 이 findall()함수는 모든 일치 항목을 포함하는 목록을 반환합니다.

# 예
# 모든 일치 항목의 목록을 인쇄합니다.
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# ['ai', 'ai']

# 목록에는 발견된 순서대로 일치 항목이 포함되어 있습니다.
# 일치하는 항목이 없으면 빈 목록이 반환됩니다.

# 예
# 일치하는 항목이 없으면 빈 목록을 반환합니다.
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
# []

#######################################
# search() 함수
#######################################
# 이 search()함수는 문자열에서 일치 항목을 검색하고, 일치 항목이 있으면 Match 객체를 반환합니다.
# 일치하는 항목이 두 개 이상인 경우 첫 번째로 나타난 일치 항목만 반환됩니다.

# 예
# 문자열에서 첫 번째 공백 문자를 검색합니다.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# The first white-space character is located in position: 3

# 일치하는 항목이 없으면 값이 None반환됩니다.

# 예
# 일치하는 결과가 없는 검색을 수행합니다.
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
# None

#######################################
# split() 함수
#######################################
# 이 split()함수는 각 일치 항목에서 문자열이 분할된 목록을 반환합니다.

# 예
# 각 공백 문자에서 분할:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# ['The', 'rain', 'in', 'Spain']

# 매개변수를 지정하여 발생 횟수를 제어할 수 있습니다 maxsplit.

# 예
# 문자열을 처음 나타나는 부분에서만 분할합니다.
import re

txt = "The rain in Spain"
# x = re.split("\s", txt, 1) 이제 이렇게 안된다고 한다
x = re.split("\s", txt, maxsplit=1)
print(x)
# ['The', 'rain in Spain']

#######################################
# sub() 함수
#######################################
# 이 sub()함수는 일치 항목을 선택한 텍스트로 바꿉니다.

# 예
# 모든 공백 문자를 숫자 9로 바꾸세요:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
# The9rain9in9Spain

# 다음 매개변수를 지정하여 교체 횟수를 제어할 수 있습니다 count.

# 예
# 처음 두 개의 발생을 바꾸세요:
import re

txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2) 이것도 경고 오류남
x = re.sub("\s", "9", txt, count=2)

print(x)
# The9rain9in Spain

#######################################
# 일치 객체
#######################################
# Match 객체는 검색 및 결과에 대한 정보를 담고 있는 객체입니다.
# 참고: 일치하는 항목이 없으면 NoneMatch 객체 대신 값이 반환됩니다.

# 예
# Match Object를 반환하는 검색을 수행합니다.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)

print(x) #this will print an object
# <re.Match object; span=(5, 7), match='ai'>

# Match 객체에는 검색과 결과에 대한 정보를 검색하는 데 사용되는 속성과 메서드가 있습니다.

# .span()일치 항목의 시작 및 끝 위치를 포함하는 튜플을 반환합니다.
# .string함수에 전달된 문자열을 반환합니다.
# .group()일치 항목이 있는 문자열 부분을 반환합니다.

# 예
# 첫 번째 일치 발생 위치(시작 및 종료 위치)를 출력합니다.
# 정규 표현식은 대문자 "S"로 시작하는 단어를 찾습니다.

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# (12, 17)

# 예
# 함수에 전달된 문자열을 출력합니다.
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
# The rain in Spain

# 예
# 문자열에서 일치하는 부분을 출력합니다.
# 정규 표현식은 대문자 "S"로 시작하는 단어를 찾습니다.
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# Spain

# 참고: 일치하는 항목이 없으면 NoneMatch 객체 대신 값이 반환됩니다.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Consider the following code:
import re
txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)
# What will be the printed result?

# ['a', 'a']         # Correct Answer!
# 'The rin in Spin'
# 2
