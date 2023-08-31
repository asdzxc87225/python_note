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

