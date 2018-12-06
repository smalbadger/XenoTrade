'''
Class:      WidgetWithTimer
Author(s):  Sam Badger
Date:       December 6, 2018
Type:       FINAL
Description:
            Making a widget that uses a QTimer to update itself.
'''
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal

from PySide2.QtCore import QTimer

from math import floor

class WidgetWithTimer(QGroupBox):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.label = QLabel("00:00:00.000")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)
        
        self._updateTimer = QTimer()
        self._updateTimer.timeout.connect(self.updateLabel)
        self._updateTimer.start(1)
      
    def updateLabel(self):
        self.counter += 1
        ms = self.counter % 1000
        s = floor(((self.counter - ms) / 1000) % 60)
        m = floor(((self.counter - ms - s*1000) / 60000) % 60)
        h = floor((self.counter - ms - s*1000 - m*60000) / 3600000) 
        self.label.setText("{}:{}:{}.{}".format(h, m, s, ms))
        

        
if __name__ == "__main__":
    # imports 
    from PySide2.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    widget = WidgetWithTimer()
    widget.show()
    sys.exit(app.exec_())
