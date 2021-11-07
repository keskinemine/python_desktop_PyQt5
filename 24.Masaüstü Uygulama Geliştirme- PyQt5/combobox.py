from PyQt5 import QtWidgets
import sys
from comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        combo = self.ui.cbSehirler
        
        # combo.addItem('Ankara')
        # combo.addItem('Istanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana', 'İzmir', 'Rize'])
        
        self.ui.btnLoadItem.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnClear.clicked.connect(self.ClearItems)
        
        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)
        
    def ClearItems(self):
        self.ui.cbSehirler.clear()
        
    def LoadItems(self):
        sehirler = ['Adana', 'İzmir', 'Rize']

        self.ui.cbSehirler.addItems(sehirler)
        
    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        
        
        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))
            
            
    def selectedChangedIndex(self, index):
        print(index)
        
    def selectedChangedText(self, text):
        print(text)



app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())




# pyuic5 combobox.ui -o comboboxForm.py