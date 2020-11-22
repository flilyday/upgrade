# 34 __name__ & __main__
# __name__의 정체 : 파이썬 스크립트 파일을 실행하면, 자동으로 생성되는 __name__변수가 있다.
# 스크립트 파일을 정의할 때
# 1. 해당 스크립트 파일에서 기능을 쓰고 싶은 경우
# 2. 해당 스크립트 파일을 다른 본 파일에서 불러들여서 쓰려고 하는 경우 <
# if __name__ == '__main__'의 유용성 : 이걸 쓰면 해당 불러들여서 쓰려고 할 경우 __name__에는 해당 파일 이름이 바인딩 되기 때문에 해당 파일에 정의된 연산을 불필요하게 실행을 하지 않아도 된다.


# 1.임포트 할 who_you_are에서 if __name__ == '__main__'을 안 쓴 경우
# you_are_whom.py
# def main():
#     print('__name__ : {}'.format(__name__)) <- __name__에는 함수의 이름인 __main__이 매핑된다.
#
# main()

# 2. who_you_are.py에 __name__에 담긴 값이 __main__일 경우에만 실행되도록 한 경우
# def main():
#     print('__name__ : {}'.format(__name__))
#
# if __name__ == '__main__':
#     main()

# 위의 1, 2는 다른 파일에 정의해서 불러 들여야 한다.
# import who_you_are      # who_you_are를 임포트 하는 순간 who_you_are에 있는 main()함수도 같이 실행된다.
print('play_import')
print('__name__ : {}'.format(__name__))



