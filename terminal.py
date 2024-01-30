from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QLineEdit, QPushButton, QLabel
import subprocess
import os

class Terminal(QWidget):
    def __init__(self):
        super().__init__()
        self.working_dir = os.getcwd()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('STerminal')
        self.setGeometry(100, 100, 500, 500)

        # Create widgets
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.input = QLineEdit()
        self.button = QPushButton('Run')
        self.path = QLabel()
        self.path.setText(self.working_dir)

        # Create layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.output)
        hbox = QHBoxLayout()
        hbox.addWidget(self.path)
        hbox.addWidget(self.input)
        hbox.addWidget(self.button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # Connect button to function
        self.button.clicked.connect(self.run)
        self.input.returnPressed.connect(self.run)
    
    def renderWorkingDir(self):
        dirs = self.working_dir.split('/')
        while len(dirs) > 1 and dirs[-1] == '..':
            dirs.pop()
            dirs.pop()
        self.working_dir = '/'.join(dirs)
        if self.working_dir == '':
            self.working_dir = '/'
        self.path.setText(self.working_dir)
    
    def runCMD(self, cmd):
        if "cd " in cmd:
            targetDir = cmd.split(" ")[1]
            if targetDir[0] != "/":
                targetDir = self.working_dir + "/" + targetDir
            try:
                subprocess.call(cmd, shell=True, cwd=targetDir)
                self.working_dir = targetDir
                self.renderWorkingDir()
                return ''
            except Exception as e:
                return str(e)
        else:
            try:
                result = subprocess.check_output(cmd, shell=True, cwd=self.working_dir)
                return result.decode("utf-8")
            except subprocess.CalledProcessError as e:
                return str(e)

    def run(self):
        cmd = self.input.text()
        self.input.clear()

        res = self.runCMD(cmd)
        self.append_text(cmd)
        self.append_text(res if res else '\n')

    def append_text(self, text):
        self.output.appendPlainText(text)
