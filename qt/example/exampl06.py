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

