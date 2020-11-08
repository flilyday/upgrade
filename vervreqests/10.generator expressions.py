# 10.generator expressions.py

# 함수 -> 람다식 : 간단한 함수는 람다식으로 대체
# 제너레이터 함수 -> 제너레이터 표현식 : 제너레이터를 만드는 함수를 표현식으로 대체

def show_all(s):
    for i in s:
        print(i, end=' ')

st = [2*i for i in range(1, 10)]
show_all(st)
print()

g = [2*i for i in range(1, 10)]
show_all(g)
print()

# 제너레이터 함수 표현식 : [] -> () 표현식을 ()로 바꿔주기만 하면 생성이 된다.
g = [2*i for i in range(1, 10)]
st = (2*i for i in range(1, 10))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
# print(next(st))
print()

# 제너레이터 표현식 또다른 예제2
def two():
    print('two')
    return 2

g = (two()*i for i in range(1, 10) )
print(next(g))
print(next(g))

# 중괄호의 생략
def show_all(s):
    for i in s:
        print(i, end=' ')

show_all((i*2 for i in range(1, 10)))
show_all(i*2 for i in range(1, 10))
# 소괄호가 두번 나와 보기 좋지 않아, 제너레이터를 인자로 전달 할 때는 한 번의 소괄호만 쓸 수 있도록 문법을 확장시켜 놓았다.