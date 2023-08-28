from datetime import datetime
import time
#-----------使用者活的了多久-------------
'''
使用到detetime的套件。
datetim(年,月,日)
會將輸入的形形式進行資料類別的轉換
相減後會自動轉型
使用.days就可以把day轉出來
'''
def user_total_day(birthday_year = 2002, birthday_month = 9, birthday_day = 3):
    past_date = datetime(birthday_year, birthday_month, birthday_day)#輸入生日換取資料
    now = datetime.now()#獲取今天的資料
    time_diff = now - past_date#區得相差
    return  time_diff.days#回傳經過幾天
#--------------使用者的年紀--------------------
'''
會以西元年作為計算
回傳數值會是實歲，也就是法定歲數。
所以會進行檢查，如果沒過生日就要簡一。
'''
def user_age(birthday_year = 2002, birthday_month = 9, birthday_day = 3):
    age = (time.localtime().tm_year - birthday_year)
    if time.localtime().tm_mon < birthday_month:
        age -= 1
    elif  time.localtime().tm_mon == birthday_month and time.localtime().tm_mday < birthday_day:
        age -= 1
    return age
#--------使用者的過了幾個月-------
'''
前面已經求出了使用者活幾年了，再來就是剩下來的月
'''
def user_month_day(birthday_month = 9, birthday_day=3):
    month = time.localtime().tm_mon - birthday_month#這邊適用於判斷是否過生日了
    if month >= 0 :#這裡是過了所以直接回傳
        month= month -1
    else:#沒有過就是這裡
        month= 12 + month -1

    day = time.localtime().tm_mday- birthday_day
    if day < 0:
        day = 30 +day 
    elif day >= 0:
        month += 1
    return [month,day]
    '''
    |--n-----b---|
    |--v--x--v---|
    如果沒過相減得到的就會是x區間
    但是我們要球的是x外的所以整年12個月減去x區間就會剩下來的月數
    '''
#------------使用者還要多久過生日-------------
'''
這邊借用前面已經完成的功能，user_total_day()本質上就是算，輸入的日期到現在的時間差
如果今年還沒過生日，算出來會是負的，這個質代絕對值後直接用即可。
如果是正的邏輯跟上面的月一樣。
'''
def user_future_birthday(birthday_year = 2002, birthday_month = 9, birthday_day = 3):
    day = (user_total_day(time.localtime().tm_year, birthday_month, birthday_day))
    if day < 0:
        return [time.localtime().tm_year, birthday_month, birthday_day,abs(day)]
    else:
        return [time.localtime().tm_year+1, birthday_month, birthday_day,365-abs(day)]
#這裡是我懶的在外面做串列相加所以就在這邊組好，往後方便調用
def print_user_age(birthday_year = 2002, birthday_month = 9, birthday_day = 3):
    st ="實歲" + str(user_age(birthday_year,birthday_month,birthday_day))+"歲"
    st += str(user_month_day(birthday_month,birthday_day)[0])+"個月"
    st += "又"+str(user_month_day(birthday_month,birthday_day)[1])+"天"
    st += "\n出生到現在過了:"+str(user_total_day(birthday_year, birthday_month, birthday_day))+"天"
    print(st)
def print_user_future_birthday(birthday_year = 2002, birthday_month = 9, birthday_day = 3):
    birthday = user_future_birthday(birthday_year, birthday_month, birthday_day)
    st = "你將在"+str(birthday[0])+"年"+str(birthday[1])+"月"+str(birthday[2])+"日"
    st += "過生日"+"\n還有"+str(birthday[3])+"天"
    print(st)
    return(st)
    
if __name__ == "__main__":
    print_user_age()
    print(user_future_birthday())
    past_date = datetime(2002, 9, 3)

