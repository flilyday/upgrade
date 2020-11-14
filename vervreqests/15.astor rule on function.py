# 15.astor rule on function.py

# 0.일반적인 경우
# 함수를 호출할 때 : 푼다.
# 함수를 정의할 때 : 묶는다.

def who(a, b, c):
    print(a, b, c, sep=', ')

who(*[1, 2, 3])
who(*(0.1, 0.2, 0.3))
who(*'abc')

# 1.객체를 전달할 때

def who(a, b, c):
    print(a, b, c, sep=', ')

d = dict(a=1, b=2, c=3)
who(*d)     # 키를 풀 때
who(**d)    # 값을 풀 때
who(*(d.items()))    # 값을 풀 때

# 2.일반적인 정의
# def func(*args) : 값들이 튜플로 묶여서 args에 전달된다.
# def func(**args) : 값들이 딕셔너리로 묶여서 args에 전달된다.

# 2.1.값으로 호출할 때
def func(*args):
    print(args)

func()
func(1)
func(1, 2)
func(1, 2, 3)

# 2.2.딕셔너리로 호출할 때
def func(**args):
    print(args)
func()
func(a=1)
func(a=1, b=2)
func(a=1, b=2, c=3)

# 2.3.값,딕셔너리 모두로 호출할 때
def func(*arg1, **arg2):
    print(arg1)
    print(arg2)

func()
func(1, a=1)
func(1, 2, a=1, b=2)