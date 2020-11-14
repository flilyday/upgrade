# 06.functions & lambda.py

# 0. 객체처럼 다뤄지는 함
# 파이썬에서는 모든 것이 객체이다
x = 3.0
print(type(x))  #실수도 객체
print(x.is_integer())


# 함수도 객체다
def func1(n):
    return n

def func2():
    print("Hello!")

print(type(func1))
print(type(func2)) #함수도 객체


# 함수를 호출하고 반환하는 것도 가능하다
def say1():
    print('hello')

def say2():
    print('hi')

def caller(fct):
    fct() #fct를 통해 매개변수로 함수를 호출. 함수도 객체이기 때문에 매개변수로 전달하고 반환이 가능하다.

caller(say1)
caller(say2)


def fct_fac(n):
    def exp(x):
        return x**n
    return exp

f2 = fct_fac(2)
f3 = fct_fac(3)

print(f2(4))
print(f3(4))

# 1. Lambda 함수
# 특징
# A. 이름이 필요 없다(이름을 붙이는 이유는 참조값으로 나중에 호출하기 위해서인데, 이미 호출하기로 약속되어 있기 때문이다)
# B. 정의부와 호출부를 한 문장으로 표현한다.
# C. 식을 간결하게 쓰기 위한 문법적인 약속이다.

# 1.1. 기본형식
ref = lambda s : print(s)   # 람다함수의 기반 정의. 함수의 이름을 정의하지 않는다. 다만 나중에 쓰기 위해서 참조값을 좌측에 붙여 놓는다.
# 참조값 = [매개변수 : 결과값]
ref('hello')

# 1.2. 매개변수가 없는 람다함수 형식
s = lambda : print('hello')
s

# 1.3. 위 예제 fct_fac(n)함수를 람다로 고치기
def fct_fac(n):
    return lambda x : x**n
f3 = fct_fac(2)
f4 = fct_fac(3)

print(f3(4))
print(f4(4))