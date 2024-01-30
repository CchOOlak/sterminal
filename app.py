from PyQt5.QtWidgets import QApplication
from terminal import Terminal
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    terminal = Terminal()
    terminal.show()
    sys.exit(app.exec_())