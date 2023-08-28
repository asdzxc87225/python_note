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

### 03:布局管理

這個部份就有點複雜，在排版上我認為用這個會方便一些。
尤其是我們這些美感麻瓜，說實話只要整齊就好了其他在看看。


下面兩個範例的結果都一樣，這都是我請gpt寫出來的，
雖然東西簡單，但是看起來還是有點複雜，所以我就請gpt修改
主要是以每個水平的單元就包在一個class內之後在主裝，這樣應該會提高可讀性

#### ex1

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QCheckBox, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定視窗的title
        self.setWindowTitle("多元素布局示例")

        # 建立主視窗的中央元件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 建立垂直布局
        vbox = QVBoxLayout()

        # 建立水平布局1
        hbox_name = QHBoxLayout()
        label_name = QLabel("姓名:")
        self.text_name = QLineEdit()
        hbox_name.addWidget(label_name)
        hbox_name.addWidget(self.text_name)

        # 建立水平布局2
        hbox_gender = QHBoxLayout()
        label_gender = QLabel("性别:")
        self.radio_male = QRadioButton("男")
        self.radio_female = QRadioButton("女")
        hbox_gender.addWidget(label_gender)
        hbox_gender.addWidget(self.radio_male)
        hbox_gender.addWidget(self.radio_female)

        # 建立水平布局3
        hbox_hobbies = QHBoxLayout()
        label_hobbies = QLabel("兴趣爱好:")
        self.checkbox_reading = QCheckBox("阅读")
        self.checkbox_traveling = QCheckBox("旅行")
        self.checkbox_sports = QCheckBox("运动")
        hbox_hobbies.addWidget(label_hobbies)
        hbox_hobbies.addWidget(self.checkbox_reading)
        hbox_hobbies.addWidget(self.checkbox_traveling)
        hbox_hobbies.addWidget(self.checkbox_sports)

        # 建立水平布局4
        hbox_submit = QHBoxLayout()
        self.submit_button = QPushButton("确认")
        hbox_submit.addWidget(self.submit_button)

        # 將所有水平布局添加到垂直布局中
        vbox.addLayout(hbox_name)
        vbox.addLayout(hbox_gender)
        vbox.addLayout(hbox_hobbies)
        vbox.addLayout(hbox_submit)

        # 設定中央部件的布局
        central_widget.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```
### ex2
```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QCheckBox, QPushButton

class NameInput(QWidget):
    def __init__(self):
        super().__init__()
        hbox_name = QHBoxLayout()
        label_name = QLabel("姓名:")
        self.text_name = QLineEdit()
        hbox_name.addWidget(label_name)
        hbox_name.addWidget(self.text_name)
        self.setLayout(hbox_name)

class GenderSelection(QWidget):
    def __init__(self):
        super().__init__()
        hbox_gender = QHBoxLayout()
        label_gender = QLabel("性别:")
        self.radio_male = QRadioButton("男")
        self.radio_female = QRadioButton("女")
        hbox_gender.addWidget(label_gender)
        hbox_gender.addWidget(self.radio_male)
        hbox_gender.addWidget(self.radio_female)
        self.setLayout(hbox_gender)

class HobbiesSelection(QWidget):
    def __init__(self):
        super().__init__()
        hbox_hobbies = QHBoxLayout()
        label_hobbies = QLabel("兴趣爱好:")
        self.checkbox_reading = QCheckBox("阅读")
        self.checkbox_traveling = QCheckBox("旅行")
        self.checkbox_sports = QCheckBox("运动")
        hbox_hobbies.addWidget(label_hobbies)
        hbox_hobbies.addWidget(self.checkbox_reading)
        hbox_hobbies.addWidget(self.checkbox_traveling)
        hbox_hobbies.addWidget(self.checkbox_sports)
        self.setLayout(hbox_hobbies)

class SubmitButton(QWidget):
    def __init__(self):
        super().__init__()
        hbox_submit = QHBoxLayout()
        self.submit_button = QPushButton("确认")
        hbox_submit.addWidget(self.submit_button)
        self.setLayout(hbox_submit)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("多元素布局示例")

        # 创建主窗口的中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建垂直布局
        vbox = QVBoxLayout()

        # 添加各个部分的小部件
        name_input = NameInput()
        gender_selection = GenderSelection()
        hobbies_selection = HobbiesSelection()
        submit_button = SubmitButton()

        # 将各个部分的小部件添加到垂直布局中
        vbox.addWidget(name_input)
        vbox.addWidget(gender_selection)
        vbox.addWidget(hobbies_selection)
        vbox.addWidget(submit_button)

        # 设置中央部件的布局
        central_widget.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 04:對話框
### 05:菜單與工具欄
### 06:多個視窗應用程式
### 07:表格圖示
### 08:圖表與繪圖
### 09:數據庫連結
### 10:自訂意元件
### 11:多執行緒
### 12:網路通訊
### 13:文件讀寫
### 14:自定義樣式與主題
### 15:國際話語本地化
### 16:打印功能
### 17:圖像處裡
### 18:實現圖形合動畫
### 19:3D渲染
### 20:高級功能與集成
