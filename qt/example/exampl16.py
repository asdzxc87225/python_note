import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QPrintDialog, QTextBrowser
from PyQt5.QtPrintSupport import QPrinter

class PrintingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("影印示例")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.print_button = QPushButton("影印", self)
        self.text_browser = QTextBrowser(self)

        layout.addWidget(self.text_edit)
        layout.addWidget(self.print_button)
        layout.addWidget(self.text_browser)

        central_widget.setLayout(layout)

        self.print_button.clicked.connect(self.print_document)

    def print_document(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            # 创建一个文档对象
            document = QTextDocument()
            document.setPlainText(self.text_edit.toPlainText())

            # 使用打印机打印文档
            document.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrintingApp()
    window.show()
    sys.exit(app.exec_())

