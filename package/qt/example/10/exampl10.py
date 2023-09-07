import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 建立輸入框
        self.input_line_edit = QLineEdit(self)
        self.input_line_edit.setPlaceholderText('輸入格式，如 2 + 3')

        # 建立按鈕
        self.add_button = QPushButton('+', self)
        self.subtract_button = QPushButton('-', self)
        self.calculate_button = QPushButton('計算', self)

        # 連接按鈕的觸發事件的函數
        self.add_button.clicked.connect(self.addOperation)
        self.subtract_button.clicked.connect(self.subtractOperation)
        self.calculate_button.clicked.connect(self.calculateResult)

        # 建立布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.subtract_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input_line_edit)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.calculate_button)

        self.setLayout(main_layout)

    def addOperation(self):
        current_text = self.input_line_edit.text()
        self.input_line_edit.setText(current_text + ' + ')

    def subtractOperation(self):
        current_text = self.input_line_edit.text()
        self.input_line_edit.setText(current_text + ' - ')

    def calculateResult(self):
        expression = self.input_line_edit.text()
        try:
            result = eval(expression)
            self.input_line_edit.setText(str(result))
        except Exception as e:
            self.input_line_edit.setText('錯誤')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWidget()
    window.setWindowTitle('簡單計算機')
    window.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())

