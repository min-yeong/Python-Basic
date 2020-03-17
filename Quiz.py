def quiz01_1():
    str = "Life is too short, You need Python"
    print("str의 길이", len(str))
    str = str.lower()
    str = str.replace(" ", "")
    str = str.replace(",", "")
    lst = str
    chars = list(set(lst))
    lst = sorted(list(chars))
    for item in lst:
        print(item, end=" ")
    print()
    print("lst의 길이:", len(lst))

def quiz01_2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice = lst[3:7]
    slice.reverse()
    lst[3:7] = slice[:]
    print(lst)

def quiz01_3():
    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]
    for key, value in students[0].items():
        print(key, ":", value)


def quiz01_4():
    lst_date = ['2018.01.02', '2018.01.03', '2018.01.04', '2018.01.05']
    lst_dow = ["화", "수", "목", "금"]
    lst_price = [2479.65, 2486.35, 2466.46, 2497.52]
    kospi_price = dict()
    kospi_price = dict(zip(lst_dow, lst_price))
    print(kospi_price[lst_dow])

if __name__ == "__main__":
    #quiz01_1()
    #quiz01_2()
    #quiz01_3()
    quiz01_4()