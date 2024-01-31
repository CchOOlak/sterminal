from PyQt5.QtWidgets import QApplication
from terminal import Terminal
from tcpsock import TCPSockServer
import sys

if __name__ == '__main__':
    tcp_server = TCPSockServer('localhost',8585)
    tcp_server.start()

    app = QApplication(sys.argv)
    terminal = Terminal('localhost', 8585)
    try:
        terminal.show()
        sys.exit(app.exec_())
    except:
        tcp_server.close()