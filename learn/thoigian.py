import datetime as dt
import time

"""
    trong module datetime.py co 4 class hay dung la date, time, datetime, timedelta, ...

"""
# hien thi chi ngay
# a = dt.date(2019, 4, 12)
date_today = dt.date.today()
print(f"dt.date.today() {'=':.<30} {date_today}")

date_from_timestamp = dt.date.fromtimestamp(1551916800)
print(f"dt.date.fromtimestamp(1551916800) {'=':.<20} {date_from_timestamp}")


# hien thi chi thoi gian
# time(hour, minute and second)
# a = time() => 00:00:00
# b = time(11, 34, 56)


# hien thi ngay va gio
# b = datetime(2019, 3, 7, 23, 55, 59, 342380)
datetime_now = dt.datetime.now()
print(f"dt.datetime.now() {'=':.<30} {datetime_now}")
print(f"datetime_now.timestamp() {'=':.<30}{datetime_now.timestamp()}")

datetime_now_time = datetime_now.time()
print(f"datetime_now.time() = {datetime_now_time}")

datetime_now_f = datetime_now.strftime("%d-%m-%Y, %H:%M:%S")
print(f"datetime_now.strftime('%d-%m-%Y, %H:%M:%S') = {datetime_now_f}")

# timedelta => chuyen xua ly +, -, * cac moc thoi gian
t1 = dt.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = dt.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print(f"dt.timedelta() = {t3}")
print(f"t3.total_seconds() = {t3.total_seconds()}")


""" time.py

"""

seconds = time.time()
print(f"So giay tinh tu epoch=1/1/1970 seconds = time.time() = <{seconds}>")

print(f"time.ctime(seconds) = <{time.ctime(seconds)}>")

# time.localtime(seconds=time.time())
struct_time = time.localtime(seconds)
print("\n:", struct_time)
print("\n:", struct_time.tm_year)
print(":", struct_time.tm_hour)
 
  # trả về struct_time
print(f"\ntime.localtime(seconds) ve <{struct_time}>")
 
# trả về giây từ struct_time
print(f"\ntime.mktime(struct_time) ve seconds <{time.mktime(struct_time)}>")


if __name__ == "__main__":
    pass