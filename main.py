from lzma import CHECK_SHA256
from PyQt6 import QtCore, QtGui, QtWidgets
from Gui import Ui_MainWindow
from PyQt6.QtGui import QPalette, QColor
import sys


SHOW_FULLSCREEN = False

_translate = QtCore.QCoreApplication.translate


CHANNEL_MAP = {  # The starting coordinates of each channel
    1: {'x': 0, 'y': 0},
    2: {'x': 120, 'y': 0},
    3: {'x': 240, 'y': 0},
    4: {'x': 360, 'y': 0},
    5: {'x': 480, 'y': 0},
    6: {'x': 0, 'y': 96},
    7: {'x': 120, 'y': 96},
    8: {'x': 240, 'y': 96},
    9: {'x': 360, 'y': 96},
    10: {'x': 480, 'y': 96},
    11: {'x': 0, 'y': 192},
    12: {'x': 120, 'y': 192},
    13: {'x': 240, 'y': 192},
    14: {'x': 360, 'y': 192},
    15: {'x': 480, 'y': 192},
    16: {'x': 0, 'y': 288},
    17: {'x': 120, 'y': 288},
    18: {'x': 240, 'y': 288},
    19: {'x': 360, 'y': 288},
    20: {'x': 480, 'y': 288},
}

_translate = QtCore.QCoreApplication.translate

class Channel(QtWidgets.QWidget):
    def __init__(self, channel, text):
        super(Channel, self).__init__()
        self.channel = channel
        self.text = text
        self.status = "Off"
        self.amps = 0.00
        self.channelLabel = QtWidgets.QLabel("Ch:")
        self.channelLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignRight)

        self.channelValue = QtWidgets.QLabel(str(self.channel))
        self.channelName = QtWidgets.QLabel(self.text)
        

        
        self.row1 = QtWidgets.QWidget()
        self.row1Layout = QtWidgets.QHBoxLayout()
        self.row1Layout.setSpacing(0)
        self.row1Layout.setContentsMargins(0, 0, 0, 0)
        self.row1Layout.addWidget(self.channelLabel, 0)
        self.row1Layout.addWidget(self.channelValue, 1)
        self.row1Layout.addWidget(self.channelName, 2)
        self.row1.setLayout(self.row1Layout)
        
        self.row2 = QtWidgets.QWidget()
        self.row2Layout = QtWidgets.QHBoxLayout()
        self.row2Layout.setSpacing(0)
        self.row2Layout.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QtWidgets.QLabel("Status:")
        self.statusValue = QtWidgets.QLabel(self.status)
        self.row2Layout.addWidget(self.statusLabel, 0)
        self.row2Layout.addWidget(self.statusValue, 1)
        self.row2.setLayout(self.row2Layout)
        
        self.row3 = QtWidgets.QWidget()
        self.row3Layout = QtWidgets.QHBoxLayout()
        self.row3Layout.setSpacing(0)
        self.row3Layout.setContentsMargins(0, 0, 0, 0)
        self.ampsLabel = QtWidgets.QLabel("Amps:")
        self.ampsValue  = QtWidgets.QLabel(str(self.amps))
        self.row3Layout.addWidget(self.ampsLabel, 0)
        self.row3Layout.addWidget(self.ampsValue, 1)
        self.row3.setLayout(self.row3Layout)
        
        self.setStyleSheet("border: 1px solid rgb(255,40,40);")
        
    
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.row1, 0)
        self.layout.addWidget(self.row2, 1)
        self.layout.addWidget(self.row3, 2)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(5,5,5,5)
        self.setLayout(self.layout)
        self.Button = QtWidgets.QPushButton()
        self.Button.setParent(self)
        self.Button.setCheckable(True)
        self.Button.clicked.connect(self.buttonPressed)
        
    def buttonPressed(self):
        print("Button pressed on channel {}".format(self.channel))
        # If checked set color to green, otherwise set color to red
        if self.Button.isChecked():
            self.setStyleSheet("border: 1px solid rgb(40,255,40);")
            self.status = "On"   
        else:
            self.setStyleSheet("border: 1px solid rgb(255,40,40);")
            self.status = "Off"
        self.redraw()
            
            
    def redraw(self):
        self.channelValue.setText(str(self.channel))
        self.channelName.setText(self.text)
        self.statusValue.setText(self.status)
        self.ampsValue.setText(str(self.amps))
        self.update()
        
    def setAmps(self, amps):
        self.amps = amps
        self.redraw()
            




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    layout = QtWidgets.QGridLayout()
    layout.setSpacing(0)
    layout.addWidget(Channel("1", "Channel 1"), 0, 0)
    layout.addWidget(Channel("2", "Channel 2"), 0, 1)
    layout.addWidget(Channel("3", "Channel 3"), 0, 2)
    layout.addWidget(Channel("4", "Channel 4"), 0, 3)
    layout.addWidget(Channel("5", "Channel 5"), 0, 4)
    layout.addWidget(Channel("6", "Channel 6"), 1, 0)
    layout.addWidget(Channel("7", "Channel 7"), 1, 1)
    layout.addWidget(Channel("8", "Channel 8"), 1, 2)
    layout.addWidget(Channel("9", "Channel 9"), 1, 3)
    layout.addWidget(Channel("10", "Channel 10"), 1, 4)
    layout.addWidget(Channel("11", "Channel 11"), 2, 0)
    layout.addWidget(Channel("12", "Channel 12"), 2, 1)
    layout.addWidget(Channel("13", "Channel 13"), 2, 2)
    layout.addWidget(Channel("14", "Channel 14"), 2, 3)
    layout.addWidget(Channel("15", "Channel 15"), 2, 4)
    layout.addWidget(Channel("16", "Channel 16"), 3, 0)
    layout.addWidget(Channel("17", "Channel 17"), 3, 1)
    layout.addWidget(Channel("18", "Channel 18"), 3, 2)
    layout.addWidget(Channel("19", "Channel 19"), 3, 3)
    layout.addWidget(Channel("20", "Channel 20"), 3, 4)
    
    
    # widget.setLayout(layout)
    # MainWindow.setCentralWidget(widget)
    ui.Buttons.setLayout(layout)
    

    
    # ch1 = Channel("Grill", 1, ui.Button_Ch_1, ui.Background_Ch_1, ui.Channel_Name_Ch_1, ui.Status_Value_Ch_1, ui.Amps_Value_Ch_1)

    if SHOW_FULLSCREEN:
        MainWindow.showFullScreen()

    else:
        MainWindow.show()

    sys.exit(app.exec())
