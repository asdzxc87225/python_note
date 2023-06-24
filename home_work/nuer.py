from zhdate import ZhDate
from datetime import datetime
def Far_East_calendar(birthday_year,birthday_month,birthday_day): 
    sky = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
    land = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    year = sky[birthday_year % 10 +6] + land[birthday_year%12-4]
    date1 = ZhDate.from_datetime(datetime(birthday_year,birthday_month,birthday_day)) 
    return year+"年農曆"+str(date1.lunar_month)+"月"+str(date1.lunar_day)+"日"
def Far_East_Zodiac(year):
    zodiac = ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
    return (zodiac[year%12-4])
def show_Far_East_calendar(birthday_year,birthday_month,birthday_day):
        st = str(Far_East_calendar(birthday_year,birthday_month,birthday_day))+'屬'
        st += Far_East_Zodiac(birthday_year)
        print(st)

if __name__ == "__main__":
    print(Far_East_calendar(2002,9,3))
    print(Far_East_Zodiac(2002))
