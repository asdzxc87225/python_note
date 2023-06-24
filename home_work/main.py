import age
import sign
import temp11
import untitled0
import nuer
from datetime import datetime
import time

def print_how_to_use(stage):
    if stage == 1:
        st = "各位大家好歡迎使用我們的程式。\n"
        st += "請根據指引完成你的生日輸入\n"
        print(st,end='')
        input("按enter繼續")
    elif stage == 2:
        print("----------------------------------------------")
        st = "有以下幾種功能\n"
        st += "1.查詢你活了多久過生日(實歲幾歲幾個月幾與天出生天數 ( 從出生至今過了幾天 ))\n"
        st += "2.顯是你的西元出生日與是星期幾\n"
        st += "3.顯示你的民國出生日\n"
        st += "4.農曆年月日生肖\n"
        st += "5.下次生日是西元幾年幾月幾日還有幾天過生日\n"
        st += "6.你的星座\n"
        st += "q.功能有哪些\n"
        st += "n.換下一位\n"
        st += "Q.離開\n"
        print(st)
    

def install_the_user_data():
    check = True
    while check:
        birthday_year =int(input("請輸入你的出生年(西元)："))
        birthday_month =int(input("請輸入你的出生月："))
        birthday_day =int(input("請輸入你的出生日："))
        check =check_install(birthday_year ,birthday_month ,birthday_day)
    return [birthday_year ,birthday_month ,birthday_day]
def check_install(birthday_year ,birthday_month ,birthday_day):
    big_month=[1,2,3,7,8,10,12]
    if birthday_month in big_month:
        day = 31
    elif birthday_month == 2:
        if birthday_month % 4 == 0 :
            day = 29
        else:
            day = 28
    else:
        day = 30
    if birthday_day > day or birthday_month >12 :
        st = '你是來自宇宙嗎？\n'
        st += '地球很危險的\n'
        st += '回你的星球吧'
        st += '下面一位'
        print (st,end='')
        input("按enter繼續")
        return True
    if 0>(age.user_total_day(birthday_year ,birthday_month ,birthday_day)):
        st = '恭喜你是被萬中選一的穿越者\n'
        st += '出口在那邊掰掰\n下一位。'
        print (st,end='')
        input("按enter繼續")
        return True
    return False

    
def run_the_funtion(funtion,birthday):
    if   funtion == '1':
        age.print_user_age(birthday[0],birthday[1],birthday[2])
    elif funtion == '2':
        temp11.show_calendar(birthday[0],birthday[1],birthday[2])
    elif funtion == '3':
        temp11.ROC_show_calendar(birthday[0],birthday[1],birthday[2])
    elif funtion == '4':
        nuer.show_Far_East_calendar(int(birthday[0]),int(birthday[1]),int(birthday[2]))
    elif funtion == '5':
        age.print_user_future_birthday(birthday[0],birthday[1],birthday[2])
    elif funtion == '6':
        sign.show_sign(birthday[1],birthday[2])
    elif funtion == 'q':
        print_how_to_use(2)
if __name__ == "__main__":
    print_how_to_use(1)
    birthday = install_the_user_data()
    print_how_to_use(2)
    while True:
        run = input("請輸入你要的功能:")
        run_the_funtion(run,birthday)
        print("----------------------------------------------")
        if run == 'Q' :
            print('end')
            break
        elif run == 'n':
            birthday = install_the_user_data()
        print()

