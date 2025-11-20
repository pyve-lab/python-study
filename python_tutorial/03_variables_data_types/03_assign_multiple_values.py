# Assign Multiple Values
# 1. 여러 변수에 값 할당
# 파이썬에서는 한 줄에서 여러 변수에 값을 할당할 수 있습니다.
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 변수의 개수와 값의 개수가 일치하는지 확인하세요. 일치하지 않으면 오류가 발생합니다.

# 2. 하나의 값을 여러 변수에 할당
# 하나의 값을 여러 변수에 할당할 수도 있습니다.
m = n = o = 100
print(m)
print(n)
print(o)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# 3. 언패킹(unpacking)
# 여러 변수에 값을 할당할 때, 리스트나 튜플과 같은 컬렉션을 사용하여 언패킹할 수도 있습니다.
fruits = ["Mango", "Pineapple", "Grapes"]
a, b, c = fruits
print(a)
print(b)
print(c)

colors = ["Red", "Green", "Blue"]
r, g, b = colors
print(r)
print(g)
print(b)