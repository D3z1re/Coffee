import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QTableWidgetItem
from style import Ui_MainWindow
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.con = sqlite3.connect('coffee.db')
        cur = self.con.cursor()

        n = int(cur.execute('''SELECT Count(*) FROM coffee_types''').fetchone()[0])

        self.tableWidget.setRowCount(n)
        for i in range(n):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(cur.execute('''
                SELECT * FROM coffee_types WHERE ID = ?''', (i + 1, )).fetchone()[j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
