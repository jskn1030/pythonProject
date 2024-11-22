'''
라일명: Ex02-2-varoable-2.py

변수명 규칙
    - 특수문자 사용 불가
    - 첫 글자는 숫자 불가
    - 키워ㅏ드(명령어) 사용 불가

    주석 단축키 Ctrl + /
    줄 복사 단축기 Ctrl + d
    줄 삭제 단축기 Ctrl + y

'''

# 1. 여러 변수에 다른 값 할당
x, y, z = "피카츄", "라이유", "파이리"
print('포켓몬 1:', x)
print('포켓몬 2:', y)
print('포켓몬 3:', z)

# 2. 여러 변수에 같은 값 할당
x = y = z = '꼬부기'
print('변경된 포켓몬:', x)
print('변경된 포켓몬:', y)
print('변경된 포켓몬:', z)

# 잘못된 변수명 예시
'''
2myvar = 'Python1' # 숫자로 시작
my-var = 'Python2' # 특수문자 포함
my var = 'Python3' # 공백 포함
'''
my_var = 'Python4' # _ 가능
