# 16.dict & defaultdict

# 0.기본적인 dict
d = {'red':3, 'white':2, 'blue':4}
d['red']=1
print(d)


# 1.1.파이썬에서 유명한 코드, 문자열을 이루는 각 알파벳 갯수 파악
s = 'robbot'
d = {}
for k in s:
    if k in d:
        d[k] += 1
    else :
        d[k] = 1
print(d)


# 1.2.setdefault 매서드를 쓴다고 했을 때
s = 'robbot'
d = {}
for k in s:
    d[k] = d.setdefault(k, 0) + 1   # d라는 객체의 k키값의 밸류를 정의한다. 없으면 0을, 있으면 해당 값을 반환한다.
print(d)


# 2.defaultdict : 예외적인 상황에서 미리 등록해 놓은 함수가 반환하는 디폴트 값을 그 키 값으로 저장한다.
from collections import defaultdict
s = 'robbot'
d = defaultdict(int)    #int함수를 등록하면서 defaultdict호출. int함수는 아무것도 지정하지 않으면 0을 반환한다. int() -> 0
for k in s:
    d[k] += 1   #d[임의의 값]->0을 받도록 약속되어 있다. d['r']이라는 요소는 없었으므로 d['r']=0이 지정되고 그 다음에 1이 더해지는 구조. 원래대로 라면 예외가 발생한다.
print(d)


# 2.1.내가 정의한 default함수를 defaultdict의 인자값으로 정의
def ret_zero():
    return 0

d = defaultdict(ret_zero)
print(d['a']) #원래대로면 예외가 발생하지만 d의 a요소가 생기고 0이 반환됨
print(d)

# 2.2.기본적인 dict
zis = {'a':0, 'b':1, 'c':2}
# print(zis['d']) <- 기본적인 dict라면 이렇게 예외처리가 된다.

# 2.3.lambda의 활용
d = defaultdict(lambda: 7)
print(d['z'])
print(d)



