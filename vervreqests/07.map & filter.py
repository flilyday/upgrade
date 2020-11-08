# 07.map & filter.py


# 0. map
def pow(n):
    return n**2

st1 = [1, 2, 3]

# st1리스트 요소 각각의 제곱을 가지는 리스트를 만든다고 할 때 map함수가 없으면 아래처럼 수동으로 해야 한다.
st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])]
print(st2)

# map을 적용했을 때
st2 = list(map(pow, st1)) # map(함수, iterable객체) <- 두번째 전달 대상은 반드시 iterable한 객체여야 한다.
print(st2)


# map 활용 예제

def pow(n):
    return n**2
st1 = [1, 2, 3]
ir = map(pow, st1)

for i in st1:   #st1이 iterator객체이므로 올 수 있다.
    print(i, end=' ')
print()
def dbl(n):
    return n*2

print(list(map(dbl, (1, 2, 3))))
print(list(map(dbl, 'hello')))

# 매개변수가 복수 개일 때 map을 쓰는 방식
def sum(n1, n2):
    return n1+n2
st1 = [1, 2, 3]
st2 = [3, 2, 1]

# st1의 각 n번째 요소와 st2의 각 n번째 요소의 합을 갖는 리스트를 구하고자 할 때
st3 = list(map(sum, st1, st2)) # sum의 첫번째 파라미터에 올 값들을 map의 두번째로, sum의 두번째 파라미터에 올 값들은 map의 세번째로.
print(st3)


# 1. 맵과 결합한 람다
# 1.1. 파이썬의 간결한 특징
st = [1, 2, 3, 4, 5, 6, 7, 8]
print(st[::])
print(st[::1]) #출력단위와 방향을 지정할 수 있다. -를 붙이면 역순이 된다.
print(st[::2])
print(st[::3])
print(st[::-1]) #파이썬의 특징. 요소의 역순을 출력할 때 -1만 하면 된다.

s ='hello'
print(s[::-1])


# 1.2. 리스트 각 요소의 문자값을 역으로 출력하고 싶을 때
def rev(n):
    return n[::-1]

st = ['one', 'two', 'three']

rst = list(map(rev, st))
print(rst)

# 1.3. 위 식을 람다와 결합하기

rst = list(map(lambda s:s[::-1], st))
print(rst)


# 2. filter : 조건에 맞는 요소만 필터링 하여 출
# map(함수, iterable객체) : 함수 -> iterable 객체를 매핑해서 반환

def is_odd(n):
    return n%2

st = [1, 2, 3, 4, 5]
ost = list(filter(is_odd, st))
print(ost)

ost2 = list(filter(lambda o:o%2, st))
print(ost) #위 식을 람다식으로 수정

# filter예제 : 3의 배수만 출력
st3 = list(filter(lambda n : not(n%3), list(range(1, 11, 1))))
print(st3)

# filter예제 : 1~10까지의 각 요소를 제곱해서  중 3의 배수만 필터링
st33 = list(filter(lambda n : not(n%3), map(lambda n:n**2, list(range(1, 11, 1)))))
print(st33)









