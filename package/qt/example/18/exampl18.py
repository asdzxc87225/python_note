import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QPropertyAnimation

class MyWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        # 创建图形场景
        scene = QGraphicsScene(self)
        self.setScene(scene)

        # 创建一个圆形图形项
        circle = QGraphicsEllipseItem(0, 0, 50, 50)
        circle.setBrush(Qt.blue)  # 设置圆形颜色
        scene.addItem(circle)

        # 创建动画
        animation = QPropertyAnimation(circle, b'pos')
        animation.setDuration(2000)  # 动画持续时间（2秒）
        animation.setStartValue(circle.pos())  # 动画起始位置
        animation.setEndValue(circle.pos() + Qt.QPoint(200, 0))  # 动画结束位置

        # 开始动画
        animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

