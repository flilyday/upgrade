# 20.enumerate.py

names = ['윤나은', '김현주', '이지선', '박선주']

# 정렬하고, 번호를 매겨서, 딕셔너리에 저장하려면?

# 문자열 비교의 대소
# 알파벳 순서상 뒤로 갈수록, 첫번재 문자가 같다면 두번째 문자를, 비교하는 문자들이 같다면 긴 문자열이, 소문자가 대문자보다 크다


# 1. 일반적인 방법
names.sort()
print(names)

dnames = {}
i = 1
for n in names :
    dnames[i] = n
    i += 1
print(dnames)

# 2.enumerate를 쓰는 방법
# enumerate는 iterator객체를 생성한다.
# 기능 : 넘버링(번호 매기는 기능)
# 유용성 : 컴프리헨션을 쓰려고 하는데 애매할 때 enuerate가 있으면 유용하게 쓸 수 있다.


names = ['윤나은', '김현주', '이지선', '박선주']
eo = enumerate(names)   #iterator객체인 enuerate객체 반환
for n in eo:    #eo에 담긴 것은 iterator객체이므로 for루프에 올 수 있음
    print(n)

names = ['윤나은', '김현주', '이지선', '박선주']
for n in enumerate(names, 10):  #번호를 10부터 매기기 시작
    print(n)

# 최종소스. 이렇게 편하게 만들 수 있다.
names = ['윤나은', '김현주', '이지선', '박선주']
dnames = {k : v for k, v in enumerate(sorted(names), 1)}
print(dnames)
