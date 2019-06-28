import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class EmbTerminal(QWidget):
    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QProcess(self)
        self.terminal = QWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)
        # Works also with urxvt:
        self.process.start('urxvt',['-embed', str(int(self.winId()))])
        self.setFixedSize(640, 480)


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        central_widget = QWidget()
        lay = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget()
        lay.addWidget(tab_widget)

        tab_widget.addTab(EmbTerminal(), "EmbTerminal")
        tab_widget.addTab(QTextEdit(), "QTextEdit")
        tab_widget.addTab(QMdiArea(), "QMdiArea")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())