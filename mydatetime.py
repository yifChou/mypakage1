import time
import functools
from datetime import datetime
def run_time(func): #计算函数运行所需时间 使用：在函数前面加上@run_time
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start = datetime.now()
        f = func(*args,**kw)
        end = datetime.now()
        print(func.__name__,"运行时间",end-start)
        return func(*args,**kw)
    return wrapper
def get_now():#获取当前时间字符串--2015-12-12 12:12:12
    now = datetime.now()
    now = str(now).split(".")[0]
    return now
def get_timestamp(): #获取当前时间的java时间戳
    dt = time.time()*1000
    timestamp = str(dt).split(".")[0]
    return timestamp
def str_to_timestamp(strtime):#字符类型转换成java时间戳--20151212121212
    strlen = str(strtime)
    if len(strlen)<= 14 :
        dt = datetime(int(strlen[0:4]),int(strlen[4:6]),int(strlen[6:8]),int(strlen[8:10]),int(strlen[10:12]),int(strlen[12:14]))
        return dt.timestamp() * 1000
    else:
        print("请输入14位数")
def stamp_to_str(stamp): #java时间戳转换成字符--1449893532000
    pystamp = stamp/1000
    dt = datetime.fromtimestamp(pystamp)
    return str(dt)
@run_time
def date_format_str(format = "%Y %m %d %H:%M:%S"):#当前时间按照一定格式输出("%Y-%m-%d-%H-%M-%S")
    now = datetime.now()
    strnow = now.strftime(format)
    time.sleep(61)
    return strnow


date_format_str()