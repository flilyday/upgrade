# 26.special method.py
# iterable 클래스 디자인 해보기
# iterator 클래스 디자인 해보기


# 1.스페셜 메서드
# 스페셜 메서드 ? 약속된 메서드(무엇이 약속? 호출 시점이 약속됨)
# 형태 : __name__()
# 종류
# __init__
# __iter__
# __str__
# 번역이 된다 : len(객체) < - 호출은 이 형태로 하지만 사실은
# 객체.__len__() <-- 이렇게 파이썬 내부적으로 번역되어 호출이 된다.

t = (1, 2, 3)
print(len(t))   # t.__len__()

itr = iter(t)   # itr = t.__iter__()
for i in itr:
    print(i, end=' ')

s = str(t)  # s = t.__str__()
print(s)



# 2.스페셜 메서드 정의하기
class Car:
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return 'Vehicle number: ' + self.id

def main():
    c = Car('12러3456')
    print(len(c))
    print(str(c))

main()


# 3.iterable객체가 되게 하기
# iterable 객체 : iter함수에 인자로 전달 가능한 객체, 그 결과로 'iterator 객체' 반환.
# iterator 객체 : next함수에 인자로 전달 가능한 객체

class Car:
    def __init__(self, id):
        self.id = id
    def __iter__(self): #스페셜 메서드
        return iter(self.id)    #변수 id의 iterator객체를 반환

def main():
    c = Car("31러9876")
    for i in c: #Car객체가 iterable객체라는 증거
        print(i, end=' ')

main()


# 4.iterator객체가 되게 하기
class Coll:
    def __init__(self, d):
        self.ds = d
        self.cc = 0

    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1]

def main():
    co = Coll([1, 2, 3, 4, 5])
    while True:
        try :
            i = next(co)
            print(i, end = '')
        except StopIteration:
            break
main()

# 5.iterator객체이자 iterable객체가 되게 하기
# iterable객체를 인자로 전달하면서 iter함수를 호출하면 iterator객체가 반환된다.

class Coll2:
    def __init__(self, d):
        self.ds = d

    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc -1]

    def __iter__(self): # 이 메서드가 핵심
        self.cc = 0     # netx호출 횟수 초기화
        return self     # 이 객체를 그대로 반환함

def main():
    co = Coll2([1, 2, 3, 4, 5])
    for i in co :       # for루프 진행 과정에서 iter함수가 호출됨. next함수를 쓰기 위해서는 iter함수가 호출되어야 하는게 핵심
        print(i, end=' ')
    for i in co :
        print(i, end=' ')
main()

