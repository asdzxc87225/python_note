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

