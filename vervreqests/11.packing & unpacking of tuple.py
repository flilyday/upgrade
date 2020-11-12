# 11.packing & unpacking of tuple.py
# packing :  묶기
# unpacking : 풀기
# 별기호 * : 묶는다는 의미로 사용된다. 풀기의 의미로도 사용되기도 한다.(함수 인자 전달 할 때만)

# 0.튜플 패킹
tri_one = (12, 15)
print(tri_one)

tri_two = 23, 12    #값은 두개인데 변수는 하나 -> 자동으로 튜플로 저장된다.
print(tri_two)

# 1.1.튜플 언 패킹 : 저장된 값을 꺼내는 행위. 이 때는 변수의 갯수가 일치해야 한다.
tri_three = (12, 25)
bt, ht = tri_three
print(bt, ht)


# 1.2.튜플 언패킹2 : 둘 이상의 값을 리스트로 묶어서 하나의 변수에 저장하는 것도 가능하다.
# *others는 앞, 중간, 뒤 모두 오는 것이 가능하다.

nums = (1, 2, 3, 4, 5)
n1, n2, *others = nums  #둘 이상의 값을 리스트로 묶을 때 *를 사용한다.
print(n1)
print(n2)
print(others)   #나머지는 리스트로 묶이게 된다.

nums = (1, 2, 3, 4, 5)
first, *others, last = nums
print(first)
print(others)
print(last)

nums = (1, 2, 3, 4, 5)
*others, n1, n2 = nums
print(others)
print(n1)
print(n2)

# 리스트의 경우도 튜플과 동일하다
nums = [1, 2, 3, 4, 5]
n1, n2, *others = nums
print(n1)
print(n2)
print(others)

# 2.함수 호출 및 반환 과정에서의 패킹과 언패킹
def ret_nums():
    return  1, 2, 3, 4, 5   #튜플의 소괄호가 생략된 형태이다. 패킹되어 반환됨
nums = ret_nums()
print(nums)

n, *others = ret_nums()     #반환되는 값이 언패킹 되어 변수들에 저장된다.
print(n)
print(others)      #나머지 값은 역시 리스트로 저장된다는 것에 유의

# 묶는다는 의미 : (함수를 정의할 때) 세번째 이후 인자값들이 모두 묶여서 한꺼번에 전달되는 상황
def show_nums(n1, n2, *other):     #세 번째 이후 값들은 튜플로 묶여  other에 전달 <
    print(n1, n2, other, sep=', ')
show_nums(1, 2, 3, 4)
show_nums(1, 2, 3, 4, 5)

# 전달되는 모든 값들을 하나의 튜플로 묶어서 nums에 저장
def nums(*sum):
    s = 0
    for i in sum:
        s += i
    return s

print(nums(1, 2, 3))
print(nums(1, 2, 3, 4))
print(nums(1, 2, 3, 4, 5))

# 푼는다는 의미 : (함수를 호출 할 때)
def show_man(name, age, height):
    print(name, age, height, sep=', ')
p = ('Yoon', 22, 180)
show_man(*p)    #p에 담긴 값을 풀어서 각각의 매개변수에 전달

p = ['Park', 21, 177]
show_man(*p)

# 튜플을 꺼내고 싶을 때 : 동일한 구조로 맞추면 된다.
t = 1, 2, (3, 4)
a, b, (c, d) = t    #튜플 안 값의 구조와 동일한 형태로 변수를 선언한다
print(a, b, c, d, sep=', ')

p = 'hong', (32, 178), '010-1234-5678', 'Korea'
na, (age, height), ph, ad = p
print(na, ad)

# 원하는 값이 정해져 있을 때, 불필요하게 값을 할당하지 않아도 된다.
na, (_, _), _, ad = p
print(na, ad)

# 3.for loop에서의 언패킹
ps = [('Lee', 172), ('Kim', 173), ('Choi', 174)]    #리스트에 담긴 튜플
for n, h in ps:
    print(n, h, sep=', ')

ps = (['Lee', 172], ['Kim', 173], ['Choi', 174])    #튜플에 담긴 리스트
for n, h in ps:
    print(n, h, sep=', ')


