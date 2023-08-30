import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定主視窗標題
        self.setWindowTitle("表格圖示範例")

        # 建立一個表格檢視表
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 400, 200)

        # 設定表格的行數何列數
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        # 設定表頭標籤
        self.tableWidget.setHorizontalHeaderLabels(["列1", "列2", "列3"])

        # 添加數據到表格單原格
        data = [["A1", "B1", "C1"],
                ["A2", "B2", "C2"],
                ["A3", "B3", "C3"]]

        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(data[i][j])
                self.tableWidget.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

