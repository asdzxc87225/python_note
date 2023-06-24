import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_data():
    url = 'https://www.twse.com.tw/rwd/zh/afterTrading/FMSRFK?date=20190101&stockNo=2330&response=html'
    web = requests.get(url)
    web.encoding = 'utf-8'
    soup = BeautifulSoup(web.text, 'html.parser')
    data1 = soup.find("tbody")
    data2 = data1.find_all("td")
    data3 = [ list() for x in range(9)]
    cont = 0
    for x in range(len(data2)):
        data3[cont].append((data2[x].text))
        cont += 1
        if cont == 9:
            cont = 0
    for x in range(1,4,1):
        for y in range(12):
            data3[x][y] = float(data3[x][y])
    for x in range(1,4,1):
        for y in range(12):
            data3[x][y] = int(data3[x][y])
    return data3
if __name__ == '__main__':
    data = get_data()
    plt.plot(data[1],data[2],'--',label = 'hightest price')
    plt.plot(data[1],data[3],'--',label = 'hightest price')
    plt.legend()
    plt.title('108 2330 Monthly transaction information')
    plt.xlabel('month',fontsize='14')
    plt.ylabel('price',fontsize='14')
    #plt.yticks([10,20,30])
    #plt.ylim(200,500)
    plt.show()
