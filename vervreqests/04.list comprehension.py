# 04.list comprehension.py

# 0.일반적인 리스트 생성 방법
r1 = [1, 2, 3]
r2 = []
r3 = [1, 2, [3, 4]]

r4 = list('Hello')
r5 = list((5, 6 ,7))
r6 = list(range(0, 5))

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)

# 1. 일반적인 리스트 컴프리헨션 구문
r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1 :
    r2.append(i*2)
print(r2)
# 인위적인 방법처럼 느껴진다. 새로운 리스트를 생성해서 거기다 값을 채우는 것이.
# 그래서 나온게 리스트 컴프리헨션 : 빈 리스트를 생성하고, 연산을 거쳐 새로운 값을 넣는 것.

r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1] #값을 두배로 늘리는 리스트
print(r2)

r1 = [1, 2, 3, 4, 5]
r2 = [x+10 for x in r1] #값에 10을 더하는 리스트
print(r2)

# 2. 조건 필터 추가하기
# % 나누고 나머지를 반환하는 연산자
r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1:
    if i%2 :
        r2.append(i*2)
print(r2)

r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1 if x %2] #if절이 추가된 리스트 컴프리헨션
print(r2)

# 3. for가 한 번 더 들어가는 경우
r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = []
for t in r1 :
    for p in r2 :
        r3.append(t+p)
print(r3)

r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = [t+p for t in r1 for p in r2]
# r3 = [t+p | for t in r1 | for p in r2] t+p를 반환한다. for t in r1이 먼저 돌고, 그 밑에서 for p in r2가 돈다

r = [n*m for n in range (2, 10) for m in range (1, 10)]
print(r)

# 4. 이중 for루프에 조건 필터 추가
r = [n*m for n in range(2, 10) for m in range(1, 10) if (n*m) % 2 ]
print(r)

