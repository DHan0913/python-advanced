# import datetime
from datetime import datetime, date, time  # 특정 패키지(모듈) 내부의 객체



def get_datetime():
    """
    날짜와 시간 정보의 획득
    """


    # 현재 시간 -> now()
    now = datetime.now()
    print("현재시각:", now)

    # 생성자를 이용한 날짜의 지정 
    # 년, 월, 일, 시, 분, 초 밀리세컨드
    # 최소, 년, 월, 일
    dt = datetime(1999, 12, 31)
    print("1900년대 마지막 날:", dt)

    # 없는 날짜 지정하면 밸류 에러

    # datetime의 속성
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

    # 요일 정보 : 0-월 ~ 6-일
    print("요일:", now.weekday())
    
    # 날짜 정보를 반환 date() -> date 객체
    # 시간 정보를 반환 time() -> time 객체
    print("date:", now.date(), type(now.date())) # 날짜정보
    print("time:", now.time(), type(now.time())) # 시간정보

    # date 객체는 datetime 객체의 날짜 관련 속성, 메서드
    # time 객체는 datetime 객체의 시간 관련 속성

def timedelta_ex():
    """
    timedelta 클래스:
    """

    current = datetime.now()
    past = datetime(2012, 9, 24) # 과거
    # 대소 비교 가능
    print(current > past) #
    # 두 날짜의 간격
    diff = current - past
    print("시간간격:", diff)

    # 속성: days, seconds, microseconds
    print(diff.days, diff.seconds, diff.microseconds)
    # 메서드: total_seconds()
    print("총", diff.total_seconds(), "초 흘렀습니다")

    # datetime과 timedelta 합산
    print(current, "에서", diff, "를 합산한 결과:", current + diff)
    
def format_date():
    """
    .strftime() -> 날짜, 시간 정보를 문자열로 포메팅
    .strptime() -> 문쟈열 정보를 날짜, 시간 정보로 해독
    """

    current = datetime.now()
    print(current)
    print(current.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
    
    strdate = "2045년 08월 08일"
    dt = datetime.strptime(strdate, "%Y년 %m월 %d일")
    print(dt)
    print(repr(dt))

    # dt2 = eval(repr(dt))
    # print(dt2, type(dt2))

if __name__ == "__main__":
    # get_datetime()
    # timedelta_ex()
    format_date()