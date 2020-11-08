# 09.generator functions.py

# Generator? iterator 객체의 한 종류. 제너레이터를 호출하면서 next함수를 호출하면 값을 하나씩 얻을 수 있다.
# 제너레이터를 만드는 방법 2가지
# A. Generator 함수
# B. Generator 표현식

# 0.제너레이터 함수 만들기
def gen_num(): #제너레이터 함수 정의
    print('first number')
    yield 1 #yield가 들어가면 제너레이터가 된다.
    print('second number')
    yield 2
    print('third number')
    yield 3

# yield 내다, 던지다

gen = gen_num()     #제너레이터 객체 생성

next(gen)   # iterator객체이기 때문에 next메서드를 호출 할 수 있다.
next(gen)
next(gen)
# next(gen)   # 다음 값이 없는대도 호출하면 stopIteration예외가 발생한다.

# 1.제너레이터 함수만들기2

def gen_for():
    for i in [1, 2, 3]:
        print(i)
        yield i


g = gen_for()
next(g)
next(g)
next(g)
# next(g)   # 다음 값이 없는대도 호출하면 stopIteration예외가 발생한다.

# 2. 제너레이터의 장점
# 2.1.일반적인 리스트 생산 방식으로 만들었을 때
def pows(s):
    r = []
    for i in s:
        r.append(i**2)
    return r

st = pows([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in st :
    print(i, end=' ')
print()
import sys
print(sys.getsizeof(st))

# 2.2.제너레이터를 사용했을 때의 장점 : 메모리를 효율적으로 사용한다.
# map과 filter도 제너레이터 객체이다.
def gpows(s):
    for i in s:
        yield i**2
st = gpows([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in st:
    print(i, end=' ')   #lazy evaluation : 필요할 때 만들므로 메모리가 절약된다.
print()
print(sys.getsizeof(st))

# for문 대신 yield from ns로 줄여 쓸 수 있다.
def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    for i in ns:
        yield i
g = get_nums()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    yield from ns
g = get_nums()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))






