# Tuple
def define_tuple():
    """
    튜플의 정의
    - list와 비슷하나 immutable(변경불가)
    - (), tuple 객체 함수 이용
    - 요소값이 1개인 경우 , 를 찍어줘야함
    """
    tp = tuple()
    print(tp, type(tp))

    tp2 = () # 공튜플(literal)
    tp3 = (1,) # 항목이 1개면 반드시 콤마
    tp4 = (1, 2, 3)

def tuple_oper():
    """
    튜플의 연산자
    - len, 포함여부(in, not in)
    - 인덱스 접근, 슬라이싱 가능
    - immutable 자료형 -> 내부 자료 변경 불가
    - 반복(*), 연결(+)
    """
    tp = 1, 2, 3, 4, 5 # ()를 써주지 않아도 튜플로 인식
    print(tp, "LENGTH:", len(tp))
    print("3 in tp?", 3 in tp)
    print("tp 인덱스 접근:", tp[0], tp[1], tp[2], tp[-2], tp[-1])
    print("슬라이싱 tp:", tp[1:4], type(tp[1:4]))
    print("튜플 전체:", tp[:])
    print("tp 2번 반복:", tp * 2)
    print("연결 tp:", tp + (6, 7, 8))

def tuple_assignment():
    """
    튜플의 할당
    - 튜플을 활용하여 여러개의 변수를 동시 할당
    """
    x, y, z = 10, 20, 30
    print(x, y, z)
    # 튜플을 이용한 변수의 값 Swap(값 교체)
    x, y = 10, 20
    print("x={}, y={}".format(x, y))
    x, y = y, x
    print("x={}, y={}".format(x, y))

def tuple_methods():
    """
    튜플의 메서드
    """
    tp = (20, 30, 10, 20)
    # 특정 객체의 index
    print(tp.index(20)) # 20객체의 인덱스
    print(tp.index(20, 1)) # 인덱스 검색의 범위 제한

    # 요소의 갯수 확인
    print("COUNT:", tp.count(20)) # 내부의 20 객체의 갯수

def packing_unpacking():
    """
    튜플의 패킹과 언패킹
    """
    tp = 10, 20, 30, "Python" # ()사용하지 않아도 가능
    print(tp, type(tp))
    # 기본 unpacking : 튜플의 요소 개수만큼 변수를 부여, 부여된 변수는 요소의 갯수와 동일해야함
    a, b, c, d = tp
    print(a, b, c, d)
    #a, b, c = tp -> ERROR
    #a, b, c, d, e = tp -> ERROR

    # 확장 unpacking : 지정되지 않은 개수의 튜플을 할당 받을 변수의 이름 앞에 *
    a, *b = tp
    print("a:", a, type(a))
    print("b:", b, type(b))
    a, *b, c = tp
    print("a:", a, type(a))
    print("b:", b, type(b))
    print("c:", c, type(c))

def loop():
    """
    튜플의 순회
    """
    tp = (10, 20, 30, 40, 50)
    for item in tp:
        print(item, end=" ")
    print()

if __name__ == "__main__":
    #define_tuple()
    #tuple_oper()
    #tuple_assignment()
    #tuple_methods()
    #packing_unpacking()
    loop()