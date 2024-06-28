import sys
import PyQt5


from PyQt5.QtWidgets import QMainWindow, QApplication
from py_files.StartWindow import Ui_MainWindow

from py_files import FirstLevel, SecondLevel


class StartWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_start.clicked.connect(self.start_game)
        self.btn_exit.clicked.connect(self.close_game)

    def start_game(self):
        if self.btn_change_level.currentText() == "1 уровень":
            self.close()
            FirstLevel.main()

        if self.btn_change_level.currentText() == "2 уровень":
            self.close()
            SecondLevel.main()

    def close_game(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec())
