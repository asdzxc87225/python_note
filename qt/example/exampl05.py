import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定主視窗標題
        self.setWindowTitle("菜單欄與工具欄的範例")


        # 創見問建菜單選項
        new_action = QAction("新建", self)
        open_action = QAction("打开", self)
        save_action = QAction("保存", self)
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)

        # 建立菜單欄
        menubar = self.menuBar()
        # 建立文件菜單
        file_menu = menubar.addMenu("文件")
        # 將菜單選項添加到文件菜單

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # 建立工具欄
        toolbar = QToolBar("工具欄")
        self.addToolBar(toolbar)

        # 在工具欄上添加工具按鈕
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

