# pyqt 

## gpt推薦的練習項目

我請gpt幫我設計20個基本練習。

### 01:Hello PyQt 

第一個範例這個是一個顯示Hello, Pyqt的一個視窗。
主要讓我們練習如何設定標題，與視窗大小與加入文字標籤等等。
main的部份就是練習如何使用這個視窗。
使用這個要了解sys的函數庫。
```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("第一個pyqt程式")

        # 设置窗口大小
        self.setGeometry(100, 100, 400, 200)

        # 创建标签控件
        label = QLabel("Hello, PyQt!", self)
        label.move(150, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

  ```

### 02:按鈕和事件處理 

- 建立一個視窗內有一個按鈕
- 按鈕按下之後顯示訊息框

我修改了gpt 給我的範例，在他的基礎上我家了一個if結構。
主要功能只是讓他在兩個狀態切換讓他有開關的感覺

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置視窗title
        self.setWindowTitle("按鈕事件範例")

        # 设置視窗大小
        self.setGeometry(100, 100, 400, 200)

        # 建立標籤
        self.label = QLabel("狀態1", self)
        self.label.move(150, 80)

        # 建力按鈕
        self.button = QPushButton("點擊", self)
        self.button.move(150, 120)

        # 按鈕觸發後的運行動作
        self.button.clicked.connect(self.on_button_click)
        self.flage = True

    def on_button_click(self):
        # 按鈕觸發後執行動作
        if self.flage :
            self.label.setText("狀態2")
            self.flage = False
        else :
            self.label.setText("狀態1")
            self.flage = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

```
