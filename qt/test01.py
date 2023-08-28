import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget, QSpinBox, QLineEdit
from datetime import datetime

class RFTransmitterQtApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("射頻發射程式")
        self.setGeometry(100, 100, 300, 200)

        self.port_label = QLabel("COM 口：")
        self.port_combobox = QComboBox()
        self.port_combobox.addItem("/dev/ttyUSB0")  # 根據您的情況添加串口
        self.port_combobox.addItem("/dev/ttyUSB1")
        self.port_combobox.addItem("/dev/ttyACM0")
        self.port_combobox.addItem("COM1")
        # 添加更多串口

        self.baud_label = QLabel("波特率：")
        self.baud_combobox = QComboBox()
        self.baud_combobox.addItem("9600")
        self.baud_combobox.addItem("115200")
        # 添加更多波特率


        self.transmit_button = QPushButton("開始發射")

        self.status_label = QLabel("發射狀態：等待發射")

        self.mode_data1 = QLabel("資料長度(byte):")
        self.target1 = QLineEdit()
        self.target1.setText('10')
        self.mode_data2 = QLabel("資料總數(次數):")
        self.target2 = QLineEdit()
        self.target2.setText('5')
        self.mode_data3 = QLabel("資料間隔時間(s):")
        self.target3 = QLineEdit()
        self.target3.setText('0.5')

        layout = QVBoxLayout()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_combobox)
        layout.addWidget(self.baud_label)
        layout.addWidget(self.baud_combobox)
        layout.addWidget(self.mode_data1)
        layout.addWidget(self.target1)
        layout.addWidget(self.mode_data2)
        layout.addWidget(self.target2)
        layout.addWidget(self.mode_data3)
        layout.addWidget(self.target3)

        layout.addWidget(self.status_label)
        layout.addWidget(self.transmit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.transmitter = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RFTransmitterQtApp()
    window.show()
    sys.exit(app.exec_())

