# 22.str combination on method.py

# 0. 기본적인 사용 방법
# String formatting method calls : '메도스 호출'을 통해 문자열 조합하기
# '__{}_{}__'format(value, value) 스타일 문자열 조합

fs = '{0}...{1}...{2}'
ms = fs.format('Robot', 125, 'Box') #.format은 매소드이다.
print(ms)

print('{0}...{1}...{2}'.format('Robot', 125, 'Box'))
print('{2}...{1}...{0}'.format('Robot', 125, 'Box'))    #원하는 위치에 따라서 순서를 바꿀 수 있다.
print('{}...{}...{}'.format('Robot', 125, 'Box'))    #숫자를 안쓰면 순서에 따라 대입된다.
print('{toy}...{num}...{item}'.format(toy='Robot', num=125, item='Box'))    #문자로 지정할 수도 있다.


# 1. 언패킹을 고려하여 인자전달도 가능
my = ['Robot', 125, 'Box']
print('{}...{}...{}'.format(*my))
my = ['Box', (24, 31)]
print('{0[0]}..{0[1]}..{1[0]}..{1[1]}'.format(*my)) #인덱싱 연산을 더해서 다음과 같은 형태의 문자열 조합도 가능


# 2. 딕셔너리 기반의 인덱싱 연산도 가능
d = {'toy': 'Robot', 'price': 3500}
ds = 'toy = {0[toy]}, price = {0[price]}'.format(d)
print(ds)


# 3. 세밀한 문자열 구성 지정
# %[flag][width][.precision]f


print('{0}'.format(3.14))
print('{0:f}'.format(3.14))     #{0:f}이렇게 출력하면 정밀도가 기본 소수점 6짜리로 설정됨
print('{0:d}'.format(3))        #정수로 출력
print('{0:f}'.format(3.14))     #실수로 출력

print('%f' %3.14)
print('{0:f}'.format(3.14))

# 비교
print('%.4f' %3.14)     #%뒤에 4
print('{0:.4f}'.format(3.14))   #:뒤에 4

print('%9.4f' %3.14)     #%뒤에 .앞에 9 : 빈칸 채우기
print('{0:9.4f}'.format(3.14))   #:뒤에 .앞에 9 : 빈칸 채우기

print('{0:<10.4f}'.format(3.14))    #왼쪽으로 붙임
print('{0:>10.4f}'.format(3.14))    #오른쪽으로 붙임
print('{0:^10.4f}'.format(3.14))    #가운데로 붙임


print('%+d, %+d' %(5, -5))          #부호 출력
print('{0:+d}, {1:+d}'.format(5, -5))
print('{0:+}, {1:+}'.format(5, -5)) #d생략가능
print('{:+}, {:+}'.format(5, -5))   #0,1도 생략가능


print('{0:*^10.4f}'.format(3.14))   #^중앙정렬. *별로 채움
print('{0:+<10}'.format(7))         #<좌측정렬. +플러스로 채움
print('{0:^^10}'.format('hi'))      #^중앙정렬. ^꺽쇠로 채움

