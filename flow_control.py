def if_statement():
    """
    if ~ elif ~ else
    """

    """
    금액을 입력받고
        금액이 10,000원 이상이면 by taxi
        금액이 2,000원 이상이면 by bus
        그 미만이면 on foot
    """
    money = int(input("얼마 가지고 있어? "))

    message = ""
    if money >= 10000:
        message += "by taxi"
    elif money >= 2000:
        message += "by bus"
    else:
        message += "on foot"

    print(message)


def cond_expr():
    """
    조건 표현식
    """
    money = int(input("얼마 가지고 있어? "))

    message = "by taxi" if money >= 10000 else "by bus" if money >= 2000 else "on foot"
    print(message)


def for_ex():
    """
    반복문 활용 패턴
    """
    # 기본적인 순회 : for 타겟변수 in 순차자료형
    for animal in ['cat', 'cow', 'dog', 'tiger']:  # 순차형의 length 만큼 순회
        print(animal, end=' ')  # sep=' ' (구분자), end='\n' (종결자)
    else:
        print()

    # 인덱스와 요소를 함께 받아올 경우 : enumerate 함수
    for index, color in enumerate(['red', 'blue', 'green', 'yellow', 'black', 'white']):
        print(index, color)

    # continue : 남아있는 코드 실행 중단 -> 다음번 루프
    # break : 반복을 종료 바깥으로 이동

    # 1 ~ 10까지 loop -> 짝수만 출력
    print("===== continue")
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        print(i, end=' ')
    else:
        print()

    print("===== break")

    r1 = list(range(1, 12, 2))
    print("r1:", r1)
    r2 = r1 + [12, 13, 15]
    print("r2:", r2)

    # 리스트 내부에서 짝수를 찾으면 "찾았습니다" -> 루프 종료
    #                       못찾으며 "없습니다"
    for i in r2:
        if i % 2 == 0:
            print("짝수를 찾았습니다.", i)
            break  # 루프 탈출
    else:
        print("짝수는 없습니다.")

    """
    while 반복조건:
        반복 코드

        - 반복 조건 잘 제어해서 무한루프에 빠지지 않도록 제어
    """

    # 연습문제 1
    # 2단 ~ 9단까지
    # 2 x 2 = 4
    # 2 x 3 = 6
    # ...

    for a in range(2, 10):
        for b in range(1, 10):
            print(a, "X" ,b, "=", a * b)

    # 연습문제 2
    # 별 그리기
    # *
    # **
    # ***
    # ****
    # *****

    # pythonic way
    for i in range(1, 6):
        print("*" * i)


if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    for_ex()