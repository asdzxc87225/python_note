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

