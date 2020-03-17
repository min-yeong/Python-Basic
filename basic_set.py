# Set 연습
evens = {0, 2, 4, 6, 8} # 짝수 집합
odds = {1, 3, 5, 7, 9} # 홀수 집합
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # 전체 집합
mthree = {0, 3, 6, 9} # 3의 배수 집합

def define_set():
    """
    Set 정의 연습
    - 순서가 없고 중복 불허
    - 인덱싱, 슬라이싱 불가
    - len, 포함여부(in, not in) 정도만 사용 가능
    - 집합을 표현하는 자료형(집합 연산 가능)
    """
    # 리터럴 기호 {} -> set과 dict에서 둘다 사용하기 때문에 비어있는 set을 표현할 때는 리터럴기호 사용불가
    s = set() # 비어있는 Set 표현 방법
    print("s:", type(s))
    # 길이와 포함 여부(2가 각 집합에 포함되어 있는가)
    print(numbers, "의 길이:", len(numbers))
    print(2 in numbers, 2 in evens, 2 not in odds, 2 not in mthree)

    # Set 객체 함수를 이용해서 다른 순차 자료형을 Set으로 캐스팅할 수 있음
    s = "Python Programming"
    print(s, "length:", len(s))
    chars = set(s.upper())
    print(chars, "length:", len(chars))
    # 순서가 없고 중복이 제거됌 -> 리스트 등 자료형에서 중복을 제거할 때 사용
    lst = "Python Programming Java Programming R Programming".split()
    print(lst)
    lst = list(set(lst))
    print("중복제거:", lst)

def set_methods():
    """
    Set의 메서드
    """
    # 요소의 추가
    numbers.add(10)
    print(numbers)
    print("evens:", evens)
    evens.add(2)
    print("evens:", evens) # 중복된 값 추가 불가

    # 요소 삭제 : discard(요소를 삭제하되 존재하지 않는 값이여도 오류가 나지않는다), remove(요소를 삭제하되 존재하지 않는 값이면 오류발생)
    numbers.discard(15)
    print("numbers:", numbers)
    numbers.discard(5)
    print("numbers:", numbers)

    if 15 in numbers:
        numbers.remove(15)
    else:
        numbers.remove(4)
    print("remove:", numbers)

    evens.update({10, 12, 14, 16}) # 여러 요소가 한번에 업데이트
    print("evens:", evens)
    evens.clear() # Set 비우기
    print("evens:", evens)

def set_oper():
    """
    집합 연산
    - 합집합, 모집합, 부분집합, 교집합, 차집합
    """
    # 합집합 : |, union 메서드
    print("짝수 합집합 홀수:", evens.union(odds))
    print(evens.union(odds) == numbers)
    print(evens | odds == numbers)

    # 모집합, 부분집합의 판단 issuperset, issubset
    print(numbers.issuperset(evens), numbers.issuperset(odds))
    print(evens.issubset(numbers), odds.issubset(numbers))
    print(evens.issuperset(odds))

    # 교집합 : &, intersection 메서드
    print(evens.intersection(mthree) == {0, 6}) # 짝수와 3의 배수와 교집합
    print(odds & mthree == {3, 9})

    # 차집합 : -, difference 메서드
    print(numbers.difference(evens) == odds) # 전체수와 짝수의 차집합
    print(numbers - odds == evens) # 전체수와 홀수의 차집합

def loop():
    """
    Set의 순환
    """
    print("numbers:", numbers)
    # 순회
    for number in numbers:
        print(number, end=" ")
    print()

if __name__ == "__main__":
    #define_set()
    #set_methods()
    #set_oper()
    loop()