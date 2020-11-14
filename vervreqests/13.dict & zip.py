# 13.dict & zip.py

# 0.객체를 정의하는 다양한 방
print(type({}))     #빈 객체의 타입 출력해 보기

d = dict([('a',1),('b',2),('c',3)])
print(d)           #객체 생성의 새로운 방법 1

d = dict(zip(['a','b','c'],[1, 2, 3]))
print(d)            #객체 생성의 새로운 방법 2

d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(a=1, b=2, c=3)
d3 = dict([('a',1),('b',2),('c',3)])
d4 = dict(zip(['a','b','c'],[1, 2, 3]))

print(d1== d2 == d3 == d4)  #정의하는 방식에 상관없이 key와 value가 같으면 모두 동일한 객체.

# 1.파이썬 3.7부터 객체의 순서를 보장해준다(다른 언어에서는 보장하지 않음). 군만두 서비스와 같은 개념
d = {'a':1, 'b':2, 'c':3}
d['d']=4
for k in d:
    print(d[k], end=', ')
print()

# 2. zip함수 : iterable한 객체를 zip함수의 인자값으로 주면, 인자 각각에서 요소가 하나씩 나와 튜플로 반환됨
# 유용성 : 데이터를 구분해서 나눠야 할 때 유용하게 사용됨
# 2.1.리스트
z = zip(['a', 'b', 'c'], [1, 2, 3])
for i in z:
    print(i)

# 2.2.튜플
z = zip(('a', 'b', 'c'), (1, 2, 3))
for i in z:
    print(i)

# 2.3.문자열
z = zip('abc', (1, 2, 3))
for i in z:
    print(i)

# 2.4.zip과 리스트의 조합
d4 = dict(zip(['a','b','c'],[1, 2, 3]))

# 2.5.3개를 묶는 것도 가능
c = list(zip('abc',(1, 2, 3),['one','two','three']))
print(c)