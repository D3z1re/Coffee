import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QTableWidgetItem
from style import Ui_MainWindow
from PyQt5 import uic
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.con = sqlite3.connect('coffee.db')
        cur = self.con.cursor()

        self.n = int(cur.execute('''SELECT Count(*) FROM coffee_types''').fetchone()[0])

        self.tableWidget.setRowCount(self.n)

        for i in range(self.n):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(cur.execute('''
                SELECT * FROM coffee_types WHERE ID = ?''', (i + 1, )).fetchone()[j])))

        self.add_btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = SecondForm()
        self.second_form.show()


class SecondForm(QWidget):

    def __init__(self):
        super().__init__()

        uic.loadUi('form_style.ui', self)
        self.initUi()

    def initUi(self):
        self.btn.clicked.connect(self.add_coffee)

    def add_coffee(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
