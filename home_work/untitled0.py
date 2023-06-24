
import datetime
class Lunar(object):
  g_lunar_month_day = [
    0x4ae0, 0xa570, 0x5268, 0xd260, 0xd950, 0x6aa8, 0x56a0, 0x9ad0, 0x4ae8, 0x4ae0,  #1910
    0xa4d8, 0xa4d0, 0xd250, 0xd548, 0xb550, 0x56a0, 0x96d0, 0x95b0, 0x49b8, 0x49b0,  #1920
    0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada8, 0x2b60, 0x9570, 0x4978, 0x4970, 0x64b0,  #1930
    0xd4a0, 0xea50, 0x6d48, 0x5ad0, 0x2b60, 0x9370, 0x92e0, 0xc968, 0xc950, 0xd4a0,  #1940
    0xda50, 0xb550, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950, 0xb4a8, 0x6ca0,  #1950
    0xb550, 0x55a8, 0x4da0, 0xa5b0, 0x52b8, 0x52b0, 0xa950, 0xe950, 0x6aa0, 0xad50,  #1960
    0xab50, 0x4b60, 0xa570, 0xa570, 0x5260, 0xe930, 0xd950, 0x5aa8, 0x56a0, 0x96d0,  #1970
    0x4ae8, 0x4ad0, 0xa4d0, 0xd268, 0xd250, 0xd528, 0xb540, 0xb6a0, 0x96d0, 0x95b0,  #1980
    0x49b0, 0xa4b8, 0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada0, 0xab60, 0x9370, 0x4978,  #1990
    0x4970, 0x64b0, 0x6a50, 0xea50, 0x6b28, 0x5ac0, 0xab60, 0x9368, 0x92e0, 0xc960,  #2000
    0xd4a8, 0xd4a0, 0xda50, 0x5aa8, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950,  #2010
    0xb4a0, 0xb550, 0xb550, 0x55a8, 0x4ba0, 0xa5b0, 0x52b8, 0x52b0, 0xa930, 0x74a8,  #2020
    0x6aa0, 0xad50, 0x4da8, 0x4b60, 0x9570, 0xa4e0, 0xd260, 0xe930, 0xd530, 0x5aa0,  #2030
    0x6b50, 0x96d0, 0x4ae8, 0x4ad0, 0xa4d0, 0xd258, 0xd250, 0xd520, 0xdaa0, 0xb5a0,  #2040
    0x56d0, 0x4ad8, 0x49b0, 0xa4b8, 0xa4b0, 0xaa50, 0xb528, 0x6d20, 0xada0, 0x55b0,  #2050
  ]
  g_lunar_month = [
    0x00, 0x50, 0x04, 0x00, 0x20,  #1910
    0x60, 0x05, 0x00, 0x20, 0x70,  #1920
    0x05, 0x00, 0x40, 0x02, 0x06,  #1930
    0x00, 0x50, 0x03, 0x07, 0x00,  #1940
    0x60, 0x04, 0x00, 0x20, 0x70,  #1950
    0x05, 0x00, 0x30, 0x80, 0x06,  #1960
    0x00, 0x40, 0x03, 0x07, 0x00,  #1970
    0x50, 0x04, 0x08, 0x00, 0x60,  #1980
    0x04, 0x0a, 0x00, 0x60, 0x05,  #1990
    0x00, 0x30, 0x80, 0x05, 0x00,  #2000
    0x40, 0x02, 0x07, 0x00, 0x50,  #2010
    0x04, 0x09, 0x00, 0x60, 0x04,  #2020
    0x00, 0x20, 0x60, 0x05, 0x00,  #2030
    0x30, 0xb0, 0x06, 0x00, 0x50,  #2040
    0x02, 0x07, 0x00, 0x50, 0x03  #2050
  ]
  START_YEAR = 1901
  gan = '甲乙丙丁戊己庚辛壬癸'
  zhi = '子醜寅卯辰巳午未申酉戌亥'
  xiao = '鼠牛虎兔龍蛇馬羊猴雞狗豬'
  lm = '正二三四五六七八九十冬臘'
  ld = '初一初二初三初四初五初六初七初八初九初十十一十二十三十四十五十六十七十八十九二十廿一廿二廿三廿四廿五廿六廿七廿八廿九三十'
  def __init__(self, dt = None):
    self.localtime = dt if dt else datetime.datetime.today()
  def sx_year(self):    
    year = self.ln_year() - 3 - 1 
    year = year % 12 
    return self.xiao[year]
  def gz_year(self):     
    year = self.ln_year() - 3 - 1 
    G = year % 10 
    Z = year % 12 
    return self.gan[G] + self.zhi[Z]
  def gz_month(self): 
    pass
  def gz_day(self):     
    C = ct.year // 100 
    y = ct.year % 100 
    y = y - 1 if ct.month == 1 or ct.month == 2 else y
    M = ct.month 
    M = M + 12 if ct.month == 1 or ct.month == 2 else M
    d = ct.day 
    i = 0 if ct.month % 2 == 1 else 6 
    G = 4 * C + C // 4 + 5 * y + y // 4 + 3 * (M + 1) // 5 + d - 3 - 1
    G = G % 10
    Z = 8 * C + C // 4 + 5 * y + y // 4 + 3 * (M + 1) // 5 + d + 7 + i - 1
    Z = Z % 12
    return self.gan[G] + self.zhi[Z]
  def ln_year(self): 
    year, _, _ = self.ln_date()
    return year
  def ln_month(self): 
    _, month, _ = self.ln_date()
    return month
  def ln_day(self): 
    _, _, day = self.ln_date()
    return day
  def ln_date(self): 
    delta_days = self._date_diff()   
    if (delta_days < 49):
      year = self.START_YEAR - 1
      if (delta_days <19):
       month = 11;
       day = 11 + delta_days
      else:
        month = 12;
        day = delta_days - 18
      return (year, month, day)
    delta_days -= 49
    year, month, day = self.START_YEAR, 1, 1
    tmp = self._lunar_year_days(year)
    while delta_days >= tmp:
      delta_days -= tmp
      year += 1
      tmp = self._lunar_year_days(year)
    (foo, tmp) = self._lunar_month_days(year, month)
    while delta_days >= tmp:
      delta_days -= tmp
      if (month == self._get_leap_month(year)):
        (tmp, foo) = self._lunar_month_days(year, month)
        if (delta_days < tmp):
          return (0, 0, 0)
          return (year, month, delta_days+1)
        delta_days -= tmp
      month += 1
      (foo, tmp) = self._lunar_month_days(year, month)
    day += delta_days
    return (year, month, day)
  def ln_date_str(self):
    _, month, day = self.ln_date()
    return '農曆{}月{}'.format(self.lm[month-1], self.ld[(day-1)*2:day*2])  
  def calendar(self):
    pass
  def _date_diff(self):
    return (self.localtime - datetime.datetime(1901, 1, 1)).days
  def _get_leap_month(self, lunar_year):
    flag = self.g_lunar_month[(lunar_year - self.START_YEAR) // 2]
    if (lunar_year - self.START_YEAR) % 2:
      return flag & 0x0f
    else:
      return flag >> 4
  def _lunar_month_days(self, lunar_year, lunar_month):
    if (lunar_year < self.START_YEAR):
      return 30
    high, low = 0, 29
    iBit = 16 - lunar_month;
    if (lunar_month > self._get_leap_month(lunar_year) and self._get_leap_month(lunar_year)):
      iBit -= 1
    if (self.g_lunar_month_day[lunar_year - self.START_YEAR] & (1 << iBit)):
      low += 1
    if (lunar_month == self._get_leap_month(lunar_year)):
      if (self.g_lunar_month_day[lunar_year - self.START_YEAR] & (1 << (iBit -1))):
         high = 30
      else:
         high = 29
    return (high, low)
  def _lunar_year_days(self, year):
    days = 0
    for i in range(1, 13):
      (high, low) = self._lunar_month_days(year, i)
      days += high
      days += low
    return days
  def _julian_day(self):
    ct = self.localtime 
    year = ct.year
    month = ct.month
    day = ct.day
    if month <= 2:
      month += 12
      year -= 1
    B = year / 100
    B = 2 - B + year / 400
    dd = day + 0.5000115740 
    return int(365.25 * (year + 4716) + 0.01) + int(30.60001 * (month + 1)) + dd + B - 1524.5 
def show_lunar_calendar(birthday_year=2002,birthday_month=9,birthday_day=3):
    t = datetime.datetime(birthday_year,birthday_month,birthday_day)
    lt = Lunar(t)
    st =(lt.gz_year()+'年'+lt.ln_date_str()+lt.gz_day()+'日屬'+lt.sx_year())
    return(st)

if __name__ == '__main__':
    birthday_year = int(input("請輸入年份："))
    birthday_month = int(input("請輸入月份："))
    birthday_day = int(input("請輸入日期："))  
    ct = datetime.datetime(birthday_year,birthday_month,birthday_day)
    print(show_lunar_calendar(2002,9,3))
