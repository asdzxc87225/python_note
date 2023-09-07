# 按鈕的建立
按鈕在這裡是一個概念，它就是一個讓使用者點擊的東西。
我們可以藉由他的觸發來執行特定的程式。

## step1
按照慣例引入函數這次的按鈕就是QPushButton。

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
```
## step2
建立按鈕與設定觸法動作
```py
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ...
        #建立按鈕物件
        self.button = QPushButton("點擊", self)
        self.button.move(150, 120)
        ...
        #連結運作funtion
        self.button.clicked.connect(self.on_button_click)
```
## 運用補充
雖然按鈕與使用者的互動只又按下，但是還是有其他變化。

### 一般觸發動作
這裡就是向上面的範例一樣建立後就直接跑程式。

### 一下開下次關
我的話會用一個變數通常是flage代表狀態在用if的結構來確定開或是關。
```py
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ...
        # 建力按鈕
        self.button = QPushButton("點擊", self)
        self.button.move(150, 120)

        # 按鈕觸發後的運行動作
        self.button.clicked.connect(self.on_button_click)
        self.flage = True
        ...

    def on_button_click(self):
        # 按鈕觸發後執行動作
        if self.flage :
            self.label.setText("狀態2")
            self.flage = False
        else :
            self.label.setText("狀態1")
            self.flage = True
```
### 多個狀態循環
這個就是在上面的範例為基礎，只是flage變數重bool變成int形式。
只要能讓flage變數的數值能夠循環變化就可以達到此功能。

```py
flage += 1 
flage = flage // n
```
上面這兩行重複執行flage的數值就會以0到n-1的數值循環。
之要我們用if elif else 就可以定義不同數值所代表的功能。
