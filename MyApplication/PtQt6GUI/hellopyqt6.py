from PyQt6.QtWidgets import QApplication, QWidget

# tạo đối tượng Qapplication
app = QApplication([])
# tạo cửa sổ chính

window = QWidget(windowTitle="hello pyqt6")
window.show()

app.exec()
