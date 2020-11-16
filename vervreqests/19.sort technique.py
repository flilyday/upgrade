# 19.sort technique.py

# 1. 기본적으로 정렬을 제공한다.
ns = [3, 1, 4, 2]
ns.sort()   #기본 오름차순 정렬을 지원한다.
print(ns)

ns.sort(reverse=True)   #역순으로 정렬
print(ns)

# 2. 임의의 기준을 주고 싶을 때는 함수 객체를 전달하면 된다.
ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]  #(name, age)
def age(t):
    return t[1]     #정렬 기준을 함수 객체로 만들어 놓는다.(여기서는 튜플을 인자로 받아서 두번재 값을 반환하는 함수)
ns.sort(key=age)   #매개변수 key에 함수 age를 전달
print(ns)

ns.sort(key=age, reverse=True)   #매개변수 key에 함수 age를 전달
print(ns)

# Lambda를 이용한 정렬(A, B, c 이름을 기준으로 역순으로 정렬)
ns.sort(key = lambda t : t[0] , reverse=True)
print(ns)

#이름 길이순으로 정렬
names = ['Julia', 'Yoon', 'Steve']
names.sort(key=len)
print(names)

# 두 수의 합이 많은 순으로 정렬
nums = [(3, 1), (2, 9), (0, 5)]
nums.sort(key = lambda t : t[0]+t[1], reverse=True)
print(nums)


# 3.sorted함수 사용하기
# sort : list의 매소드
# sorted : 별도로 존재하는 함수

org = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
cpy = sorted(org, key= lambda t : t[1], reverse=True)
print(org)  #원본은 유지된다.
print(cpy)  #정렬된 사본이 생성되었다.

# 튜플은 .sort매서드 적용이 안된다(수정이 안되므로). 대신 sorted 함수를 통해 복사된 객체를 생성하고 리턴값으로 리스트 객체를 받을 수 있다.
org = (3, 1, 2)
cpy = sorted(org)
print(org)
print(cpy)
print(tuple(cpy))

# 각 문자열의 첫번째 숫자를 기준으로 정렬하기
org = ('321', '214', '197')

cpy = tuple(sorted(org, key=lambda t : int(t[0])))
print(cpy)