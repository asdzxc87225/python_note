import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QWidget

class ChatClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("localhost", 12345))  # 服务器地址和端口

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def receive_messages(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if message:
                window.add_message(message)

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("简单聊天客户端")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.text_browser = QTextBrowser()
        self.layout.addWidget(self.text_browser)

        self.input_line_edit = QLineEdit()
        self.input_line_edit.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_line_edit)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.chat_client = ChatClient()

    def send_message(self):
        message = self.input_line_edit.text()
        self.chat_client.send_message(message)
        self.input_line_edit.clear()

    def add_message(self, message):
        self.text_browser.append(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()

    receive_thread = threading.Thread(target=window.chat_client.receive_messages)
    receive_thread.daemon = True
    receive_thread.start()

    sys.exit(app.exec_())

