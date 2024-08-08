# 함수의 매개변수
# 기본적으로 필요한 만큼 선언할 수 있음

def sum_val(a, b):
    return a + b


def incr(a, step=1):    # 두번째 인수(step)은 기본 값이 있음
    return a + step


print(sum_val(2, 3))
print(incr(10)) #   두 번째 인수가 부여되지 않으면 기본값을 활용
print(incr(10, 2))  # 기본값 무시하고 값을 부여하면 그 값이 활용


# 키워드 인수
def area(width, height):
    return width * height


print(area(10, 20)) # 설계된 매개변수 순서대로 호출
print(area(width=10, height=20))    # 매개변수의 이름값으로 호출
print(area(height=20, width=10))    # 호출 순서는 중요하지 않음


# 가변 인수 : 정해지지 않은 수의 매개변수 -> 매개변수 앞에 *
def get_total(*args):   # args -> 정해지지 않은 개수의 매개변수
    total = 0
    for x in args:
        if isinstance(x, (int, float)):
            total += x
    return total


print(get_total(1, 3, 5, 7, 9))
print(get_total(1, 6, 3, 9, 21, 14, 93, 23))
print(get_total(1, 6, 3, 9, "A", 21, 14, 93, 23))


# 키워드 인수 : **
# 함수에 고정인수, 가변인수, 키워드 인수
# 선언부에 고정인수, 가변인수, 키워드 인수 순서로 선언

def func_args(a, b, *args, **kwargs):
    print("고정인수:", a, b)
    print("가변인수:", args, type(args))
    print("키워드인수:", kwargs)

func_args(10, 20, 30, 40, 50, 60, 70, option1="test", option2="kwargs")

print("-----------")

# 함수도 객체다 -> 함수의 인수로 전달될 수 있다
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def calculator(a, b, func): # func -> 함수
    if callable(func):  # 넘어온 매개변수가 실행 가능 객체인지 확인
        return func(a, b)


print(calculator(3, 7, plus))
print(calculator(3, 7, minus))



# 1회성으로 로직 전달하고자 할 때
# 익명 함수 lambda 함수를 전달해 줄 수 있다
def clean_strings(strings, *funcs):
    results = []
    for s in strings:
        for func in funcs:
            if callable(func):  # 넘어온 인자가 실행 가능 객체?
                s = func(s)
        results.append(s)

    return results

dirty_strings = "python pRoGramMing, jAVa pRoGRAMMING, LINUX, WinDoWs".split(", ")
print(dirty_strings)
cleaned = clean_strings(dirty_strings, str.strip, str.title)
print(cleaned)


# lambda : 익명 함수
# 익명 함수를 이용한 키함수 정의
strings = "Life is too short, you need Python".replace(",", "").lower().split()
print("strings:", strings)

# 문자열 길이 순으로 정렬
sorted_str = sorted(strings, key=lambda  x: len(x))
print(sorted_str)





