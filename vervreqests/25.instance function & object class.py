# 25.instance function & object class.py

# isinstance(object, classinfo)  <- 객체의 클래스 유형을 확인하는 함수. 좌ojbect가 우class인지 확인

# 1. 객체가 해당 클래스인지 확인
class Simple:
    pass

s = Simple()
print(isinstance(s, Simple))   #s가 Simple클래스의 객체인가?
print(isinstance([1, 2], list))    #[1, 2]가 list클래스의 객체인가?


# 2. 객체가 해당 클래스인지 확인2 : 상속관계에 있어서의 내용
class Fruit:
    pass

class Apple(Fruit):
    pass

class SuperApple(Apple):
    pass

sa = SuperApple()
print(isinstance(sa, SuperApple))
print(isinstance(sa, Apple))
print(isinstance(sa, Fruit))    #해당 클래스의 객체이거나, 클래스를 상속하는 클래스의 객체일 때 True

# 3.object 클래스
# 파이썬의 모든 클래스는 object클래스를 직접 혹은 간접 상속한다.
# object클래스 : 파이썬이 기본 제공하는 클래스

class Simple:
    pass

print(isinstance(Simple(), object)) # Simple클래스 객체가 object클래스를 상속하는가?
print(isinstance([1, 2], object)) # 리스트는 object클래스를 상속하는가?


# 4.클래스에서의 상속관계 : issubclass함수를 사용.
class A:
    pass

class Z(A):
    pass

print(issubclass(Z, A)) #Z는 A를 상속하는가?
print(issubclass(type, object)) #type클래스는 object클래스를 상속하는가?


# 4.1.object클래스의 명세 확인
for i in dir(object):
    print(i)

# __init__생성자 함수가 들어 있다. 새로운 클래스를 정의할 때는 __init__ 메서드를 그냥 정의하는 것이 아닌 오버라이딩 하게 되는 것


