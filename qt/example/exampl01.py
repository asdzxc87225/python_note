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
