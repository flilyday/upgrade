# 29._slots_ effect.py
# __dict__의 단점과 해결책
# 단점 : 객체의 값을 관리할 때 '키'를 이용해서 '값'을 얻게 하므로 리스트나 튜플보다 메모리 사용량이 많아진다.
# 그러므로 많은 수의 객체를 생성하려고 할 때는 메모리에 부담이 된다.
# 해결책 -> __slots__의 사용
# 0.일반적인 경우 : __dict__에 값이 할당
class Point3D :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.x, self.y, self.z)   #좌표 정보 출력

def main():
    p1 = Point3D(1, 1, 1)
    p2 = Point3D(24, 17, 31)
    print(p1)
    print(p2)
main()

print('-')

# 1. __slots__를 쓰는 경우
class Point3D :
    __slots__ = ('x', 'y', 'z')     #속성을 x, y, z로 제한한다.
                                    #이 클래스로 생성한 변수는 x, y, z로 제한한다.

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.x, self.y, self.z)

def main():
    p1 = Point3D(1, 1, 1)
    # p1.w = 30     #w는 slots에 명시하지 않은 이름이므로 오류 발생
main()

print('-')

# 2. __slots__를 썼을 때의 성능 향상 테스트
# 2.1.__dict__만 있을 때 내부적으로 일어나는 과정
class Point3D :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.x, self.y, self.z)   #좌표 정보 출력

def main():
    p = Point3D(24, 17, 31)
    print(p.x, p.y, p.z)
    print(p.__dict__['x'], p.__dict__['y'], p.__dict__['z'])    #내부적으로는 이렇게 __dict__의 값을 참조하여 출력하게 된다.
main()

print('-')
# 2.2.속도 테스트
# 2.2.1.slots를 안 쓸 경우 : 3.78초 정도
import timeit
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({0},{1},{2})'.format(self.x, self.y, self.z)

def main():
    start = timeit.default_timer()
    p = Point3D(1, 1, 1)

    for i in range(3000):
        for i in range(3000):
            p.x += 1
            p.y += 1
            p.z += 1
    print(p)

    stop = timeit.default_timer()
    print(stop - start)
main()

# 2.2.2.slots를 안 쓸 경우 : 3.78초 정도
import timeit
class Point3D:
    __slots__ = ('x', 'y', 'z')     #이 부분을 추가

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({0},{1},{2})'.format(self.x, self.y, self.z)

# 2.2.3.slots를 쓸 경우 : 2.98정도
def main():
    start = timeit.default_timer()
    p = Point3D(1, 1, 1)

    for i in range(3000):
        for i in range(3000):
            p.x += 1
            p.y += 1
            p.z += 1
    print(p)

    stop = timeit.default_timer()
    print(stop - start)

main()



