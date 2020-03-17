def define_list():
    # 리스트 연습
    """
    List
    - 순차자료형 :순서존재, 길이(leng), 포함여부 확인(in. not in), 인덱싱, 슬라이딩. 연결(+), 반복(*)
    - 가변자료형: 내부 자료 변경
    """
    lst1 = list()
    print(lst1, "Python")
    lst2 = [] # 리터럴 이용한 빈 리스트
    lst3 = [1, 2, "Python"] # 내부 요소들은 어떤 각체들 x
    print(lst3, type(lst3))

    # 다른 순차 자료형을 list() 객체 함수로 list 변경
    lst4 = list("Python Programming")
    print(lst4)

def list_oper():
    """리스트 연산자"""
    lst = [1, 2, "Python"]
    print(lst, "length:", len(lst)) # 길이 : len
    print("1이 list에 있는가?", 1 in lst) # 포함 여부 확인 : in, not in

    # 인덱싱 가능
    print("정인덱싱:", lst[0], lst[1], lst[2])
    print("역인덱싱:", lst[-3], lst[-2], lst[-1])

    # 슬라이싱
    print(lst[1:3]) # 항상 경계에 유의
    print(lst[1:]) # 끝 경계가 생략되면 끝까지
    print(lst[0:2])
    print(lst[:2])
    print(lst[:]) # 리스트 전체

    copy = lst[:] # 전체 리스트의 복제
    print("복제:", copy)
    print("copy is lst?", copy is lst) #

    # 연결과 반복은 새로운 리스트를 생성하여 원본은 유지된다
    print(copy + ["Java", True, 3.14159]) # 연결
    print(copy * 2) # 반복

    # append : 마지막에 새 요소를 추가한다
    print(copy)
    copy.append([3, 4])
    print("APPEND:", copy)
    # 내부에서 4를 찾아내기
    print(copy[3][1])
    del copy[3]
    # extend : 인자값을 부여된 리스트를 뒤에 연결하여 확장
    copy.extend([3, 4])
    print("EXTEND:", copy)

    # insert(i, x) : i 인덱스에 x를 추가
    copy.insert(2, [1,2,3]) # 2번 인덱스의 위치에 1,2,3을 추가
    print("INSERT:", copy)

    # 포함 여부 확인 : in, not in
    # copy 리스트 내에서 "Python" 요소가 있는지 확인
    print("포함 여부:", "Python" in copy)

    # 인덱스 확인
    # copy 리스트 내에 "Python" 문자열의 인덱스
    print("Index of Python:", copy.index("Python"))
    # 만약 찾고자 하는 요소가 내부에 없다면 ERROR(but 리스트에는 find 함수가 없음) -> 반드시 포함여부 확인
    if "Java" in copy :
        print("Index of Java:", copy.index("Java"))
    else :
        print("Java는 없습니다.")

    # 요소의 갯수 파악 : count
    # copy 리스트에서 1의 갯수
    print("Count of 1:", copy.count(1))

    # 요소의 삭제 : del(인덱스로 삭제), remove(요소값의 삭제)
    # 삭제할 객체가 내부에 없으면 ERROR -> 포함 여부 확인
    if 3 in copy:
        copy.remove(3)
        print("Remove 3 from copy", copy)
    else:
        print("삭제할 요소가 없습니다.")

    # 슬라이싱을 이용한 삽입과 치환, 삭제 -> 메서드를 이용하는 거보다 효율적
    lst2 = [1, 12, 123, 1234, 12345] # len == 5인 리스트
    print("lst2:", lst2)
    # 삽입 : 2번 인덱스 위치에 [10, 20] 추가
    lst2[2:2] = [10, 20]
    print("lst2:", lst2)
    # 삭제 : 범위를 잡고 해당 범위에 빈리스트[] 할당
    lst2[2:4] = []
    print("lst2:", lst2)
    # 치환 : 범위를 잡고 다른 리스트를 할당
    lst2[1:4] = [10, 20]
    print("lst2:", lst2)
    # 가장 마지막리스트에 삽입 (extend와 비슷)
    lst2[len(lst2):] = [30]
    print("lst2:", lst2)
    # 가장 앞리스트에 삽입
    lst2[:0] = [40]
    print("lst2:", lst2)

def list_method():
    """
    리스트의 메서드 : reverse, sort
    """
    # reverse : 리스트 요소의 순서 뒤집기
    lst = [80, 90, 85, 70, 60, 75, 100, 95]
    # 복제본
    copy = lst.copy()
    print("Reverse 이전:", copy)
    copy.reverse()
    print("Reverse 이후:", copy)

    # sort : 정렬 (sorted : 문법상 정렬 함수 -> 정렬 시도한 객체 내부를 변경하지 않음 ,
    #              sort : 객체 내부의 정렬 메서드 -> 객체 내부의 내용을 변경)
    # 그외의 sorted와 sort의 사용방법은 동일하다.
    print("Sorted 이전:", copy)
    print("Sorted 이후:", sorted(copy)) # 기본적으로 오름차순
    print("Sorted 수행이후:", copy) # 객체 내부 데이터 변경없음
    # copy 객체 내부의 sort 메서드를 수행
    copy.sort()
    print("Sort 수행 이후:", copy) # 기본적으로 오름차순, 객체 내부 데이터 변경

    # 역순 정렬 : sort, sorted에 reverse=True를 부여하면 역순 정렬
    copy = lst.copy()
    print("역순 정렬 이전:", copy)
    print("역순 정렬:", sorted(copy, reverse=True))

    # copy를 정수형이 아닌 str 기준으로 역순 정렬
    print("lst str 기준 역순 정렬", sorted(copy, key=str, reverse=True))
    # key 인자값에 두 값을 비교하는 함수를 부여하면 사용자 정의 정렬 기준 생성 가능
    lst = [19, 46, 37, 35, 91, 55, 64]
    # 각 요소값들을 10으로 나눈 나머지를 정렬 기준으로 설정
    # sort를 위한 key함수 선언
    def key_func(val):
        return val % 10
    lst2 = sorted(lst, key=key_func)
    print("Custom Sort", lst2)
    # 문자열을 기준으로 문자열의 길이를 대상으로 sort하는 key 함수
    def key_length(val):
        return len(val)
    words = "Life is too short you need Python".split()
    print("WORDS:", words)
    # 단어 길이의 역순으로 정렬 (가장 긴것부터 짧은 거 순)
    print("WORDS 길이의 역순:", sorted(words, key=key_length, reverse=True))

def loop():
    """
    리스트의 순회
    """
    words = "Life is too short you need Python".split()
    print("WORDS:", words)
    # 순차형 자료형은 for...in... 문으로 차례대로 요소를 반환받을 수 있음(별도의 인덱스 변수는 없다)
    for word in words:
        print("Words in words:", word)

def stack_ex():
    """
    리스트를 활용한 stack의 구현
    - append, pop 메서드를 이용
    """
    stack = []
    # input
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("STACK:", stack)
    # output : input 방향과 동일
    print(stack.pop())
    print(stack.pop(-1))
    print(stack.pop())
    if len(stack) > 0: # pop을 하기전에 비어있는지 먼저 확인
        print(stack.pop())
    else:
        print("스택이 비어있음")
    print("STACK:", stack)

def queue_ex():
    """
    리스트를 활용한 Queue의 구현
    - append, pop(0) 메서드 이용
    """
    queue = []
    # input
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("QUEUE:", queue)
    # output : 0번 인덱스부터
    while(len(queue)>0):
        print("Queue item:", queue.pop(0))
    print("QUEUE:", queue)

if __name__== "__main__":
    #define_list()
    #list_oper()
    #list_method()
    #loop()
    #stack_ex()
    queue_ex()