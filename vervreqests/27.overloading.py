# 27.overloading.py
# 연산자 오버로딩 ? 약속 -> 특정 연사자를 썼을 때 파이썬에서 호출해주기로 한 메소드가 불러지는 것
# 연산자 : + - * /

# 1.연산자 오버로딩의 예
class Account:
    def __init__(self, aid, abl):
        self.aid = aid  #계좌번호
        self.abl = abl  #계좌잔액
    def __add__(self, m):   #입금
        self.abl += m
        print('__add__')
    def __sub__(self, m):   #출금
        self.abl -= m
        print('__sub__')
    def __call__(self):     #계좌상황을 문자열로 반환
        print('__call__')
        return str(self.aid) + ':' + str(self.abl)

def main():
    acnt = Account('James01', 100)      #계좌 개설
    acnt + 100      #100원 입금, __add__ 호출로 이어짐
    acnt - 50       #50월 출금,  __sub__ 호출로 이어짐
    print(acnt())

main()


# 2.적절한 형태로 +와 -연산자 오버로딩
# 2.1.일반적인 연사에서의 내부 처리 과정
n1 = 3  #3이라는 객체가 만들어지고 이름표에 n1을 붙인것.
n2 = 5
print(n1 + n2)  #n1+n2의 값이 새로 생성됐지 n1과 n2가 변하지 않았다.
s1 = 'Y'
s2 = 'oon'
print(s1+s2)    #s1+s2의 값이 새로 생성됐지 s1과 s2가 변하지 않았다.
# 그러나 위의 예제에서는 + - 연산의 결과로  acnt의 값이 바뀌고 있다.

# 2.2. + 연산자를 적절히 오버로딩한 예

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)   #새로운 객체 생성 및 반환
    def __call__(self):     #벡터 정보를 문자열로 반환
        return 'Vector({0}, {1})'.format(self.x, self.y)

def main():
    v1 = Vector(3, 3)
    v2 = Vector(7, 7)
    v3 = v1 + v2    #새로운 Vector객체 생성되어 v3에 저장
    print(v1())     #__call__ 호출 결과로 반환되는 문자열 출력
    print(v2())     #__call__ 호출 결과로 반환되는 문자열 출력
    print(v3())     #__call__ 호출 결과로 반환되는 문자열 출력

main()

print('-')

# 3.메소드 __str__의 정의
# 3.1.모든 클래스에 상속되는 __str__매서드
class Simple:
    def __init__(self, i):
        self.i = i
s = Simple(10)  #10이 저장된 Simple객체 생성
print(s.i)
print(s)
print(s.__str__())  #모든 클래스가 상속하는 object클래스에 __str__이 정의되어 있고, 이것을 상속했기 때문에 Simple클래스에 정의하지 않아도 호출이 가능.

# 3.2.__str__오버로딩 하기
class Simple:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return 'Simple({0})'.format(self.i) #'Simple(20)'형태의 문자열 생성 및 반환. 기본으로 상속되는 __str__매서드 오버로딩하기 -> ()연산자로 부르면 특정 값 나오게 하기
s = Simple(20)
print(s)


# 3.3.Vector클래스의 __call__ 대신에 __str__ 로 오버로딩하기
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)   #새로운 객체 생성 및 반환
    def __str__(self):     #object클래스를 오버로딩
        return 'Vector({0}, {1})'.format(self.x, self.y)

def main():
    v1 = Vector(3, 3)
    v2 = Vector(7, 7)
    v3 = v1 + v2    #새로운 Vector객체 생성되어 v3에 저장
    print(v1)     #__str__ 호출 결과로 반환되는 문자열 출력 : print(v1()) 이런식으로 출력할 필요가 없게 됨
    print(v2)     #__str__ 호출 결과로 반환되는 문자열 출력
    print(v3)     #__str__ 호출 결과로 반환되는 문자열 출력

main()

print('-')

# 4.in-place형태의 연산자 오버로딩
# n1 = 3, n2 = 4
# n1 + n2 <- 기본적으로 피 연산자들의 값이 바뀌지 않는다.
# n1 + 5  <- 피 연산자의 값이 바뀐다. 이것을 in-place연산이라고 한다.

# 4.1.immutable객체의 값 변화
n = 5
print(id(n))
n += 1
print(id(n))
# 정수, 문자열은 immutable객체이기 때문에 in-place연산을 하더라도 가리키는 값이 바뀔 수 밖에 없다.

n = [1, 2]
print(id(n))

n += [3]
print(id(n))
# mutable객체인 list를 대상으로 연산을 해보면 값이 바뀌지 않는다.

# 5.Vector클래스에 __iadd__메서드 추가하여 += 연산자 별도 오버로딩
# __add__ : +연산에 대한 오버로딩
# __iadd__ : +=연산에 대한 오버로딩
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):   #벡터의 + 연산
        return Vector(self.x + o.x, self.y + o.y)   #새로운 객체 생성 및 반환
    def __iadd__(self, o):  #벡터의 += 연산
        self.x += o.x
        self.y += o.y
        return self     #v1 += v2의 연산 결과로 v1을 반환. 꼭 넣어줘야 함
    def __str__(self):  #벡터 정보를 문자열로 반환
        return 'Vector({0}, {1})'.format(self.x, self.y)

def main():
    v1 = Vector(2, 2)
    v2 = Vector(7, 7)
    print(v1, id(v1))   #v1과 v1에 저장된 객체의 주소 정보 출력
    v1 += v2            #v1.__add__(v2)
    print(v1, id(v1))   #v1과 v1에 저장된 객체의 주소 정보 출력)

main()

# 6.Account클래스 수정하기
#고객의 계좌정보이기 때문에
# +보다 += 연산이 계좌 잔액이 증가하는 입금 연산에 어울린다
# -보다 -= 연산이 계좌 잔액이 증가하는 입금 연산에 어울린다

class Account:
    def __init__(self, aid, abl):
        self.aid = aid  #계좌번호
        self.abl = abl  #계좌잔액
    def __iadd__(self, m):   #입금
        self.abl += m
        return self
    def __isub__(self, m):   #출금
        self.abl -= m
        return self
    def __str__(self):     #계좌상황을 문자열로 반환
        print('__call__')
        return '{0},{1}'.format(self.aid, self.abl)

def main():
    acnt = Account('James01', 100)      #계좌 개설
    acnt += 130      #130원 입금
    print(acnt)
    acnt -= 50       #50월 출금
    print(acnt)

main()