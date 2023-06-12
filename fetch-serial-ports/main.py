import imp
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from serialgui import Ui_Form
from function import Function_UI
import serial, serial.tools.list_ports

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_Form()
        self.uic.setupUi(self.main_win)

        self.serial = Function_UI()
        self.serialPort = serial.Serial()

        self.uic.baud_List.addItems(self.serial.baudList)
        self.uic.baud_List.setCurrentText('9600')
        #self.update_ports()
        self.uic.connect_Button.clicked.connect(self.connect_serial)
        self.uic.refresh_Button.clicked.connect(self.update_ports)
        #self.uic.connect_Button.clicked.connect(self.update_portsInfoAll)
    

    def connect_serial(self):
        if(self.uic.connect_Button.isChecked()):
            port = self.uic.port_List.currentText()
            baud = self.uic.baud_List.currentText()
            #print(update_portInfo(port))
            self.serial.serialPort.port = port
            self.serial.serialPort.baudrate = baud
            self.serial.connect_serial()
            if(self.serial.serialPort.is_open):
                self.uic.connect_Button.setText("Disconnect")
        else:
            self.serial.disconnect_serial()
            self.uic.connect_Button.setText("Connect")
    

    def update_ports(self):
        self.serial.update_port()
        self.uic.port_List.clear()
        self.uic.port_List.addItems(self.serial.portList)
        #self.serial.update_portInfo_allPorts()
        self.serial.update_portInfo_allPorts()
        self.uic.portinfo_field.clear()
        self.uic.portinfo_field.setText(str(self.serial.portList))
        #self.serial.connect_serial()


    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())