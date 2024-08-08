def handling_exception():
    """
    예외 처리 절차
    """
    lst = []

    # 1번째 시도
    try:
        lst[0] = 1  # 예외 발생 코드
    except:
        print("예외 발생") # 예외가 발생했을 때 처리되는 블록

    # 2번째 시도
    try:
        lst[0] = 1  # 예외 발생 코드
        4 / 0
    except Exception:   # 발생 예외 지칭
        print("Exception 예외 발생") # 예외가 발생했을 때 처리되는 블록


    # 일단 오류 회피하긴 했는데 어떤 예외가 발생했는지 알 수가 없음


    # 3번째 시도
    try:
        # lst[0] = 1  # 예외 발생 코드    -> IndexError
        4 / 0         # ZeroDivisionError
    except Exception as e:   # 발생 예외 지칭 -> 심볼을 붙여서 어떤 예외인지 확인
        print("Exception e:", e)
        print("예외 타입:", type(e))


    # 4번째 시도
    # Exception 예외는 모든 예외를 다 처리하기 때문에 구체적인 예외를 분리할 필요가 있음
    try:
        # lst[0] = 1  # 예외 발생 코드    -> IndexError
        # 4 / 0  # ZeroDivisionError
        val = int("string")
    except ValueError as e:
        print("정수를 변환할 수 없습니다.")
    except IndexError as e:
        print("IndexError")
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:  # 발생 예외 지칭 -> 심볼을 붙여서 어떤 예외인지 확인
        print("Exception e:", e)
        print("예외 타입:", type(e))

    print("==========")
    # 5번째 시도
    # Exception 예외는 모든 예외를 다 처리하기 때문에 구체적인 예외를 분리할 필요가 있음
    try:
        # lst[0] = 1  # 예외 발생 코드    -> IndexError
        # 4 / 0  # ZeroDivisionError
        val = int("2024")
    except ValueError as e:
        print("정수를 변환할 수 없습니다.")
    except IndexError as e:
        print("IndexError")
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:  # 발생 예외 지칭 -> 심볼을 붙여서 어떤 예외인지 확인
        print("Exception e:", e)
        print("예외 타입:", type(e))
    else:   # 예외가 없을 때 실행되는 블록
        print(val)
    finally:    # 예외 유무 상관 없이 가장 마지막에 실행되는 블록
        print("End of try")


def raise_exception():
    def beware_dog(animal):
        if animal == "dog":
            raise RuntimeError("강아지는 출입을 제한합니다.")
        else:
            print("어서오세요")

    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))


if __name__ == "__main__":
    # handling_exception()
    raise_exception()