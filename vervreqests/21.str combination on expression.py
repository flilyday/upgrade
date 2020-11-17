# 21.str combination on expression.py

# 0. 문자열 조합?
s = 'I am ' + str(7) + ' years old'     #문자열 조합
print(s)



# 1. 문자열 조합의 방법
# String formatting expressions : 표현식을 기반으로 문자열 조합  '__%s_%s__' %(value, value)
# String formatting method calls : '메소드 호출'을 통해 문자열 조합  '__{}_{}__'.format(value, value)

# 1.1.일반적인 방법
friends = [('jung', 22), ('Hong', 23), ('Park', 24)]
for f in friends :
    print('My friend', f[0], 'is', f[1], 'years old.')

# 1.2. 문자열을 조합한 방법
s = 'My name is %s' %'Yoon'     # %s의 위치에 문자열 'yoon'이 삽입됨
print(s)

# %s : 이 위치에다 문자열을 넣어라
# %d : 이 위치에다 정수를 넣어라
# %f : 이 위치에다 실수를 넣어라

s = 'My friend %s is %d years old and %fcm tall.' %('Jung', 22, 178.5)
print(s)

friends = [('jung', 22), ('Hong', 23), ('Park', 24)]
for f in friends:
    print('My friend %s is %d years old' %(f[0], f[1]))

# 1.3. 타입지시자에 맞게 넣어야 한다.
# print('%d' %'둘') #오류가 난다. 형변환이 불가능하므로.
print('My friend %s is %s years old and %scm tall.' %('Jung', 22, 178.5)) #정수, 실수 -> 문자열로 형변환이 이루어진다.

# 형 변환이 가능한 경우
# 정수, 실수 -> 문자열
# 정수 <-> 실수
# 실수 -> 정수로 갈 때 데이터 손실이 날 수 있다. 3.1 -> 3
print('%d' %3.14)   #0.14가 손실이 났다.



# 2. 딕셔너리로 출력 대상 지정하기
s = "%(name)s : %(age)d" % {'name' : 'Yoon', 'age': 22}
print(s)



# 3. 세밀한 문자열 조합 지정

print('height: %f' %178.5)  #기본 출력 형태

# 출력식의 형식 : %[flags][width][.precision]
# [flags] : -(왼쪽정렬), +(부호정보) , 0(빈 공간을 0으로 채우기)
# [width] : 폭, 출력할 너비 지정
# [.precision] : 정밀도, 소수 이하 자리

print('height : %f' %3.14)  #표현식 없이 출력
print('height : %.3f' %3.14)    #소수점 3자리까지 출력
print('height : %.2f' %3.14)    #소수점 2자리까지 출력

print('height : %7.2f' %3.14)    #7칸 확보하고 3.14 넣음
print('height : %10.2f' %3.14)   #10칸 확보하고 3.14 넣음

print('height : %07.2f' %3.14)   #빈 공간을 0으로 채워버린다.
print('height : %010.2f' %3.14)   #10칸 확보하고 3.14 넣음

# - 옵션을 추가했을 때
print('height : %-7.2f' %3.14)    #7칸 확보하고 3.14 넣음, -는 좌측 정렬의 의미
print('height : %-10.2f' %3.14)   #10칸 확보하고 3.14 넣음

# + 옵션을 추가했을 때
n = 3
print('num: %+d' %n) # +를 두면 부호가 함께 출력된다.

m = -1
print('num: %+d' %m) # +를 두면 부호가 함께 출력된다.


# 3.1.딕셔너리를 출력할 때도 적용된다.
print('%(h)s : %(v)-+10.3f입니다.' % {'h':'height', 'v':3.14})
# s : 해당 문자열, f : 해당 실수
# 10칸을 확보
# .3 소숫점 3째자리까지
# - 왼쪽 정렬
# + 부호 출력


