# 기본 자료형
def bool_ex():
    print("===== bool 자료형")
    # 참(True):1을제외한나머지, 거짓(False):1
    # bool() 논리값을 판정할 수 있다
    # 값이 비어있는 경우 False, 세팅되어있는 경우 True
    print(bool(0), bool(10)) # 0은 값이 비어있다고 판단
    print(bool(""), bool("Python")) # ""은 값이 비어있다고 판단
    print(bool([]), bool([1, 2, 3])) # 순차 자료형

def int_ex():
    print("===== 정수형 자료")
    # 리터럴, int()
    a = 23
    b = int(23)
    print(a, "is", type(a))
    print(isinstance(a, int)) # a가 int의 객체인지 확인
    # 10진수, 2진수, 8진수, 16진수
    b = 0b1101 # 2진수
    o = 0o23 # 8진수
    x = 0x23 # 16진수
    print(b, o, x)
    # python 3.x 에서는 long과 int를 구분하지 않고 int로 처리(int가 64비트 초과 데이터도 처리 가능)
    i = 2**2048
    print("bit int:", i)
    # 현재 가지고 있는 i의 비트 수
    print("i의 비트 수:", i.bit_length())
    # 진법 변환 함수 : bin, oct, hex -> 문자열로 반환
    y = 2019
    print("2019 -> 2진수:", bin(y))
    print("2019 -> 8진수:", oct(y))
    print("2019 -> 16진수:", hex(y))

def float_ex():
    print("===== 실수형 연습")
    # float, double은 구분하지 않고 float으로 처리
    f1 = 3.14159
    f2 = float(3.14159)
    print(f1, "is", type(f1))
    print("f2 is float?", isinstance(f2, float))
    f3 = 3.0
    print(f3, "is", type(f3))
    # 형태의 체크 is_integer() -> 정수 형태인가 (타입비교가 아닌 형태 비교)
    print(f2, "가 정수형태인가?", f2.is_integer())
    print(f3, "가 정수형태인가?", f3.is_integer()) # 소수점아래 값이 없기 때문에 true
    # 지수 표기법 (10의 n승, e 혹은 E 활용)
    c = 3e3 # 3의 10의 3승
    d = -2E-5 # -2의 10의 -5승
    print(c, d)
    print(type(c), type(d))
    print(-2e-5 == -0.00002)

def math_functions():
    print("===== 내장 수치 함수")
    # 기본적인 수치 함수는 별도 모듈 없이 사용 가능, 복잡한 수치 함수는 math 모듈 내부에 있다 import math
    print("절댓값:", abs(-10))
    print("나눈셈의 몫과 나머지:", divmod(5, 3)) # 5를 3으로 나눈 몫과 나머지
    print("제곱함수:", pow(2, 3))
    # 그 외의 해당 특정 수치값을 만들 수 있는 int, float, complex 등의 함수
    # 간단한 통계 함수 지원
    scores = [80, 90, 70, 60, 100] # list 자료형
    print("최저점수:", min(scores))
    print("최고점수:", max(scores))
    print("합계:", sum(scores))
    print("통계:", sum(scores)/len(scores))

def bit_oper():
    print("===== 비트 연산자")
    # 정수형 데이터를 비트 단위로 제어
    # bit NOT : ~ (1 <-> 0)
    print(bin(5), bin(~5))
    # bit shift << (비트를 왼쪽으로 이동), >> (비트를 오른쪽으로 이동)
    bits = 1
    print(bin(bits << 4)) # 왼쪽으로 4 이동
    # bit AND : &(둘다 참), OR : |(하나라도참)
    a = 0b10101010
    b = 0b11110000
    print("a AND b:", bin(a&b))
    print("a OR b:", bin(a|b))

if __name__ == "__main__":
    #bool_ex()
    #int_ex()
    #float_ex()
    #math_functions()
    bit_oper()