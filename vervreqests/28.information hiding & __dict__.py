# 28.information hiding & __dict__.py
# 정보은닉이란? 객체에 접근할 때 다이렉트로 '객체.변수' 형태로 접근하는게 아니라 지정한 매서드 방법으로만 접근하는 것. -> 간접접근
# 정보은닉의 장점은 기능이 아니라 객체의 안전성에 있다.

# 1.정보은닉의 유용성 : 기능X, 안전성 확보O
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return '{0} : {1}'.format(self.name, self.age)


def main():
    p = Person('James', 22)
    print(p)
    p.age -= 1  #나이가 한 살 더 먹어야는데, -1을 했다. 논리적 오류여서 프로그램적으로 찾아내기 힘듦. <- 객체의 변수에 직접 접근할 때의 위험성
    print(p)

main()

print('-')
# 2.은닉의 예
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def add_age(self, a):
        if a < 0:
            print("입력 오류")
        else:
            self.age += a

    def __str__(self):
        return '{0} : {1}'.format(self.name, self.age)


def main():
    p = Person('James', 22)
    p.add_age(1)
    print(p)

main()


# 3.파이썬에서 제공하는 객체 내부의 변수에 바로 접근하지 못하게 하는 방법
# 1. __변수
class Person:
    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def add_age(self, a):
        if a < 0:
            print("입력 오류")
        else:
            self.__age += a     #객체 내부에서는 __변수로 접근 가능하

    def __str__(self):
        return '{0} : {1}'.format(self.__name, self.__age)

def main():
    p = Person('Sora', 22)
    # p.__age += 1    #이게 금지가 된다. 오직 매서드를 통해서만 접근해야 한다.
    print(p)

main()

# 3.1. _변수 : 직접 접근하지 않는 대신 _언더바를 하나만 쓰기로 약속했다. 대신 언더바 하나만 쓰면 외부에서 객체 값 접근이 된다.
class Person:
    def __init__(self, n, a):
        self._name = n
        self._age = a

    def add_age(self, a):
        if a < 0:
            print("입력 오류")
        else:
            self._age += a     #객체 내부에서는 __변수로 접근 가능하

    def __str__(self):
        return '{0} : {1}'.format(self._name, self._age)

def main():
    p = Person('Sora', 22)
    # p._age += 1    ### 근데 이게 되버린다.
    print(p)

main()

# 4.__dict__
# 4.1.객체 내에는 해당 객체의 변수정보를 담고 있는 딕셔너리가 존재한다.
class Person:
    def __init__(self, n, a):
        self._name = n
        self._age = a

def main():
    p = Person('James', 10)
    print(p.__dict__)   #객체마다 하나씩 객체의 속성정보를 담고 있는 dict가 생성된다.
main()

# 4.2.변수를 추가했을 때 __dict__가 가지는 값도 변경된다.
class Person:
    def __init__(self, n, a):
        self._name = n
        self._age = a

def main():
    p = Person('James', 10)
    p.len = 178     #len이라는 변수를 객체에 추가
    p.adr = 'Kor'   #adr이라는 변수를 개체에 추가
    print(p.__dict__)   #객체마다 하나씩 객체의 속성정보를 담고 있는 dict가 생성된다.
main()

# 4.3.__dict__에 직접 접근해서 값을 변경
class Simple:
    def __init__(self, n, a):
        self._name = n
        self._age = a
    def __str__(self):
        return '{0}: {1}'.format(self._name, self._age)

def main():
    sp = Simple('my',10)
    print(sp)
    sp.__dict__['_name'] = 'Kerry' #__dict__에 접근해서 값을 변경
    sp.__dict__['_age'] += 10   #__dict__에 접근해서 값을 변경
    print(sp)   #__dict__변경 후 출력 결과

main()
print('-')

# 4.4. 파이썬에서 __로 정의했을 때 값 변경을 막는 방식
class Person:
    def __init__(self, n, a):
        self.__n = n
        self.__a = a

def main():
    p = Person('james', 10)
    print(p.__dict__)

main()

# __n이 _Person__n으로 바뀌어 저장된다.
# __AttrName -> _Person__AttrName




