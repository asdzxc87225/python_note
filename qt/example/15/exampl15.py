import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTranslator

class TranslationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("翻译示例")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.label = QLabel(self.tr("Hello, World!"))  # 使用tr方法进行翻译
        self.button = QPushButton(self.tr("切换语言"))

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        central_widget.setLayout(layout)

        self.translator = QTranslator()
        self.load_translator("myapp_en.qm")  # 默认加载英文翻译

        self.button.clicked.connect(self.toggle_language)

    def load_translator(self, translation_file):
        if self.translator.load(translation_file):
            QApplication.instance().installTranslator(self.translator)

    def toggle_language(self):
        # 切换语言按钮的点击事件
        if self.translator.isEmpty():
            self.load_translator("myapp_fr.qm")  # 加载法语翻译
        else:
            self.translator = QTranslator()  # 清空翻译器
            QApplication.instance().removeTranslator(self.translator)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec_())

