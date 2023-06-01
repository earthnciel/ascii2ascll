import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("My TEST v1.0")
        self.setWindowIcon(QIcon("icon.png"))

        # StatusBar
        self.statusbar = QStatusBar(self)          # QStatusBar 객체 생성
        self.setStatusBar(self.statusbar)          # 위젯 배치
        self.statusbar.showMessage("TEST v1.0")

        # label
        self.label = QLabel("메시지: ", self)
        self.label.move(10, 10)

        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(50, 10)

        btn = QPushButton(text="버튼", parent=self)
        btn.clicked.connect(self.buy)
        btn.move(50, 50)
        btn.resize(200, 30)

        btn1 = QPushButton("Quit", self)
        btn1.move(100, 100)
        btn1.clicked.connect(self.btn_clicked)
        btn1.resize(100, 30)

    def buy(self):
        print("버튼 클릭")

    def btn_clicked(self):
        QApplication.instance().quit()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
