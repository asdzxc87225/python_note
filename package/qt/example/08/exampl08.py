import sys
import matplotlib.pyplot as plt

class LineChartWindow:
    def __init__(self):
        # 创建窗口
        self.figure, self.ax = plt.subplots()

        # 设置窗口标题
        self.figure.canvas.setWindowTitle("折线图示例")

        # 创建折线数据
        x = [1, 2, 3, 4]
        y = [3, 4, 2, 6]

        # 绘制折线图
        self.ax.plot(x, y, marker='o')

        # 设置横轴和纵轴标签
        self.ax.set_xlabel('X轴')
        self.ax.set_ylabel('Y轴')

        # 显示图表
        plt.show()

if __name__ == "__main__":
    app = LineChartWindow()
    sys.exit(app.exec_())

