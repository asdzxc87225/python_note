import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  # 添加导入语句
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class InteractiveChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定視窗標題
        self.setWindowTitle("互動式折線圖")

        # 建立 Matplotlib Figure 對象
        self.figure, self.ax = plt.subplots()

        # 建立 Matplotlib Canvas 對象，並將 Figure 放入其中
        self.canvas = FigureCanvas(self.figure)

        # 建立 widget 以容納 Canvas
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 建立排版管理器
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.canvas)

        # 啟用 Matplotlib 的引導工具欄
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)

        # 建立數據
        x = [1, 2, 3, 4, 5]
        y = [3, 4, 2, 6, 5]

        # 繪製折線圖
        self.ax.plot(x, y, marker='o')

        # 設置橫軸與縱軸的標籤
        self.ax.set_xlabel('X轴')
        self.ax.set_ylabel('Y轴')

        # 顯示圖表
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveChartWindow()
    window.show()
    sys.exit(app.exec_())

