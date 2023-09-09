import time
t = time.time()
t1 = time.localtime(t)
t2 = time.strftime('%Y/%m/%d %H:%M:%S',t1)
t3 = time.strptime(t2, '%Y/%m/%d %H:%M:%S')
print(t)     # 1634632136.9454331
print(t1)    # time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=8, tm_min=28, tm_sec=56, tm_wday=1, tm_yday=292, tm_isdst=0)
print(t2)    # 2021/10/19 08:28:56
print(t3)    # time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=8, tm_min=28, tm_sec=56, tm_wday=1, tm_yday=292, tm_isdst=-1)
