import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
class MainWindow(QWidget):
    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)

        #Đặt tiêu đề cho cửa sổ:
        self.setWindowTitle("Hello Python")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #tạo cửa sổ chính
    window = MainWindow()

    #execute vòng lặp:
    sys.exit(app.exec())