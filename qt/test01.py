import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QCheckBox, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.vbox_1()
        self.vbox_2()

        hbox = QHBoxLayout()
        hbox.addLayout(self.vbox)
        hbox.addLayout(self.vbox2)
        central_widget.setLayout(hbox)
    def vbox_1 (self):
        self.vbox = QVBoxLayout()
        labe1 = QLabel("labe1")
        labe2 = QLabel("labe2")
        labe3 = QLabel("labe3")
        self.vbox.addWidget(labe1)
        self.vbox.addWidget(labe2)
        self.vbox.addWidget(labe3)

    def vbox_2 (self):
        self.vbox2 = QVBoxLayout()
        labe4 = QLabel("labe1")
        labe5 = QLabel("labe2")
        labe6 = QLabel("labe3")
        self.vbox2.addWidget(labe4)
        self.vbox2.addWidget(labe5)
        self.vbox2.addWidget(labe6)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
