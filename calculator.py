import sys
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'SIMPLE CALCULATOR'
        self.left = 400
        self.top = 200
        self.width = 400
        self.height = 300
        self.sum = 0
        self.dif = 0
        self.mul = 0
        self.div = 0
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Create Label 1
        self.label1 = QLabel(self)
        self.label1.setText("first number : ")
        self.label1.move(20,20)

        # Create textbox 1
        self.firstNum = QLineEdit(self)
        self.firstNum.move(100, 20)
        self.firstNum.resize(200, 20)

        # Create Label 2
        self.label2 = QLabel(self)
        self.label2.setText("second number : ")
        self.label2.move(20, 50)

        # Create textbox 2
        self.secNum = QLineEdit(self)
        self.secNum.move(100, 50)
        self.secNum.resize(200, 20)

        # Create a button in the window
        self.button = QPushButton('CALCULATE', self)
        self.button.move(100, 100)

        # Create ResultLabel add
        self.add_result = QLabel(self)
        #self.add_result.setText("Sum = %d"%self.sum)
        self.add_result.move(20, 150)

        # Create ResultLabel difference
        self.dif_result = QLabel(self)
        self.dif_result.move(20, 170)

        # Create ResultLabel product
        self.mul_result = QLabel(self)
        self.mul_result.move(20, 190)

        # Create ResultLabel division
        self.div_result = QLabel(self)
        self.div_result.move(20, 210)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()


    #@pyqtSlot()
    def on_click(self):
        if  (self.firstNum.text() and self.secNum.text()):
            fNum = float(self.firstNum.text())
            sNum = float(self.secNum.text())
            self.sum = fNum + sNum
            self.dif = fNum - sNum
            self.mul = fNum * sNum
            self.div = fNum / sNum
            self.add_result.setText("addition\t  : %.2f"%self.sum)
            self.dif_result.setText("subtraction : %.2f"%self.dif)
            self.mul_result.setText("product\t  : %.2f"%self.mul)
            self.div_result.setText("Quotient\t  : %.2f"%self.div)

        else:
            QMessageBox.question(self, 'Error!', "Please, Enter the numbers first!!!" , QMessageBox.Ok,QMessageBox.Ok)


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())