# 08.list comprehension alternating two functions.py
# 두 함수(맵과 필터)를 대체하는 리스트 컴프리헨션
# 맵과 필터는 리스트 컴프리헨션으로 대체 가능하다.

# 1.1.맵을 이용한 제곱값 리스트 만들기
st1 = [1, 2, 3]
st2 = list(map(lambda n:n**2, st1))
print(st2)

# 1.2.리스트 컴프리헨션을 이용한 리스트 만들기
st1 = [1, 2, 3]
st2 = [n**2 for n in st1]
print(st2)

# 2.1.필터를 이용한 리스트 만들기
st = [1, 2, 3, 4, 5]
ost = list(filter(lambda n:n%2, st))
print(ost)

# 2.2.리스트 컴프리헨션을 이용한 리스트 만들기
st = [1, 2, 3, 4, 5]
ost = [n for n in st if n%2]
print(ost)

# 3.1.맵과 필터를 이용한 리스트 만들기
st = list(range(1, 11, 1))
fst = list(map(lambda n:n**2, filter(lambda n:n%2, st)))
print(fst)

# 3.1.리스트 컴프리헨션을 이용한 리스트 만들기
st = list(range(1, 11, 1))
fst = [n**2 for n in st if n%2 ]
print(fst)




