def get_constellation(birthday_month, birthday_day):
      dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)#確定每個月區分星座的日期分開
      constellations = ("摩羯座", "水瓶座", "雙魚座", "白羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蝎座", "射手座", "摩羯座")#每個月的代表心做
      if birthday_day < dates[birthday_month-1]:#進行判斷日期是否要校準
          return constellations[birthday_month-1]
      else:
          return constellations[birthday_month]
def show_sign(birthday_month, birthday_day):
    print(get_constellation(birthday_month, birthday_day))

if __name__== "__main__":
    birthday_month = int(input("請輸入月份："))
    birthday_day = int(input("請輸入日期："))
    print (get_constellation(birthday_month, birthday_day) )
