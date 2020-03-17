# dict 예제
def define_dict():
    """
    사전의 정의
    """
    # 기본적인 사전의 생성
    dct = dict() # 빈사전
    print(dct, type(dct))
    # literal 이용한 생성 {}
    dct = {"backetball":5, "baseball":9}
    # 키에 접근
    print(dct["baseball"]) # baseball 키에 연결된 값을 참조
    # print(dct["soccer"]) -> KEY ERROR, 없는 키값에 접근
    # 새 값을 넣을 경우 새로운 키값 설정
    dct["soccer"] = 11
    print("dct:", dct)

    # dict의 경우 순서가 없기 때문에 len, 포함여부만 확인 가능 -> 대상은 key 값
    print(dct, "length:", len(dct))
    print("soccer in dct?", "soccer" in dct)
    print("volleyball in dct?", "volleyball" not in dct)

    # dict은 복합자료형으로서 키의 목록과 값의 목록을 별도로 뽑아낼수 있음
    print("KEYS of dct:", dct.keys()) # keys() 매서드 사용
    print("TYPE of dct:", type(dct.keys()))
    print("VALUES of dct:", dct.values()) # values() 메서드 사용
    print("TYPES of dct:", type(dct.values()))

    # 값의 포함 여부를 판단하려면 .values() 메서드로 dict_values 추출 후 확인 가능
    # dct안에 9가 포함되어 있는가?
    print("9 in dct.values()?", 9 in dct.values())

    # 사전을 생성하는 다른 방법들
    # 키워드 인자를 이용한 사전의 생성
    d1 = dict(key1="value1", key2="value2", key3="value3")
    print("d1:", d1, type(d1))
    # 튜플의 리스트로 사전의 생성
    d2 = dict([("key1", 1), ("key2", 2), ("key3", 3)])
    print("d2:", d2, type(d2))
    # 키의 목록과 값의 목록이 이미 존재하는 경우 -> zip 객체로 묶어서 dict에 전달
    keys = ("one", "two", "three", "four")
    values = (1, 2, 3, 4)
    d3 = dict(zip(keys, values))
    print("d3:", d3, type(d3))
    # 사전의 키는 immutable 자료형이여야 한다
    # bool, 수치형, 문자열, 튜플 등 불변 자료형 가능
    d4 = {}
    d4[True] = "true"
    d4[10] = 10
    d4["eleven"] = 11
    d4[("홍길동", 23)] = "홍길동 23"
    # d4[["홍길동", 23]] = "홍길동 23" -> ERROR
    print("d4:", d4, type(d4))

def dict_methods():
    """
    사전의 메서드
    """
    dct = {"soccer": 11, "baseball": 9, "volleyball": 6}
    print("dct:", dct)
    # key의 목록 추출 : keys 메서드
    keys = dct.keys()
    print("keys of dct:", keys, type(keys))
    # dict_keys 는 순차자료형으로 변환할 수 있다
    keys_list = list(keys)
    print(keys_list)
    # value의 목록 추출 : values 메서드
    values = dct.values()
    print("values of dct:", values, type(values))
    # 키-값 쌍튜플의 목록 추출
    pairs = dct.items()
    print("key-value pair of dct:", pairs)
    # 비우기
    dct.clear()
    print("dct:", dct)

def using_dict():
    """
    사전 사용 연습
    """
    phones = {
        "홍길동": "010-1234-5678",
        "장길산": "010-2345-6789",
        "임꺽정": "010-3456-7890"
    }
    print(phones)

    # 새로운 키의 추가
    phones['일지매'] = "010-4567-8901"
    print(phones)

    # 키의 직접접근 vs get메서드
    if "고길동" in phones:
        print(phones['고길동']) # 키값의 직접접근은 키가 없는경우 에러발생
    else:
        print(phones.get('고길동')) # get메서드는 키값이 없는 경우 None 리턴
    # 없는 키값을 검색할 때 기본값을 리턴하고자 하는 경우 get메서드의 두번째 인자로 기본값을 부여할 수 있다
    print(phones.get("고길동", "미등록"))

    # 삭제 : del
    if "일지매" in phones:
        del phones['일지매']
    print(phones)

    # pop메서드 : 값을 가져오고 해당 객체를 삭제
    print(phones.pop('장길산'))
    print(phones)

    # popitem 메서드 : 키-밸류 쌍튜플을 반환하고 키를 삭제
    item = phones.popitem() # 가장마지막객체 반환
    print("Name:", item[0], item[1]) # 0번인덱스에는 키값, 1번인덱스에는 전화번호

def loop():
    """
    사전 객체의 조회
    """
    phones = {
        "홍길동": "010-1234-5678",
        "장길산": "010-2345-6789",
        "임꺽정": "010-3456-7890"
    }
    print(phones)

    # 기본적인 loop : keys() 목록을 대상으로 한다
    for key in phones:
        print(key, ":", phones[key])
    print()

    # 키와 값을 함께 loop : items 메서드는 키-값 쌍튜플의 목록
    for key, value in phones.items():
        print(key, ":", value)


if __name__ == "__main__":
    #define_dict()
    #dict_methods()
    #using_dict()
    loop()