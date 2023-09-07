import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget

class FileInteractionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("文件交互程序")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.central_widget.setLayout(layout)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        # 创建打开文件操作
        self.open_action = QAction("打开文件", self)
        self.open_action.triggered.connect(self.open_file)

        # 创建保存文件操作
        self.save_action = QAction("保存文件", self)
        self.save_action.triggered.connect(self.save_file)

    def create_menus(self):
        # 创建文件菜单
        file_menu = self.menuBar().addMenu("文件")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                content = file.read()
                self.text_edit.setPlainText(content)

    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            content = self.text_edit.toPlainText()
            with open(file_name, "w") as file:
                file.write(content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileInteractionApp()
    window.show()
    sys.exit(app.exec_())

