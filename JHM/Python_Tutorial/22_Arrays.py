####################################################################################
# 파이썬 배열
####################################################################################

# 참고: Python에는 배열에 대한 기본 지원이 없지만 대신 Python 리스트를 사용할 수 있습니다.

#######################################
# 배열
#######################################
# 참고: 이 페이지에서는 LISTS를 ARRAYS로 사용하는 방법을 보여줍니다. 하지만 Python에서 배열을 사용하려면 NumPy 라이브러리 와 같은 라이브러리를 가져와야 합니다 .
# 배열은 하나의 변수에 여러 값을 저장하는 데 사용됩니다.

# 예
# 자동차 이름을 포함하는 배열을 만듭니다.
cars = ["Ford", "Volvo", "BMW"]

#######################################
# 배열이란 무엇인가?
#######################################
# 배열은 한 번에 두 개 이상의 값을 저장할 수 있는 특수한 변수입니다.
# 항목 목록(예: 자동차 이름 목록)이 있는 경우 자동차를 단일 변수에 저장하는 방식은 다음과 같습니다.

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
# 하지만 자동차 목록을 반복해서 특정 자동차를 찾고 싶다면 어떨까요? 자동차가 3대가 아니라 300대라면 어떨까요?
# 해결책은 배열입니다!
# 배열은 하나의 이름으로 여러 값을 보관할 수 있으며, 인덱스 번호를 참조하여 값에 액세스할 수 있습니다.

#######################################
# 배열의 요소에 접근하기
#######################################
# 배열 요소는 인덱스 번호를 참조하여 참조합니다.

# 예
# 첫 번째 배열 항목의 값을 가져옵니다.
x = cars[0]

# 예
# 첫 번째 배열 항목의 값을 수정합니다.
cars[0] = "Toyota"

#######################################
# 배열의 길이
#######################################
# 이 메서드를 사용하여 len()배열의 길이(배열에 있는 요소의 개수)를 반환합니다.

# 예
# 배열 의 요소 개수를 반환합니다 cars.
x = len(cars)
# 참고: 배열의 길이는 항상 가장 높은 배열 인덱스보다 1 더 큽니다.

#######################################
# 루핑 배열 요소
#######################################
# for in루프를 사용하면 배열의 모든 요소를 ​​반복 할 수 있습니다.

# 예
# 배열 의 각 항목을 인쇄합니다 cars.
for x in cars:
  print(x)
#Toyota
# Volvo
# BMW
# apple

#######################################
# 배열 요소 추가
#######################################
# append()이 메서드를 사용하면 배열에 요소를 추가 할 수 있습니다

# 예
# 배열 에 요소를 하나 더 추가합니다 cars.
cars.append("Honda")

#######################################
# 배열 요소 제거
#######################################
# pop()이 메서드를 사용하면 배열에서 요소를 제거할 수 있습니다.

# 예
# 배열 의 두 번째 요소를 삭제합니다 cars.
cars.pop(1)
# remove()이 메서드를 사용하여 배열에서 요소를 제거할 수도 있습니다.

# 예
# 값이 "Volvo"인 요소를 삭제합니다.

# cars.remove("Volvo")
# 참고: 목록의 remove()메서드는 지정된 값의 첫 번째 발생 항목만 제거합니다.

#######################################
# 배열 메서드
#######################################
# Python에는 목록/배열에 사용할 수 있는 내장 메서드 세트가 있습니다.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# 참고: Python에는 배열에 대한 기본 지원이 없지만 대신 Python 리스트를 사용할 수 있습니다.


# QQQQQQQQQQQQQQQQQQ
# Exercise
# QQQQQQQQQQQQQQQQQQ
# Python Lists can be used as arrays.
# What will be the result of the following code:
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])

# apple       # Correct Answer!
# banana
# cherry