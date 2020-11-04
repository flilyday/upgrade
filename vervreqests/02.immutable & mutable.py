# 02.immutable & mutable.py

# 수정 가능한 객체와 수정 불가능한 객체의 차이점

# 대표적인 수정 가능한 객체(mutable) : 리스트
# 대표적인 수정 불가능한 객체(immutable) : 튜플


# 1.변경가능한 객체 : 리스트의 예
r = [1, 2]
print(id(r)) #r의 주소 정보 확인

r += [3, 4]
print(r)
print(id(r)) #여전히 주소 정보가 동일하다. -> 리스트 객체는 수정이 가능하다.


# 2. 변경 불가능한 객체 : 튜플의 예
t = (1, 2)
print(id(t))

t+= (3, 4)
print(t)
print(id(t)) #객체를 수정 할 수 없으므로, 새로 객체가 생성되었다. 주소 정보가 바뀌었다. 위의 t는 rc가 0이 되었다.


# 3. 성격에 따라 달라지는 함수의 예
# 3.1. 리스트의 경우 생각한 것처럼 합쳐져서 나온다.
def add_last(m, n):
    m += n    #m에 n의 내용을 추가함. m이 어떤 객체냐에 따라 연산과정이 달라짐

r = [1, 2]
add_last(r, [3, 4])
print(r)

# 3.2. 튜플의 경우 생각지 않은 값이 나온다.
t = (1, 3)
add_last(t, (5, 7)) #(1, 3, 5, 7)로 나올 것처럼 생각된다.
print(t)  #튜플에 5와 7이 추가되지 않는다. (1, 3)

# 3.3. 그러면 튜플의 경우 생각한 것처럼 값을 받으려면 다음 식처럼 쓴다.
def add_tuple(t1, t2):
    t1 += t2
    return t1

tp = (1, 3)
tp = add_tuple(tp, (5, 7))
print(tp)


# 4. 리스트 정렬의 예
def min_max(d):
    d.sort()
    print(d[0], d[-1], sep=',')
d = [3, 1, 5, 4]
min_max(d)
print(d) #원본 객체가 바뀌어 버렸다. 의도하지 않은 상황

def min_max2(d):
    d = list(d) #복사해서 쓰면 원본과의 연결이 끊긴다.
    d.sort()
    print(d[0], d[-1], sep=',')
l = [3, 1, 5, 4]
min_max2(l)
print(l)    #원본이 그대로 출력된다.


# 5. 튜플 정렬의 예
def min_max3(d):
    d = list(d) #튜플에서도 min_max2처럼 잘 작동한다. 복사본에서는 리스트로의 형 변환이 한 번 이루어진다.
    d.sort()
    print(d[0], d[-1], sep=', ')
t = (2, 7, 5, 9, 0)
min_max3(t)
print(t)     #원본이 그대로 출력된다.












