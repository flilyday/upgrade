# 23.class & object.py

# 객체 안에 변수가 만들어지는 시점
# 클래스 : 객체를 만들기 위한 설계도
# 객체 : 클래스를 기반으로 만들어진 실제 사물

# 1.파이썬의 클래스와 객체에는 독특한 부분이 있다(파이썬의 유연함)

class Simple:
    #i = x  <--이런 식으로 클래스 변수에 대한 정의는 따로 하지 않았는데도 아래 메소드에서 바로 사용되고 있다.
    def seti(self, i):   #seti 메소드의 정의
        self.i = i

    def geti(self):  #geti 메소드의 정의
        return self.i

# 클래스의 기본 정의 : 클래스 내에 들어갈 변수(데이터)와 메소드(기능)을 정의하는 것
# 파이썬 클래스에서는 메소드만 정의하면 된다. 변수는 알아서 할당.



# 2.클래스 변수가 생성되는 시점
s1 = Simple()
s1.seti(200)    # 이 메소드의 실행 과정에서 객체 내에 변수 i가 만들어 진다.
print(s1.geti())

s2 = Simple()
#print(s2.geti())    #오류가 난다. seti로 값을 넘기지 않았으므로.



# 3. 설계도에 해당하는 클래스를 바탕으로 만들어진 객체에는 변수와 매소드를 모두 담는다.
class Simple:
    def __init__(self):
        self.i = 0      #초기 생성자에 아래 메서드에서 쓸 모든 변수를 만들어 줌으로써, 클래스&객체 표준을 일관성 있게 유지하고 위처럼 오류가 나지 않도록 한다.

    def seti(self, i):
        self.i = i

    def geti(self):
        return self.i

s = Simple()
print(s.geti())

s.seti(25)
print(s.geti())

# 4.객체에 변수와 메서드 붙였다 떼었다 해보기
class SoSimple:
    def geti(self):
        return self.i

# 4.1.객체에 변수 추가
ss = SoSimple()
ss.i = 27   #이 순간 변수 ss에 담긴 객체에 i라는 변수가 생긴다.
print(ss.geti())

# 4.2.객체에 메서드 추가
ss.hello = lambda : print('hi~')
ss.hello()

del ss.i        #지우는 것도 가능하다. 객체의 변수 삭제
del ss.hello    #지우는 것도 가능하다. 객체의 메서드 삭제
# print(ss.geti())  #지웠으므로 에러 발생
# ss.hello()        #지웠으므로 에러 발생


# 5.클래스에 변수 추가하기
class Simple:
    def __init__(self, i):
        self.i = i
    def geti(self):
        return self.i

Simple.n = 7    #Simple클래스에 변수 n을 추가하고 7로 초기화
print(Simple.n)
print('-'*30)
# 파이썬의 클래스는 클래스이자 객체이다.

s1 = Simple(3)
s2 = Simple(5)
print(s1.n, s1.geti(), sep = ', ')
print(s2.n, s2.geti(), sep = ', ') #규칙 : 여기서 n은 s1객체변수가 아니라 클래스 Simple의 변수다. 객체에 값이 없으면, 클래스로 가서 값을 찾아 가져온다.



# 6.파이썬에서는 클래스도 객체
print(type)     #type() 함수로 생각하고 function으로 나올 것 같은데 class로 나온다.
print(type([1, 2]))
print(type(list))   #list의 자료형을 물어보면 type의 객체로 나온다.

class Simple:
    pass

print(type(Simple)) #모든 클래스는 type이라는 클래스의 객체이다.

simple2 = Simple    #변수 simple2에 클래스 Simple을 담음
s1 = Simple()   #클래스 Simple객체로 생성
s2 = simple2()  #변수 simple2로도 객체 생성할 수 있음



