# 32.decorator.py
# decorator : 꾸며주는 역할을 하는 함수 또는 클래스를 뜻함


# 0.기본함수
def smile() :
    print('^-^')

def confused():
    print('@_@')

smile()
confused()

# 1. 기본함수를 꾸며주고 싶을 때 쓰는 객체를 데코레이터라 한다.
# 꾸미기란? 기능이나 액션을 추가
# smile() -> decorator -> smile()+@

def deco(func):
    def df():
        print('emoticon!')  #추가된 기능
        func()              #원래 있던 기능
        print('emoticon!')  #추가된 기능
    return df

smile = deco(smile)
smile()

confused = deco(confused)
confused()

# 2.전달인자기 있는 함수 기반의 데코레이터
def adder2(n1, n2):
    return n1 + n2

def adder3(n1, n2, n3):
    return n1 + n2 + n3

# 인자의 갯수와 상관없이 합계식을 보여주는 데코레이터를 만들려고 하면?

def adder_deco(func):   #데코레이터 함수
    def df(*args):      #전달인자를 튜플로 묶는다.
        print(*args, sep='+', end=' ')  #전달받은 튜플을 언패킹 한다
        print('= {0}'.format(func(*args)))
    return df

adder2 = adder_deco(adder2)
adder2(1, 2)

adder3 = adder_deco(adder3)
adder3(1, 2, 3)


# 3. @기반으로 보기
# 3.1. 기본식 : 데코레이터를 정의하고 통과시키기
def deco(func):
    def df():
        print('emoticon!')  #추가된 기능
        func()              #원래 있던 기능
        print('emoticon!')  #추가된 기능
    return df

def smile() :
    print('^-^')    #함수 정의

smile = deco(smile) #데코레이터를 통과 시키기
smile()

# 3.2. decorator 표식('@')을 이용하여 쓰기
@deco    #함수를 정의할 때부터 데코레이터를 통과시킨다고 명시한다. 3.1.과 같은 식이 된다.
def smile():
    print('ㅡㅡ^')
smile()

# 4. adder 데코레이터의 예제
def adder_deco(func):
    def ad(*args):
        print(*args, sep='+', end=' ')
        print('= {0}'.format(func(*args)))
    return ad

@adder_deco
def adder(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

adder(1, 2, 3, 4)

print('-')
# 5.중첩 데코레이터

def deco1(fnc):
    def inner():
        print('deco1')
        fnc()
    return inner

def deco2(fnc):
    def inner():
        print('deco2')
        fnc()
    return inner

@deco1
@deco2
def smile():
    print('^^')

def main():
    smile()     #simple이 deco 되는 과정 : 새로운 simple = deco1(deco2(simple))

main()


