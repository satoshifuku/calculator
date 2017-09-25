# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtGui, QtWidgets, QtCore


class My_calculator(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.names = ['A/C', '+/-', '%', '/',
                      '7', '8', '9', '*',
                      '4', '5', '6', '-',
                      '1', '2', '3', '+',
                      '0', ' ', '.', '=']
        self.position_leidter = (0, 0, 1 ,4)
        self.positions = [(i,j) for i in range(1,6) for j in range(4)]
        self.setWindowTitle('Calculator')
        self.set_body()

    def set_body(self):
        '''
        set a line eiter and buttions on a gridlayout.
        The line editer is used to show a number.
        '''
        # create instance for grid layout
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.editer = QtWidgets.QLineEdit('0')
        self.editer.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.editer.setReadOnly(True)
        # set line editer from (0, 0) to (0, 4) in teh gridlayout
        self.grid.addWidget(self.editer, *self.position_leidter)

        self.buttons = []
        self.temp_number = 0

        for position, name in zip(self.positions, self.names):

            # create button with name
            self.buttons.append(QtWidgets.QPushButton(name))

            # set button on the postion in the gridlayout
            self.grid.addWidget(self.buttons[-1], *position)

            # connect an click to a function named changeText.
            # changeText  can change text in line editer
            self.buttons[-1].clicked.connect(self.changeText)


    def changeText(self):
        sending_button = self.sender()
        name = sending_button.text()
        # Search name in line editor which exists in a list .
        if name in [str(i) for i in range(10)]:
            num = int(self.editer.text()+name)
            self.editer.setText(str(num))
        else:
            self.temp_number = int(self.editer.text())
            print(self.temp_number)
            if name == self.names[0]:
                self.editer.clear()
                self.temp_number = 0
                self.editer.setText('0')


def main():

    app = QtWidgets.QApplication(sys.argv)
    calc = My_calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
