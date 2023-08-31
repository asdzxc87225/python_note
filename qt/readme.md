# pyqt 

## gpt推薦的練習項目

我請gpt幫我設計20個基本練習。幾本先分成兩個階段由於qt的坑真的太大所以一個一個的指令去聊解對於實做並沒有太大的幫助，所以第一階段先以實做也就是20個基本練習來作為入門，先體驗架構大概了解寫一個界面的結構，第二街對在針對細節去做研究這部份就要仰賴官方的文擋了。

範例都放到example裡可以去查看


----
### 01:Hello PyQt 

第一個範例這個是一個顯示Hello, Pyqt的一個視窗。
主要讓我們練習如何設定標題，與視窗大小與加入文字標籤等等。
main的部份就是練習如何使用這個視窗。
使用這個要了解sys的函數庫。
#### 使用到的函數庫
- sys
##### qt的函數
- QApplication
- QMainWindow
- QLable


##### 引入函數庫

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
```
##### MyWindow的物件

- 設定視窗標題
- 設定視窗大小
- 建立物件

繼承QMainWindow的變數與函數
```py
super().__init__()
```

|函數 | 功能|
| -- | -- |
| setWindowTitle | 設定視窗的標題 |
| setGeometry | 設定大小 |

##### 開啟窗口的方法
要使用我們設定的視窗要調用到sys的函數庫，來控制開始與結束。
```py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

----
### 02:按鈕和事件處理 

- 建立一個視窗內有一個按鈕
- 按鈕按下之後顯示訊息框

我修改了gpt 給我的範例，在他的基礎上我家了一個if結構。
主要功能只是讓他在兩個狀態切換讓他有開關的感覺
#### 引入的函數庫
- sys
#### qt函數庫
- QApplication
- QMainWindow
- QPushButton
- QLabel
```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
```
#### 使用的方法

##### 設定樣式與位置

```py
按鈕變數 = QPushButton("按鈕上的文字", self)
```
|方法 	|參數 	|說明|
| -- | -- | --|
|move() 	|x, y 	|設定 QPushButton 在擺放的父元件中的 xy 座標，x 往右為正，y 往下為正，尺寸根據內容自動延伸。|
|setGeometry() 	|x, y, w, h 	|設定 QPushButton 在擺放的父元件中的 xy 座標和長寬尺寸，x 往右為正，y 往下為正，如果超過長寬尺寸，預設會被裁切無法顯示。|

##### 觸發的方式
```py
按鈕變數.clicked.connect(運形函數)
```
----
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

程式在閱讀時先看MyWindow這個主視窗，可以知道只有一個按鈕之後就是觸發後的事件。
這個範例我們可以感受到class美好在主視窗的class，我們只要煩惱布局的問題就號，其他的就交給各自的class去負責。
MyDialog定義上市對話框，可以用來作為提示警告引導輸入等功能，這個範例就是簡提示使用者輸入之後再按確定送出。
```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLineEdit

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # 設定對會框title
        self.setWindowTitle("輸入對話框")

        # 建立對話框的布局
        layout = QVBoxLayout()

        # 建立文字輸入框
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # 建立確定按鈕
        self.ok_button = QPushButton("確定", self)
        layout.addWidget(self.ok_button)
        self.ok_button.clicked.connect(self.on_ok_button_click)

        # 設定對話框的布局
        self.setLayout(layout)

    def on_ok_button_click(self):
        # 當使用點擊卻動按鈕時，獲取文字輸入框中的文字
        user_input = self.text_input.text()
        print("使用者輸入:", user_input)
        self.accept()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定視窗標題
        self.setWindowTitle("主視窗")

        # 建立按鈕，用於打開對話框
        self.open_dialog_button = QPushButton("打開對話框", self)
        self.open_dialog_button.clicked.connect(self.open_dialog)
        self.setCentralWidget(self.open_dialog_button)

    def open_dialog(self):
        # 建立並顯示對話框
        dialog = MyDialog()
        result = dialog.exec_()
        if result == QDialog.Accepted:
            print("使用者按了確定按鈕")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

```

### 05:菜單與工具欄

Menu Bur 與 Tool Bar 在我看來就是兩種選單試過就知道了，目前看來就是跟按鈕的功能很像觸發後執行某些事件。
QAction建立選單內的內容，範例程式基本上就是先建立QAction再把建立好的物件加入MnuBar或是
ToolBar內部之後在顯示。
```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定主視窗標題
        self.setWindowTitle("菜單欄與工具欄的範例")


        # 創見問建菜單選項
        new_action = QAction("新建", self)
        open_action = QAction("打开", self)
        save_action = QAction("保存", self)
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)

        # 建立菜單欄
        menubar = self.menuBar()
        # 建立文件菜單
        file_menu = menubar.addMenu("文件")
        # 將菜單選項添加到文件菜單

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # 建立工具欄
        toolbar = QToolBar("工具欄")
        self.addToolBar(toolbar)

        # 在工具欄上添加工具按鈕
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 06:多個視窗應用程式

這個就是兩個視窗，程式結構基本一樣只是一個在上層令一個就等上層的呼叫。


```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('子視窗')
        self.setGeometry(200, 200, 400, 300)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('主視窗')
        self.setGeometry(100, 100, 400, 300)

        self.open_window_button = QPushButton('打开新視窗', self)
        self.open_window_button.clicked.connect(self.openNewWindow)

    def openNewWindow(self):
        self.new_window = SubWindow()
        print('show sub window')
        self.new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
```

### 07:檢視表

資料的管理顯示，這個部份除了如何將資料顯示出來外，還有要如何讀資料存資ㄌ料的問題。
未來我打算把arduino 用電腦讀進來，之後資料的處理就很重要。

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定主視窗標題
        self.setWindowTitle("表格圖示範例")

        # 建立一個表格檢視表
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 400, 200)

        # 設定表格的行數何列數
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        # 設定表頭標籤
        self.tableWidget.setHorizontalHeaderLabels(["列1", "列2", "列3"])

        # 添加數據到表格單原格
        data = [["A1", "B1", "C1"],
                ["A2", "B2", "C2"],
                ["A3", "B3", "C3"]]

        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(data[i][j])
                self.tableWidget.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```

### 08:圖表與繪圖

matplotlib 的函數庫來做繪圖的動作，由qt來做顯示這樣的設計希望未來可以提供更靈活的程式可以好好使用。

```py
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  # 添加导入语句
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class InteractiveChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定視窗標題
        self.setWindowTitle("互動式折線圖")

        # 建立 Matplotlib Figure 對象
        self.figure, self.ax = plt.subplots()

        # 建立 Matplotlib Canvas 對象，並將 Figure 放入其中
        self.canvas = FigureCanvas(self.figure)

        # 建立 widget 以容納 Canvas
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 建立排版管理器
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.canvas)

        # 啟用 Matplotlib 的引導工具欄
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

        # 建立數據
        x = [1, 2, 3, 4, 5]
        y = [3, 4, 2, 6, 5]

        # 繪製折線圖
        self.ax.plot(x, y, marker='o')

        # 設置橫軸與縱軸的標籤
        self.ax.set_xlabel('X轴')
        self.ax.set_ylabel('Y轴')

        # 顯示圖表
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveChartWindow()
    window.show()
    sys.exit(app.exec_())
```

### 09:數據庫連結
數據庫的連結就以連結來說並不難，問題會出在連接之後呢？與在這之前的資料庫設定

```py
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('mydatabase.db')

# 打开数据库
if db.open():
    print("數據連接成功")
    # 在这里执行数据库操作，如查询、插入、更新等
else:
    print("數據庫連接失敗")
```

### 10:自訂意元件

這個題目就是讓我自行設定一個功能並且做出來，gpt就給了一個計算機的範例。
這部份我之前有做python\_read這個專案就符合要求了。

- 功能目標
- 指引使用者
- 輸出結果
- 錯誤指示

基本上設計時就符合這些功能就好了。

### 11:多執行緒

這個部份我在python\_read也有實做過，我是用python內建的threading來實做。
基本上就是以下幾點要知道。

- 什麼時候要用
- 如何建立執行序
- 如何執行緒跑funtion
- 如果funtion要傳變數要如何做

### 12:網路通訊

這部份要有網路的能力，這題先跳過。

结合 PyQt 和网络通信，您可以创建强大的图形用户界面（GUI）应用程序，以与远程服务器、Web 服务或其他网络资源进行交互。以下是一些 PyQT 结合网络通信可以带来的变化和用途：

    实时数据显示：您可以创建具有实时数据更新功能的应用程序，例如监控实验室设备、传感器或网络数据。通过网络通信，您可以获取远程数据并在 PyQt 界面上实时显示。

    远程控制：结合网络通信，您可以创建远程控制应用程序，用于控制远程设备或系统。用户可以通过 PyQt 界面发送命令或控制信号。

    数据可视化：将网络通信与 PyQt 结合使用，可以将从远程服务器获取的数据可视化，以创建仪表板、监控界面或数据分析工具。

    客户端-服务器应用程序：您可以创建客户端-服务器应用程序，其中 PyQt 程序充当客户端，与服务器进行通信以获取或提交数据。这对于构建分布式应用程序非常有用。

    聊天应用程序：结合网络通信，您可以开发实时聊天应用程序，允许用户通过 PyQt 界面发送和接收消息，与其他用户进行交流。

    文件传输和共享：通过网络通信，您可以创建文件传输应用程序，允许用户通过 PyQt 界面上传、下载和共享文件。

    远程桌面控制：结合网络通信，您可以实现远程桌面控制应用程序，允许用户从远程访问和控制其他计算机的桌面。

    云服务集成：将 PyQt 应用程序与云服务（例如 AWS、Azure、Google Cloud）集成，以实现云存储、计算和分析功能。

    Web API 访问：使用 PyQt 和网络通信，可以轻松访问和使用各种 Web API，例如社交媒体 API、地图服务 API 或数据 API。

    物联网（IoT）控制：通过网络通信，您可以与物联网设备通信，监控和控制物联网设备，例如智能家居设备或传感器网络。

    远程教育和远程会议：结合网络通信，您可以创建远程教育或远程会议应用程序，允许教育者和参与者之间进行实时互动。

    在线游戏：使用 PyQt 和网络通信，可以创建在线多人游戏，支持玩家之间的实时互动。

总之，将 PyQt 与网络通信相结合，可以为您的图形用户界面应用程序增加丰富的互动性和实时性。这将使您能够构建各种类型的应用程序，满足不同领域的需求。

### 13:文件讀寫

這提要注意的就是讀取文件之後在寫數內容或是新增文件等等的操作。

```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget

class FileInteractionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("文件交互程序")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.central_widget.setLayout(layout)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        # 创建打开文件操作
        self.open_action = QAction("打开文件", self)
        self.open_action.triggered.connect(self.open_file)

        # 创建保存文件操作
        self.save_action = QAction("保存文件", self)
        self.save_action.triggered.connect(self.save_file)

    def create_menus(self):
        # 创建文件菜单
        file_menu = self.menuBar().addMenu("文件")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                content = file.read()
                self.text_edit.setPlainText(content)

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            content = self.text_edit.toPlainText()
            with open(file_name, "w") as file:
                file.write(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileInteractionApp()
    window.show()
    sys.exit(app.exec_())
```

### 14:自定義樣式與主題
自定義簡單的就是設定的好看阿之類的，但是這對我們這些美感麻瓜來說有點太難了。
```py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class CountryStyleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("农村风格界面")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # 创建一个标签并设置样式
        label = QLabel("欢迎来到乡村")
        label.setStyleSheet("font-size: 20px; color: green;")

        # 创建一个按钮并设置样式
        button = QPushButton("点击我")
        button.setStyleSheet("background-color: #FFD700; border: 2px solid brown; font-weight: bold;")

        # 将标签和按钮添加到布局中
        layout.addWidget(label)
        layout.addWidget(button)

        self.central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountryStyleApp()
    window.show()
    sys.exit(app.exec_())

```
## 後面的需要配合其他套件之後在研究
### 15:國際話語本地化

這個部份我還在想一下要如何使用可能要用字典或是其他資料格式
然後在去取代現有的元件之後更新界面。

### 16:影印功能

這個部份qt有提供但是我決的它部穩定，所以我想應該用其他的函數庫qt 就是只應使用者操作與顯示為主。

### 17:圖像處裡
這個要結合opencv 會比較好，這部份等等在研究
### 18:實現圖形合動畫

### 19:3D渲染
### 20:高級功能與集成
