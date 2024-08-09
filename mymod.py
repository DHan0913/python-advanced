pi = 3.14


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def main():
    print("이 모듈은 최상위 모듈입니다")


print("모듈의 이름은", __name__)

if __name__ == "__main__":
    main()
else:   # 모듈로 임포트 될 때의 코드
    pass