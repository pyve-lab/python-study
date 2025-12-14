####################################################################################
# 파이썬 날짜시간
####################################################################################

#######################################
# 파이썬 날짜
#######################################
# Python의 날짜는 그 자체로 독립적인 데이터 유형이 아니지만, datetime날짜를 날짜 객체로 처리하기 위해 명명된 모듈을 가져올 수 있습니다.

# 예
# datetime 모듈을 가져와서 현재 날짜를 표시합니다.
import datetime

x = datetime.datetime.now()
print(x)
# 2025-12-02 22:21:50.122974

#######################################
# 날짜 출력
#######################################
# 위의 예제 코드를 실행하면 결과는 다음과 같습니다.

# 2025-12-02 22:17:14.446793
# 날짜에는 년, 월, 일, 시, 분, 초, 마이크로초가 포함됩니다.

# 이 datetime모듈에는 날짜 객체에 대한 정보를 반환하는 여러 가지 방법이 있습니다.
# 다음은 몇 가지 예입니다. 이 장의 뒷부분에서 이에 대해 자세히 알아보겠습니다.

# 예
# 요일의 연도와 이름을 반환합니다.
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
# 2025
# Tuesday

#######################################
# 날짜 객체 생성
#######################################
# 날짜를 생성하려면 모듈 datetime()의 클래스(생성자) 를 사용하면 됩니다 datetime.
# 이 datetime()클래스는 날짜를 생성하기 위해 년, 월, 일이라는 세 가지 매개변수가 필요합니다.

# 예
# 날짜 객체를 만듭니다.
import datetime

x = datetime.datetime(2020, 5, 17)
print(x)
# 2020-05-17 00:00:00

# 이 datetime()클래스는 시간과 시간대(시, 분, 초, 마이크로초, tzone)에 대한 매개변수도 받지만 이는 선택 사항이며 기본값은 0, ( Nonetimezone의 경우)입니다.

#######################################
# strftime() 메서드
#######################################
# 해당 datetime객체에는 날짜 객체를 읽을 수 있는 문자열로 포맷하는 메서드가 있습니다.
# 이 메서드는 호출되며 반환된 문자열의 형식을 지정하기 위해 strftime()하나의 매개변수를 사용합니다. format

# 예
# 월 이름을 표시합니다.
import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
# June

# 모든 법적 형식 코드에 대한 참조:
# Directive	Description	Example
# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %C	Century	20
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 weeknumber (01-53)	01


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Consider the following code:
import datetime
x = datetime.datetime
# Which syntax will print the current date?

# print(x.datetime())
# print(x.date())
# print(x.now())          # Correct Answer!