import datetime
def AD_year_month_day(birthday_year,birthday_month,birthday_day):
    
    week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    week=week_list[(datetime.date(birthday_year,birthday_month,birthday_day).weekday())]
    return week
def ROC_calendar(year):
    return year-1911   
def show_calendar(birthday_year,birthday_month,birthday_day):
    st =  '西元'+str(birthday_year)+'年'+str(birthday_month)+'月'+str(birthday_day)+'日'
    st += AD_year_month_day(birthday_year,birthday_month,birthday_day)
    print(st)
    return(st)
def ROC_show_calendar(birthday_year,birthday_month,birthday_day):
    year = ROC_calendar(birthday_year)
    st =  '民國'+str(year)+'年'+str(birthday_month)+'月'+str(birthday_day)+'日'
    print(st)
    return(st)
if __name__ == "__main__":
    birthday_year = int(input("請輸入年份："))
    birthday_month = int(input("請輸入月份："))
    birthday_day = int(input("請輸入日期："))
    show_calendar(birthday_year,birthday_month,birthday_day)
    ROC_show_calendar(birthday_year,birthday_month,birthday_day)
