# 14.dict looping & comprehension.py

# 0.일반적인 방법
d = dict(a=1, b=2, c=3)
for k in d:
    print(d[k])

# d.keys() : 키를 호출
# d.values() : 값을 호출
# d.items() : 키,값 모두 호출

# 0.1. 키만 필요할 때
d = dict(a=1, b=2, c=3)
for k in d.keys():
    print(k)

# 0.2. 값만 필요할 때
d = dict(a=1, b=2, c=3)
for k in d.values():
    print(k)
# 0.3. 모두 필요할 때
d = dict(a=1, b=2, c=3)
for k in d.items():
    print(k)

d = dict(a=1, b=2, c=3)
for k, v in d.items():
    print(k, v, sep=', ')


# 1. dict 컴프리헨션
# 1.0.dict컴프리헨션
d1 = dict(a=1, b=2, c=3)
d2 = {k: 2*v for k, v in d1.items()}
d3 = {k: 2*v for k, v in d2.items()}

print(d1)
print(d2)
print(d3)

# 1.1.if절이 포함된 컴프리헨션
d1 = dict(a=1, b=2, c=3, d=4)
d2 = {k: v for k, v in d1.items() if v%2}
print(d2)

# 1.2.zip을 포함한 딕셔너리
ks = ['a', 'b', 'c', 'd']
vs = [1, 2, 3, 4]

d = {k:v for k, v in zip(ks, vs)}
print(d)

# 1.2.zip을 포함한 딕셔너리 + if절
ks = ['a', 'b', 'c', 'd']
vs = [1, 2, 3, 4]

d = {k: v for k, v in zip(ks, vs) if v%2}
print(d)