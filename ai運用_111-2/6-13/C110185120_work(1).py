import matplotlib.pyplot as plt

listx= [2015,2016,2017,2018,2019]
listy1= [126,150,199,178,150]
listy2= [123,145,178,173,123]
plt.title('Sales Report')
plt.xlabel('Million')
plt.ylabel('Year')
plt.plot(listx,listy1,'r--s',label='Taipei')
plt.plot(listx,listy2,'g--*',label='Kaohsiung')
plt.legend()
plt.xticks(listx)
plt.yticks(range(50,255,25))
plt.grid(True)
plt.grid( linestyle=':', linewidth=1, alpha=1)
plt.show()
