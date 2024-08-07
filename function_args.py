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