def dummy():
    # 함수 구현부가 없어도 비워두면 안된다
    pass


def times(a, b):
    return a * b


# 매개변수의 유무, 출력의 유무
# return 문
#   기본적으로 함수를 종료하고 함수 호출 지점으로 돌아감
#   돌려줄 출력이 있을때는 return 뒤에 데이터를 명시


def none():
    return  # 출력 없이 return문만 썼을 때는 None


print(none())
# 함수도 객체
#   다른 객체와 동등한 권리를 갖는다
#   - 변수에 할당될 수 있고
#   - 다른 함수의 매개변수로 전달될 수 있고
#   - 함수의 결과로 반환될 수 있음


fun = times # 변수에 할당
print(fun, type(fun))
# 실행가능 객체인지를 확인 -> callable
print(callable(fun))    # fun은 실행가능한 객체?

if callable(fun):
    print(fun(10, 10))