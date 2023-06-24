import requests
from bs4 import BeautifulSoup
class welicha():
    def __init__(self,addr):
        self.web = requests.get(addr)
        self.web.encoding = 'utf-8'
        self.soup = BeautifulSoup(self.web.text, "html.parser")
        self.data1 = self.soup.find('h1',class_='font_red18')
        self.data2 = self.soup.find('table',class_='tableWin')
        self.data3 = self.data2.find_all("span")
        self.day = [self.data3[1].text, self.data3[0].text]
    def show_(self):
        print('威力彩期數:',self.day[0],'第',self.day[1],'期')
        print('開出順序:',end = ' ')
        for n in range(10,len(self.data3)):
            print(self.data3[n].text+' ',end = '')
        print()
        print('大小順序:',end = ' ')
        for x in range(3,9):
            print(self.data3[x].text+' ',end = '')
        print()
        print('第二區:',self.data3[9].text)

if __name__ == "__main__":
    url = 'https://www.taiwanlottery.com.tw/result_all.htm#01'
    lottery = welicha(url)
    lottery.show_()
