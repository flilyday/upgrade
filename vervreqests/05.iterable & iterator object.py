# 05.iterable & iterator object.py

# 0.일반적인 반복 방법
ds = [1, 2, 3, 4]
for i in ds:
    print(i, end = ' ')
print()

# 1. iter()함수를 이용해 Iter객체를 생성하기. 원할 때 하나씩 값을 꺼내 쓸 수 있다.
ds = [1, 2, 3, 4]
ir = iter(ds) #iterator 객체를 얻는 방법 : iter()함수를 호출한다.

print(next(ir)) #다음 값을 반환해라 : next(ir)
print(next(ir))
print(next(ir))
print(next(ir))
# print(next(ir)) #다 꺼냈는데 또 호출하면 StopIteration이라는 예외를 발생시킨다. 필요에 의해서 예외를 발생시키고 있다.

# 2. 정의 : iterable 객체를 대상으로 iter함수를 호출해서 iterator 객체를 만든다.
# Iterable 객체 : iter함수에 인자로 전달 가능한 객체
# Iterator 객체 : iter함수가 생성해서 반환하는 객체

# 3. Special Method : 파이썬에서 처리해주는 특별한 함수
ds = [1, 2, 3]
ir = iter(ds)
print(next(ir))
print(next(ir))

# iter(), next()를 쓰지만, 실제로 파이썬에서는 아래와 같이 처리를 한다.
# ds = [1, 2, 3]
# ir = ds.__iter.__() #iter함수의 실제 모습 : 리스트의 __iter__메소드 호출을 통해서 iterator 객체를 얻게 된다.
# print(ir.__next__()) #next함수의 실제 모습 : ir객체의 __next__메소드 호출을 한다.
# print(ir.__next__())

# 4.Iterable 객체의 종류와 확인 방법
# Iterable한 객체의 종류 : 리스트, 튜플, 문자열
r = [1, 2, 3, 4, 5]
td = ('one', 'two', 'threee')
s = 'iteration'

# 확인방법
print(dir([1, 2])) # dir함수에 넣고 돌렸을 때 __iter__메소드가 존재하면 Iterable한 객체이다.
print(hasattr([1, 2], '__iter__')) # hasattr함수에 넣으면 T,F반환

# for루프와 Iterable 객체
for i in [1, 2, 3]:
    print(i, end = ' ') # for문은 내부적으로 아래와 같이 처리된다.

ir = iter([1, 2, 3])
while True :
    try :
        i = next(ir)
        print(i, end = ' ')
    except StopIteration:
        break


# 모든 iterator는 iterable한 객체이기도 하다.
ir = iter([1, 2, 3]) #ir에 저장되는 것은 iterator객체
for i in ir:    #for루프에 iterator객체를 가져다 두었다.
    print(i, end=' ')

ir1 = iter([1, 2, 3])
ir2 = iter(ir1)
print(ir1 is ir2) #ir1과 ir2가 참조하는 객체는 같은 객체이다.
print(id(ir1))
print(id(ir2))




