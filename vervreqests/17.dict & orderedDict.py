# 17.dict & orderedDict.py
# 파이썬 3.7부터 순서를 보장해주기 시작했다.
# 원래는 순서가 없는 구조(집합)
d = {}
d['a']=1
d['b']=2
d['c']=3
print(d)

for kv in d.items():
    print(kv)

# 순서가 의미있는 정보일 때는 orderedDict을 써야한다. 기본 dict도 순서를 보장해주기는 하지만.
from collections import OrderedDict
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
print(od)
for kv in od.items():
    print(kv)


# orderedDict에서 순서는 의미정보이다.
d1 = dict(a=1, b=2, c=3)
d2 = dict(b=2, a=1, c=3)
print(d1==d2) #dict에서저장 순서는  중요치 않다. True

from collections import OrderedDict
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print(od1==od2) #OrderedDict는 변별요소이다. False

# orderedDict에서의 순서 바꾸기 함수
from collections import OrderedDict
od = OrderedDict(a=1, b=2, c=3)
for kv in od.items():
    print(kv, end=' ')
print()

od.move_to_end('b') #키가 b인 키와 값을 맨 뒤로 이동
for kv in od.items():
    print(kv, end=' ')
print()

od.move_to_end('b', last=False) #매개변수 last에 False를 전달하면 맨 앞으로 이동
for kv in od.items():
    print(kv, end=' ')