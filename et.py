# Creating a QSpinBox widget in PyQt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox Example")
        self.setGeometry(100, 100, 300, 200)

        # Create a QSpinBox
        self.num_return_spinbox = QSpinBox()
        self.num_return_spinbox.setMinimum(0)
        self.num_return_spinbox.setMaximum(100)
        self.num_return_spinbox.setValue(50)
        self.num_return_spinbox.setSingleStep(5)

        # Add the QSpinBox to the main window
        self.setCentralWidget(self.num_return_spinbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
