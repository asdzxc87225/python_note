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

