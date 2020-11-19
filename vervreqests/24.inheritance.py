# 24.inheritance.py

# 1.상속예제1 : 단일 상속
class Father:
    def run(self):
        print("so fast!!")


class Son(Father):  #Father를 상속하는 Son클래스
    def jump(self):
        print("so hight!!!")


def main():
    s = Son()
    s.run()
    s.jump()

main()


# 2.상속예제2 : 다중 클래스로부터의 상속
class Father:
    def run(self):
        print("so fast!!")

class Mother:
    def drive(self):
        print("so deep!!")

class Son(Father, Mother):
    def jump(self):
        print("so hight!")

def main():
    s = Son()
    s.run()
    s.drive()
    s.jump()

main()


# 3.매서드 오버라이딩(유용성 : 기능보강)
# 3.1.매서드 오버라이딩의 결과 : 부모로부터 물려받은 매서드와 똑같은 매서드가 자식 매서드에 있을 때 -> 자식 매서드 실행
class Father:
    def run(self):
        print("dad fast, dad style")

class Son(Father):
    def run(self):
        print("son fast, son style")


def main():
    s = Son()
    s.run()

main()
print()

# 3.2. 부모클래스의 매서드를 쉽게 불러와서 새로운 매서드로 만들 수 있다. -> 기능보강

class Father:
    def run(self):
        print("dad fast, dad style")

class Son(Father):
    def run(self):
        print("son fast, son style")
    def run2(self):
        super().run()   #부모 클래스의 run 호출 방법

def main():
    s = Son()
    s.run2()
    s.run()

main()


# 4.__init__매서드의 오버라이딩
# 부모 클래스 정의
class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f

    def drive(self):
        self.fuel -= 10

    def add_fuel(self, f):
        self.fuel += f

    def show_info(self):
        print('id:', self.id)
        print('fuel:', self.fuel)

def main():
    c = Car("63루8119", 0)
    c.add_fuel(100)
    c.drive()
    c.show_info()
main()

# 자식 클래스 정의
class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f) #Car의 __init__ 메서드 호출 <- 이 강의의 핵심. 자식클래스가 부모클래스의 변수를 사용하려면 반드시 부모클래스의 생성자를 초기화해줘야 한다.
        self.cargo = c

    def add_cargo(self, c):
        self.cargo ++ c

    def show_info(self):
        super().show_info()     #Car의 show_info() 매서드 호출
        print('cargo', self.cargo)

def main():
    t = Truck('42럭5959', 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()

main()






