# Thread 執行緒

一般情況下程式會一行一行的執行但是這並不一定符合我們的需求，我在寫ui的時候有遇到程式出去跑funtion就沒回來界面就卡住了。

這個時候就可以用Thread來做到一邊跑ui一邊跑funiton>

## 參考資料

[官方](https://docs.python.org/zh-tw/3.10/library/threading.html)\
[莫煩python](https://mofanpy.com/tutorials/python-basic/threading/)\
[Mike Ku](https://www.learncodewithmike.com/2020/11/multithreading-with-python-web-scraping.html)

## 間單說明

```py
import threading #使用前計的引用
```

建立執行緒的方法，間單的就這兩種。
如果有參數的話就用第二種。

```py
thread = threading.Thread(target=要執行的funtion)
thread = threading.Thread(target=要執行的funtion,args=(參數))
```

建立完之後就可以使用了。

```py
thread.start()#開始
thread.join()#等待執行緒完成
```

