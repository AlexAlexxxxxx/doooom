import sys

from PyQt5.QtWidgets import QWidget, QApplication
from EndWindow import Ui_Form

from py_files import SecondLevel


class EndWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lbl_hp.setText(SecondLevel.hero_hp)
        self.lbl_xp.setText(SecondLevel.hero_xp)
        self.lbl_time.setText(SecondLevel.time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    end_window = EndWindow()
    end_window.show()
    sys.exit(app.exec())
