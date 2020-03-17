def define_str():
    """
    define_str() 문자열 정의 연습
    """
    # 문자열의 정의
    # 한 줄 문자열
    s1 = "Hello, Python" # "", '' 둘다 가능
    s2 = str("Hello, Python") # 객체 타입으로 생성
    s3 = str(3.14159) # 다른 타입을 문자열로 캐스팅
    print(s1, s2 ,s3)
    print(type(s1), type(s2), type(s3))

    # 인스턴스 체크
    print("s1은 str인가?", isinstance(s1, str))

    # 여러 줄 문자열 : """, '''
    s4 = """
    파이썬의 여러줄 문자열
    여러 줄 문자열은 다양한 용도로 사용되기도 한다
    """
    print(s4)

    # 여러 줄 문자열 활용 : 함수, 클래스 선언부 아래쪽에 입력하면 문서화할 때, 도움말 출력시 이 문자열을 출력한다.
    """
    파이썬은 기본적으로 여러 줄 주석을 허용하지 않아 
    여러 줄 문자열을 할당만 안하면 여러 주석으로 사용할 수 있다
    """

def string_oper():
    """
    문자열의 연산자 : str
    - 순차 자료형 : len, in, not in, 인덱싱, 슬라이싱, 연결(+), 반복(*)
    - 변경 불가 자료형(immutable)
    """
    s1 = "First String"
    s2 = "Second String"
    # 길이 : 시퀀스 자료형 len
    print("Len of s1:", len(s1))
    print("Len of s2:", len(s2))

    # 인덱싱 : 정인덱싱일 경우 시작은 0부터, 역인덱싱일 경우 시작은 -1부터
    # s1의 6, 7, 8번 인덱스
    print("6, 7, 8 of s1:", s1[6], s1[7], s1[8])
    print("6, 7, 8 of s1:", s1[-6], s1[-5], s1[-4]) # 역순으로 출력
    print("s1[6] == s1[-6]?", s1[6]==s1[-6])

    # str은 변경불가 이므로 내부 자료 변경 불가
    # s1[0] = 'f' -> ERROR

    # 슬라이싱 [시작경계 : 끝경계]
    s3 = s2[7:10] # 7번인덱스부터 9번까지
    print(s3)
    s4 = s2[-6:-3] # -6번인덱스부터 -4번까지
    print(s4)
    print(s3 == s4)
    # 시작 경계 생략 -> 처음부터, 끝 경계 생략 -> 끝까지
    print(s2[7:])
    print(s2[7:]==s2[7:len(s2)])
    print(s2[:6]==s2[0:6])
    # [시작경계 : 끝경계 : 간격값], 간격값이 음수일 시 방향이 역순
    print(s2[0:len(s2):2]==s2[::2]) # 0부터 끝까지 2간격
    print(s2[::-1])

    # 연결(+) -> 산술 연산이 아님
    print(s1 + s2)
    # 반복(*) : 순차형 * int
    print(s1*3) # s1을 세번반복
    print("Python"*3)

def transform_method():
    """
    변환 관리 메서드
    - lower, upper : 모두 소문자, 모두 대문자
    - swapcase : 대 <-> 소문자 전환
    - capitalize : 첫번째 글자를 대문자로 변경
    - title : 각 단어의 첫 글자를 대문자로, 나머지는 소문자
    """
    s = "i like python"
    print("SWAPCASE:", s.swapcase())
    print("CAPITALIZE:", s.capitalize())
    print("TITLE:", s.title())

def search_method():
    """
    검색 메서드 연습
    """
    s = "I Like Python, I Like Java Alse"
    print("COUNT:", s.count("Like")) # Like의 갯수

    # 문자열 찾기 : find, index 계열
    print("FIND:", s.find("Like")) # 처음부터 검색
    print("FIND AGAIN:", s.find("Like", 6)) # 6번 인덱스이후로 검색
    print("없는 문자열 FIND:", s.find("JS")) # -1 반환
    print("RFIND:", s.rfind("Like")) # 뒤에서 앞으로 검색
    print("INDEX:", s.index("Like")) # 정방향 검색
    print("INDEX AGAIN:", s.index("Like"), 6) # 검색 범위 제한
    # print("없는 문자열 INDEX", s.index("JS")) -> ERROR,
    # index는 없는 경우 에러가 발생하기 때문에 내부에 검색값이 있는 지 미리 확인하고 실행해야 함
    if "JS" in s :
        print("Safe Index:", s.index("JS"))
    else :
        print("JS는 존재하지 않는다.")

    # 역방향 검색 : rfind, rindex
    print("RFIND:", s.rfind("Like"))
    print("RFIND AGAIN:", s.find("Like", 0, 17))
    # rindex의 경우도 같은 방법, 오류가 발생할 수 있기 때문에 내부에 검색값이 있는지 먼저 확인하기

    # 특정 문자열로 시작 or 끝나는지 확인, startswith, endswith
    url = "http://naver.com"
    surl = "https://naver.com"
    ftp = "ftp://naver.com"
    print("STARTSWITH http?", url.startswith("http://"))
    print("STARTSWITH https?", surl.startswith("https://"))
    # 문자열이 여러 검색어 중 한개로 시작하는가?
    print(ftp, "STARTSWITH http or ftp?", ftp.startswith(('http://', "ftp://")))
    # url이 .com 으로 끝나는가?
    print(url, "ENDSWITH .com?", url.endswith(".com"))
    # startswith, endswith 도 시작범위, 끝범위를 잡을 수 있다
    # ftp 문자열 6번부터 11까지의 문자열이 na로 시작하는가?
    print(ftp, "(6, 11) STARTSWITH na?", ftp.startswith("na", 6, 11)) # 6~11 범위로 검색 제한

def modify_and_replace():
    """
    문자열 수정과 치환 관련 메서드
    """
    s = "       Alice And Heart Queen   "
    print("STRIP:", s.strip(), sep="") # 공백 제거
    print("LSTRIP: [", s.lstrip(), "]", sep="")
    print("RSTRIP: [", s.rstrip(), "]",  sep="")
    s2 = "------Alice And Heart Queen-----"
    print("STRIP -: [", s2.strip("-"), "]", sep="") # 제거할 조건 설정 가능

    # 치환 : s문자열을 strip, heart -> spade로 치환
    print(s.strip().replace("Heart", "Spade"))
    print("ORIGINAL s:", s) # 문자열은 불변형이기 때문에 원본이 고정

def align_methods():
    """
    문자열 정렬
    - 기본적으로 출력 자리수를 정해두고 내부에 문자열을 출력시 출력 방향을 지정(정렬)한다
    """
    s = "Alice And Heart Queen"
    print("CENTER:[", s.center(60), "]", sep="") # 60자리 확보, 중앙 정렬
    print("CENTER:[", s.center(60, "*"), "]", sep="") # 60자리 확보, 중앙 정렬, 공백은 *로 채움
    print("LJUST:[", s.ljust(60, "*"), "]", sep="") # 60자리 확보, 좌측 정렬, 공백은 *로 채움
    print("RJUST:[", s.rjust(60, "*"), "]", sep="") # 우측 정렬

    # zfill : 빈 공간을 0으로 채움
    print("ZFILL:", "1234".zfill(5))

def split_and_join():
    """
    나누기와 합치기
    """
    s = "Ham and Cheese and Breads and Ketchup"
    print("SPLIT", s.split()) # 공백문자 기준으로 분리
    ingr = s.split(" and ") # 특정 문자열을 기준으로 분리
    print("재료 목록:", ingr)
    # , 문자로 list의 각 요소를 join
    print("JOIN with ,:", ",".join(ingr))
    # split 시에 분리하고자 하는 요소의 개수 지정
    print(s.split(" and ", 2)) # 구분자를 기준으로 2개만 추출
    print(s.rsplit(" and ", 2)) # 구분자를 기준으로 오른쪽에서 2개 추출

    # 여러 줄 문자열이 있을 때 개행 문자를 기준으로 분리 : splitlines
    lines = """Java Programming
    Python Programming
    JavaScript Programming
    HTML/CSS Coding"""
    print("SPLIT:", lines.split()) # 공백문자를 기준으로 분리함
    print("SPLITLINES:", lines.splitlines()) # 개행을 기준으로 분리함
    # 개행 문자를 유지해야 하는 경우 splitlines(True), 기본값은 false 임
    print("SPLITLINES 개행 문자 유지:", lines.splitlines(True))

def check_methods():
    """
    is 계열 메서드 : 형태 판별
    반환값으로 bool(True, False)
    """
    print("1234".isdigit()) # "1234"가 숫자형태인가?
    print("abcd".isalpha()) # "abcd"가 알파벳 형태인가?
    print("Python3".isalnum()) # "Python3"가 알파벳과 숫자의 조합인가?
    print("Python 3".isalnum()) # 공백이 포함되어있기 때문에 false
    print(" \r\n\t".isspace()) # 공백문자 : 스페이스, 개행문자, 탭문자
    print("".isspace()) # 공백문자가 아닌 값이 없는 것
    # 알파벳 형태 판별
    print("PYTHON".isupper()) # 대문자인가?
    print("python".islower()) # 소문자인가?
    print("Python Programming".istitle()) # title 형태인가?

def str_format():
    """
    문자열 포맷 연습
    """
    # C-style의 포맷 : %s(문자열), %c(문자), %d(정수), %f(실수), %o(8진수), %x(16진수), %%(%literal)
    # -개의 -개 중에서 -개를 먹었다
    fmt = "%d개의 %s중에서 %d개를 먹었다."
    print(fmt % (10, "사과", 3))
    # 특정 서식 문자들은 옵션이 있을 수 있다 예) %f는 정수,실수의 자릿수를 지정해줄 수 있다.
    print("현재 이자율은 %f%%입니다." % 1.24)
    print("현재 이자율은 %.2f%%입니다." % 1.24) # 소수점 2자리까지

    # named formatting : 각 서식문자열에 이름 부여 가능, 순서는 중요하지 않고 이름이 부여된 서식에 연결할 데이터는 모두 존재해야함
    fmt = "%(total)d개의 %(fruit)s중에서 %(eat)d개를 먹었다."
    print(fmt % {"fruit" : "오렌지", "eat" : 5, "total" : 12})

    # place holder 방식 : {} -> 연결할 데이터 타입을 가리지 않는다
    fmt = "{}개의 {}중에서 {}개를 먹었다."
    # .format 메서드를 이용해서 데이터 바인딩 수행
    print(fmt.format(10, "사과", 3))

    # numbered placeholder 방식 : {번호}
    # named 혹인 numbered 방식은 하나의 데이터를 여러번 바인딩할 경우 유용하게 쓸 수 있다.
    fmt = "{0}개의 {2}중에서 {1}개를 먹었다."
    print(fmt.format(10, 3, "복숭아"))
    # named placeholder
    fmt = "{total}개의 {fruit}중에서 {eat}개를 먹었다."
    # 인자값을 이용한 데이터의 바인딩
    print(fmt.format(total=10, fruit="포도", eat=3))
    # 사전(dict)을 이용한 데이터의 바인딩 .format_map() 메서드
    dct = {
        "total" : 10,
        "fruit" : "수박",
        "eat" : 3
    }
    print(fmt.format_map(dct))

if __name__ == "__main__":
    #define_str()
    #string_oper()
    #transform_method()
    #search_method()
    #modify_and_replace()
    #align_methods()
    #split_and_join()
    #check_methods()
    str_format()