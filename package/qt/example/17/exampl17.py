import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("图像处理应用")
        self.setGeometry(100, 100, 800, 600)

        # 创建标签用于显示图像
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # 创建主布局
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        # 创建主窗口的中央部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 加载图像并进行处理
        self.load_and_process_image()

    def load_and_process_image(self):
        # 加载图像
        image = cv2.imread("your_image.jpg")

        # 在这里进行图像处理，例如转换颜色、滤波、边缘检测等
        # 这里只是一个示例，您可以根据需要添加其他处理步骤
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 将OpenCV图像转换为Qt图像
        h, w = processed_image.shape
        q_image = QImage(processed_image.data, w, h, w, QImage.Format_Grayscale8)

        # 创建Qt图像标签
        pixmap = QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessingApp()
    window.show()
    sys.exit(app.exec_())

