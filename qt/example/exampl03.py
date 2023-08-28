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

