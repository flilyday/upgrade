# 33.class method & static method.py
# 클래스 변수 : 클래스에 속한 변수

# 1.클래스 변수를 정의하고 접근하는 방식
class Simple:
    def __init__(self):
        self.ov = 10    # ov는 인스턴스 변수, 객체별로 존재하는 변수
ob1 = Simple()          # 인스턴스 변수는 객체를 통해 접근한다
print(ob1.ov)

print('-')

# 1.1.객체에서도 클래스 변수에 접근 가능
class Simple:
    cv = 11         # cv는 클래스 변수, 클래스 Simple에 속하는 변수
    def __init__(self):
        self.ov = 10

print(Simple.cv)    # 클래스 변수는 클래스 변수의 이름으로 접근

ob1 = Simple()
ob2 = Simple()
ob3 = Simple()

print(ob1.cv)       #클래스 변수는 객체를 통해서도 접근 가능
print(ob2.cv)
print(ob3.cv)

# 2.클래스가 생성될 때마다 클래스 변수의 카운트를 늘리는 변수
# 클래스를 통해서 객체를 몇 번 생성했나 알고 싶을 때
class Creation:

    count = 0

    def __init__(self):
        Creation.count += 1     # 생성될 때마다 count값 1씩 증가

    def get_cout(self):
        return Creation.count   # 클래스 변수 count값 반환

def main():
    c1 = Creation()
    print(c1.count)

    c2 = Creation()
    print(c1.count)

    c3 = Creation()
    print(c1.count)     #c1, c2, c3의 메서드를 호출해도 결과는 똑같다

main()

print('-')
# 3.static method
# static method : 클래스에 속한 메서드
# 위 2번의 예제는 번거롭다
# why? 1. 생성횟수를 알려면 일단 객체를 하나 생성해야 한다. 2. 객체를 생성할 때 count값이 1올라가므로 그 시점에서 get_count로부터 받은 값을 1빼야 한다.
# static 메서드의 유용성 : 객체를 할당받지 않아도 클래스 네임으로 바로 접근이 가능하다.

class Creation:
    def sm():   # staitc method는 첫번째 인자로 self를 주지 않는다.
        print('static mehtod!')

    sm = staticmethod(sm)   # sm메서드를 static매서드로 만드는 방법

def main():
    Creation.sm()   # static mehtod는 클래스 이름을 통해서 호출 가능
    c = Creation()
    c.sm()      # static메서드는 객체를 통해서도 호출 가능

main()

# 3.1.decorator를 이용한 static method만들기

class Creation:
    @staticmethod
    def sm():
        print('static mehtod!')

print('-')
# 4.생성한 객체 수를 반환하는 static method 만들기

class Creation:
    count = 0

    def __init__(self):
        Creation.count += 1

    @staticmethod   # 아래 메서드를 static 메서드로 만들기
    def get_count():
        return Creation.count


def main():
    print(Creation.get_count())     # 객체가 없는 상황에서도 메서드를 사용할 수 있다.
    c1 = Creation()
    print(Creation.get_count())
    c1 = Creation()
    print(Creation.get_count())

main()

print('-')
# 5. class 메서드
# class method : static method와 상당히 유사하다.

class Creation:
    num = 5     # 클래스 변수

    @staticmethod
    def sm(i):
        print('st~ 5 + {0} = {1}'.format(i, Creation.num + i))

    @classmethod
    def cm(cls, i):     # class method 에서는 첫번째 인자로 cls가 오고 파이썬에서 해당 class를 바인딩 해준다. 마치 매서드의 self 가 첫번째 인자로 오는 것과 마찬가지다.
        print('cl~ 5 + {0} = {1}'.format(i, Creation.num + i))

def main():
    Creation.sm(3)  # 클래스 이름 기반의 static method 호출
    Creation.cm(3)  # 클래스 이름 기반의 class method 호출
    c = Creation()
    c.sm(4)     # 객체를 대상으로 한 static method 호출
    c.cm(4)     # 객체를 대상으로 한 class method 호출

main()

print('-')

# 6.cls에 전달되는 것은 클래스이므로, 이를 기반으로 객체를 생성하는 것도 가능.
class Natural:
    def __init__(self, n):
        self.n = n

    def getn(self):
        return self.n

    @classmethod
    def add(cls, n1, n2):
        return cls(n1.getn() + n2.getn())

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural.add(n1, n2)    # 클래스 메서드를 가지고 객체를 만드는 예. 반환되는 객체를 n3에 저장
    print('{0} + {1} = {2}'.format(n1.getn(), n2.getn(), n3.getn()))

main()

print('-')

# 7.static method 보다 class method가 더 어울리는 경우
# 7.1.클래스 메서드를 통해 다음 날을 알려주는 클래스 함수 next_day() 만들기
class Date:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print('{0}, {1}, {2}'.format(self.y, self.m, self.d))
    @classmethod
    def next_day(cls, today):   #다음 날에 대한 객체 생성 및 반환
        return cls(today.y, today.m, today.d+1)

def main():
    d1 = Date(2020, 11, 22)
    d1.show()
    d2 = Date.next_day(d1)
    d2.show()
main()

print('-')


# 7.2.클래스 메서드를 통해 다음 날을 알려주는 클래스 함수 next_day() 만들기
class Date:

    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print('{0}, {1}, {2}'.format(self.y, self.m, self.d))

    @classmethod
    def next_day(cls, today):   #class method의 유용성 1 : 이 메서드는 Date 클래스의 객체이지만 next_day(Date, today)로 하지 않고 next_day(cls, today)로 정의했다.
        return cls(today.y, today.m, today.d+1)

class KDate(Date) :     # KDate은 Date클래스를 상속
    def show(self):     # show함수를 K시각으로 오버라이딩
        print('KOR : {0}, {1}, {2}'.format(self.y, self.m, self.d))

class JDate(Date):      # KDate은 Date클래스를 상속
    def show(self):     # show함수를 J시각으로 오버라이딩
        print('JPN : {0}, {1}, {2}'.format(self.y, self.m, self.d))

def main():
    kd1 = KDate(2020, 12, 24)
    kd1.show()
    kd2 = KDate.next_day(kd1)     # class method의 유용성2 : 정의부에서 class method로 정의했기 때문에 cls에 KDate이 바인딩 되어 값을 반환 할 수 있었다.
    kd2.show()

    jd1 = JDate(2020, 1, 1)
    jd1.show()
    jd2 = JDate.next_day(jd1)     # class method의 유용성3 : 정의부에서 class method로 정의했기 때문에 cls에 JDate이 바인딩 되어 값을 반환 할 수 있었다.
    jd2.show()

# class method 유용성 1, 2, 3을 종합 : 클래스에서 해당 클래스만 독점 사용하지 않고, 바인딩 될 수 있게 cls로 정의했기 때문에 Date클래스를 상속한 KDate과 JDate이 사용할 수 있었다.
# 이 기능은 static method로는 사용할 수 없다.

main()



