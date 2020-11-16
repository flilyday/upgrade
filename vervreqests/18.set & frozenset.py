# 18.set & frozenset.py
# 파이썬에서 제공하는 시퀀스 자료형
# 0.시퀀스 타입(저장 순서대로 저장된다. 넣을 때와 꺼낼 때의 순서 정보가 저장되어 있다.)
# 인덱싱 연산과 슬라이싱 연산 가능
# str : str클래스의 객체
# list : list클래스의 객체
# tuple : tuple클래스의 객체
# range : range클래스의 객체

#  1.매핑타입 : 순서가 보장되지 않는다.
# # 인덱싱 연산과 슬라이싱 연산 불가능
# dict

# 2.집합자료형
# 수학의 집합은 저장 순서를 유지하지 않는다.
# 수학의 집합은 중복된 값을 허용하지 않는다.
# set : mutable 객체
# frozenset : immutable객체

A= {'a', 'c', 'd', 'f'}
B= {'a', 'b', 'd', 'e'}
print(A-B)
print(A&B)
print(A|B)
print(A^B) #(A-B) U (B-A), 합집합에서 교집합 부분을 빼버린 것


A = set(['a', 'c', 'd', 'f'])
B = set('fdca') #문자열도 iterable객체이므로 이를 통해 set생성 가능
print(A)
print(B)
print(A==B)
print('a' in A)
print('b' in A)
for c in A & B :
    print(c, end=' ')


# 3.빈 딕셔너리와 빈 집합 생성
d = {}
print(type(d))

s = set()
print(type(s))


# 4.frozenset의 경우도 동일하게 위의 식이 적용된다.
A = frozenset(['a', 'c', 'd', 'f'])
B = frozenset(['a', 'b', 'd', 'e'])
print(A-B)
print(A|B)
print(A==B)
print('a' in A)
for c in A&B :
    print(c, end=' ')



t = [3, 3, 3, 7, 7, 'z', 'z']
t = list(set(t))    #set을 이용한 중복제거
print(t)


# 5.set과 frozenset의 차이
# set : mutable객체, 새로운 값의 추가 또는 삭제가 가능
# frozenset : immutable객체, 새로운 값의 추가 또는 삭제가 불가능

# add : 원소 추가하기
# discard : 원소 삭제하기
# update, |= : 다른 집합의 원소 전부 추가하기
# intersection_update, $= : 다른 집합과 공통으로 있는 원소만 남기기
# difference_update, -= : 다른 집합이 갖는 원소 모두 삭제하기
# symmetric_difference_update, ^= : 공통으로 갖지 않는 것들은 추가하고 나머지는 삭제하기

os = {1, 2, 3, 4, 5}
os.add(6)
os.discard(1)
print(os)

os.update({7, 8, 9})
print(os)

os &= {2, 4, 6, 8}
print(os)

os -= {2, 4}
print(os)

os ^= {1, 3, 6}
print(os)

# 6.set컴프리헨션
s1 = {x for x in range(1, 11)}
print(s1)

s2 = {x**2 for x in s1}
print(s2)

s3 = {x for x in s2 if x < 50}
print(s3)


