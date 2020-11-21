# 30.property.py

# 1.안전하게 접근하기 : getter와 setter
class Natural:  #자연수를 표현한 클래스. 1미만이 들어오면 1로, 아니면 해당 수로 저장
    def __init__(self, n):
        if(n < 1):
            self.__n = 1
        else :
            self.__n = n

    def getn(self): #getter의 정의
        return self.__n

    def setn(self, n):  #setter의 정의
        if (n < 1):
            self.__n = 1
        else :
            self.__n = n

def main():
    n = Natural(-3)
    print(n.getn())
    n.setn(2)
    print(n.getn())

main()
print('-')

# 2.안전하게 접근하기2 : 생성자에서 getter를 호출하여 중복코드 제거
class Natural:
    def __init__(self, n):
        self.setn(n)    #아래에 있는 setn 매서드 호출로 중복된 코드를 대신했다.

    def getn(self):
        return self.__n

    def setn(self, n):
        if n < 1 :
            self.__n = 1
        else :
            self.__n = n

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.setn(n2.getn()+n3.getn())    #식이 조금 많이 복잡해졌다.
    print(n1.getn())

main()

# 3. property의 유용성
# 식 한줄로 n = property(getn, set) getter(), setter() 메서드를 대신해 변수로의 접근이 가능해진다. n1.n , n2.n
class Natural:
    def __init__(self, n):
        self.__n = n

    def getn(self):
        return self.__n

    def setn(self, n):
        self.__n = n

    n = property(getn, setn)    #property의 설정.

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n  #식이 간결해짐. property를 쓴 효과 ->
                        #  = 등호를 기준으로 좌측은 setn이 호출, 우측은 getn이 호출된다.
                        # property가 없었을 때의 식 모양 -> n1.setn(n2.getn()+n3.getn())    #식이 조금 많이 복잡해졌다.
    print(n1.n)

main()

print('-')


#4.프로퍼티 등록의 원리
# 앞에서의 처리 n = property(getn, setn) <- property 객체 n을 생성하면서 getn과 setn을 등록했다.

# 4.1.getn과 setn을 각각 등록한 코드
class Natural:
    def __init__(self, n):
        self.setn(n)    # 아래에 있는 setn매서드 호출
    n = property()      # property 객체 생성
    def getn(self):
        return self.__n
    n = n.getter(getn)  # 위의 getn매서드를 게터로 등록

    def setn(self, n):
        if (n < 1):
            self.__n = 1
        else :
            self.__n = n
    n = n.setter(setn)  # 위의 setn매서드를 세터로 등록

print('-')

# 4.2.같은 이름 방식의 getter와 setter등록
class Natural:
    def __init__(self, n):
        self.__n = n  # 프로퍼티 n을 통해 접근

    n = property()  # property 객체 생성

    def pm(self):
        return self.__n
    n = n.getter(pm)    # 위의 pm을 getter로 등록. 등록했으니 pm이란 이름은 불필요

    def pm(self, n):
        if (n < 1):
            self.__n = 1
        else :
            self.__n = n
    n = n.setter(pm)    #위의 pm을 셋터로 등록

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n
    print(n1.n)

main()

# 5. 데코레이터 방식의 property등록
# 데코레이터 : 꾸며주는 것
# 데코레이터를 이용한 property 정의 방식이 많이 쓰인다.

class Natural:
    def __init__(self, n):
        self.__n = n

    @property   # 매서드 n을 게터로 지정하면서 property객체를 생성. 그리고 이렇게 생성된 property객체를 변수 n에 저장
    def n(self):
        return self.__n

    @n.setter   #이어서 등장하는 메서드를 n에 저장된 property객체로 저장한다. 그리고 이렇게 생성된 객체를 메서드 이름인 n으로 저장
    def n(self, n):
        if (n < 1):
            self.__n = 1
        else :
            self.__n = n

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n
    print(n1.n)


main()






