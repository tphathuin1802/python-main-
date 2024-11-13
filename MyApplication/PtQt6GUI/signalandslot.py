import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget


class MainWindow(QWidget):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.setWindowTitle("QT signal and slot")

        button = QPushButton("click me")
        button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        self.show()

    def button_clicked(self):
        print("clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
