import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class LineChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("折线图示例")

        # 创建 Matplotlib Figure 对象
        self.figure, self.ax = plt.subplots()

        # 创建 Matplotlib Canvas 对象，并将 Figure 放入其中
        self.canvas = FigureCanvas(self.figure)

        # 创建 Widget 以容纳 Canvas
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 创建布局管理器
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.canvas)

        # 创建折线数据
        x = [1, 2, 3, 4]
        y = [3, 4, 2, 6]

        # 绘制折线图
        self.ax.plot(x, y, marker='o')

        # 设置横轴和纵轴标签
        self.ax.set_xlabel('X轴')
        self.ax.set_ylabel('Y轴')

        # 显示图表
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineChartWindow()
    window.show()
    sys.exit(app.exec_())

