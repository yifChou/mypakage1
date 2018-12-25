from datetime import datetime
import functools
def run_time(func): #计算函数运行所需时间 使用：在函数前面加上@run_time
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start = datetime.now()
        f = func(*args,**kw)
        end = datetime.now()
        print(func.__name__,"运行时间",end-start)
        return func(*args,**kw)
    return wrapper
def fun_name(func): #函数异常打印出错原因 使用：在函数前面加上@fun_name
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as e:
            print(func.__name__,"：出错，原因：",e)
        return func(*args,**kwargs)
    return wrapper