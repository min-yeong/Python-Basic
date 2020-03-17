# .py 파일 한 개는 하나의 모듈, 파일명 자체가 모델의 이름이므로 파일명을 정할 때도 변수 명명 규칙 위반 금지
# 들여쓰기로 블록을판단하므로 들어쓰기에 유의
# 함수 작성 키워드 : def

# 연산자
def arith_oper():
    # 블록은 시작되었지만 구현부가 없을 경우
    #pass
    print("===== 산술연산")
    # +, -, * , /
    print(7 / 5) # 정수와 정수의 나눗셈이지만 소숫점까지 출력
    print(7 // 5) # 정수만 출력
    print(7 % 5) # 나머지 출력
    print(divmod(7, 5)) # 나눗셈의 몫과 나머지 구하는 함수
    print("7/5의 몫:", divmod(7, 5)[0])
    print("7/5의 나머지:", divmod(7, 5)[1])
    print("7의 3승:", 7**3) # 제곱
    print("7의 3승:", pow(7, 3))

def complex_ex():
    print("===== 복소수")
    # 형태 : 실수부 + 허수부
    print(3+4j) # 실수부:3, 허수부:4 인 복소수 -> 하나의 데이터 타입
    print(3+4j.real) # 실수부
    print(3+4j.imag) # 허수부
    print(3+4j.conjugate()) # 켤레복소수
    print(complex(3, 4)) # complex 객체 타입을 이용해 생성한 복소수

def rel_oper():
    print("====== 비교연산, 관계연산")
    # == 같다, != 같지않다, >, >=, <, <=
    # 관계연산을 대소비교 -> boolean
    a = 6
    # a가 0보다 크고 10보다 작다
    print(0 < a and a < 10) # 복합관계식이 가능하다
    print(0 < a < 10)
    # 수치데이터 이외의 대소 비교
    print("문자열의 대소:", "abcd" > "abce") # 문자열의 경우 앞에서부터 차례로 비교
    print("순차형의 대소:", (1, 2, 3) < (1, 2, 4)) # 앞에서부터 차례로 비교
    # 동질성의 비교 ==, 동일성의 비교 is
    a = 10; b = 20; c = a;
    print("a==b?", a==b)
    print("a==c?", a==c)
    print("a is c?", a is c)

def variable_ex():
    print("===== 변수")
    # 파이썬의 변수는 선언 작업이 없고 최초 할당과 동시에 변수가 선언됨, 동적 인터렉티브 언어이기 때문에 타입지정되지않음
    # 변수명은 문자, 숫자, _의 조합 (숫자로 시작 불가능, 예약어불가능)
    # 예약어 확인
    import keyword
    print(keyword.kwlist) # 예약어 목록
    print("예약어의 갯수:", len(keyword.kwlist))
    # 변수의 치환
    c, d = 3.5, 5.3 # 변수의 갯수와 값의 갯수는 일치해야함
    print(c, d)
    c, d = d, c # 변수의 치환 가능
    print(c, d)
    # 같은 값을 여러 변수에 동시 할당
    x = y = z = 10
    print(x, y, z)
    # 동적 타이핑 언어 : 할당될때 타입 결정
    a = 10
    print(a, "is", type(a)) # a의 타입 확인
    # 다른 타입의 객체도 할당 가능
    a = "Python"
    print(a, "is", type(a))
    # 변수가 가리키는 객체가 특정 타입인지 확인 : isinstance 함수
    print("a는 str객체인가?", isinstance(a, str))
    # 변수가 가리키는 객체의 타입을 비교할 때, 여러 개의 타입 중 하나인지 확인
    n = 3.14
    print("n은 int 혹은 float인가?", isinstance(n, (int, float)))

if __name__== "__main__":
    #arith_oper()
    #complex_ex()
    #rel_oper()
    variable_ex()