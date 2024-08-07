# 글로벌 변수 선언
global_a = 1
global_b = "Global"


# 사용자 정의 함수
def func():
    local_a = 2
    local_b = "Local"
    print(locals())  # 로컬 심볼 테이블 확인


# 사용자 클래스
class MyClass:
    x = 10
    y = 20


def symbol_table():
    """
    전역 심볼 테이블, 지역 심볼 테이블 확인
    """
    print(globals())
    print(type(globals()))

    print("global_a:", globals().get("global_a"))
    print("global_b:", globals().get("global_b"))

    func()

    # 내부의 __dict__를 확인하면 해당 객체 내부의 심볼 테이블 확인할 수 있음
    # 런타임에 속성, 메서드를 추가할 때
    func.dynamic = "Dynamic"
    print(func.__dict__)

    # 인스턴스 객채
    o = MyClass()
    o.dynamic = "Dynamic"
    print(o.__dict__)


import sys


def ref_count():
    """
    객체가 참조될 때 참조 카운트가 증가되면서 관리
    더이상 참조되는 것이 없을때 -> Garbage Collector
    """
    x = object()
    print(type(x))

    print(sys.getrefcount(x))
    # 참조 복사
    y = x
    print(sys.getrefcount(x))

    # 참조 삭제
    del x
    print(sys.getrefcount(y))


def object_id():
    """
    객체의 ID 관련 예제
    """
    # Object ID
    #   객체 ID가 같으면 같은 객체를 참조
    i1 = 10
    i2 = int(10)
    print("int:", hex(id(i1)), hex(id(i2)))  # 불변 자료형

    s1 = "hello"
    s2 = str("hello")
    print("str:", hex(id(s1)), hex(id(s2)))  # 불변 자료형

    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print("lst:", hex(id(lst1)), hex(id(lst2)))  # 가변 자료형 -> 값이 같아도 다른 객체 참조

    # == : 동등성의 비교, is : 동일성의 비교
    print(i1 == i2, i1 is i2)  # int
    print(s1 == s2, s1 is s2)  # str
    print(lst1 == lst2, lst1 is lst2)  # list -> 값은 같으나(동등) 객체는 다르다(동일하지 않음)

    # is 연산자는 id의 비교
    print(id(lst1) == id(lst2), lst1 is lst2)


def object_copy():
    """
    객체의 복제
    """

    # 참조 복제
    a = 1
    b = a

    print(a, b, a is b)
    b = 2
    print(a, b, a is b)

    # 가변 자료형
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    y = x

    print("x:", x)
    print("y:", y)
    print(x is y)

    y[2] = 10
    print("x:", x)

    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    y = x[:]  # 슬라이싱 이용한 복제
    # y = copy.copy(x)  # shallow copy

    print("x:", x)
    print("y:", y)
    print(x is y)

    y[2] = 10
    print("x:", x)
    print("y:", y)

    y[0][1] = 10
    print("x:", x)
    print("y:", y)

    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    # copy 모듈의 copy 함수, deepcopy
    import copy
    y = copy.deepcopy(x)

    print("x:", x)
    print("y:", y)

    y[2] = 10
    y[0][1] = 10

    print("x:", x)
    print("y:", y)


if __name__ == "__main__":
    # symbol_table()
    # ref_count()
    # object_id()
    object_copy()