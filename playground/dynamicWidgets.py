from PySide2.QtWidgets import QVBoxLayout, QPushButton, QGroupBox, QLineEdit


class MyButton(QGroupBox):
    def __init__(self, text):
        QGroupBox.__init__(self)
        self.pushButton = QPushButton(text)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pushButton)
        self.setLayout(self.layout)

class ButtonList(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.createElements(5)
        self.createLayout()
        self.createActions()
        
    def createElements(self, numElements):
        self.numElements = numElements
        
        self.lineEdit = QLineEdit()
        self.add = QPushButton("Add another button")
        self.widgets = []
        for i in range(self.numElements):
            self.widgets.append(MyButton("button {}".format(i+1)))
    
    def createLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.add)
        for i in range(self.numElements):
            self.layout.addWidget(self.widgets[i])
            
    def createActions(self):
        self.lineEdit.returnPressed.connect(self.update)
        self.add.clicked.connect(self.addButton)
        
    def addButton(self):
        self.widgets[0] = MyButton("New Button")
        #self.widgets.append(MyButton("New Button"))
        self.layout.addWidget(self.widgets[-1])
        #self.numElements += 1
        
    def update(self):
        
        print(self.lineEdit.text())
        n = int(self.lineEdit.text())
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
        self.createElements(n)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.add)
        for i in range(self.numElements):
            self.layout.addWidget(self.widgets[i])
        self.createActions()

if __name__ == "__main__":
    # imports 
    from PySide2.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    widget = ButtonList()
    widget.show()
    
    sys.exit(app.exec_())
