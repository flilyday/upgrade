# 12.named tuple.py

tri_one = (12, 15)  #삼각형의 밑변12와 높이 15를 묶어 놨다고 가정했을 때

from collections import namedtuple
Tri = namedtuple('Triangle', ['bottom', 'height'])  #네임드 튜플 클래스를 만든다.
t = Tri(3, 7)   # 네임드 튜플 객체 생성
print(t[0], t[1])
print(t.bottom, t.height)   #네임드 튜플의 장점. 값의 의미를 알 수 있다.
# t[0] = 15   #튜플과 마찬가지로 값을 수정할 수 없다.

Tri = namedtuple('Tri', ['bottom', 'height'])  #객체 생성은 클래스 이름이 아니라 할당 받은 변수로 하므로 이렇게 일치시키는 코드를 많이 쓰기도 한다.

Tri = namedtuple('Tri', 'bottom height')    #이런 식의 값 쓰는 것도 가능하다.

# 튜플과 마찬가지로 언패킹도 가능하다.
def show (n1, n2):
    print(n1, n2)
t = Tri(3, 8)
show(*t)