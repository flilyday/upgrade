# 31.nested function & closer.py

# 파이썬에서 함수도 객체다
# 함수의 이름은 해당 함수를 가리키는 변수다

# 1.nested function : 함수를 만들어서 반환하는 함수
def maker(m):
    def inner(n):
        return m*n
    return inner

f1 = maker(2)
f2 = maker(3)

print(f1(7))
print(f2(7))


# 2.closure : 모함수로부터 생성된 자식함수가, 모함수로부터 받은 변수의 값을 닫는 것
# 요 부분은 예전에 newlecture강의에서 본 기억을 내가 복기한거
# - 클로져 : 닫는 주체
# - 누가 닫느냐? 모 함수(네스티드 함수)로 부터 생성된 자식 함수
# - 무엇을 닫느냐? 모 함수로부터 받은 변수의 값
# - 왜 필요한가?(유용성) 원래 모 함수에 선언된 변수의 값은 그 함수를 빠져나오면(리턴으로 반환되면) 유효 범위가 사라지기 때문에 이 이론상으로는 자식 함수에서 모함수로부터 받은 변수의 값을 접근할 수 없는게 맞다.
# - 언제 닫히느냐? 자식함수에서 해당 변수를 참조하고 나서 더 이상 쓸모가 없어졌을 때

# 2.1. 자식함수에서 모함수로부터 받은 값은 자식함수의 객체에 저장되어 있다. 해당 값을 확인하는 예제
def maker(m):
    def inner(n):
        return m*n
    return inner

f1 = maker(2)
f2 = maker(3)

print(f1.__closure__[0].cell_contents)  # 모함수로부터 받은 변수 m값을 저장해 놓은 위치
print(f2.__closure__[0].cell_contents)
