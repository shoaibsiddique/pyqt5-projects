import serial, serial.tools.list_ports
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from threading import Thread, Event

class Function_UI(QObject):
    data_available = pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.serialPort = serial.Serial()
        self.serialPort.timeout = 0.5

        self.baudList = {
            '4800':4800,
            '9600':9600,
            '19200':19200,
            '38400':38400,
            '115200':115200
        }
        self.portList = []
        self.thread = None
        self.alive = Event()

    def update_port(self):
        self.portList = [port.device for port in serial.tools.list_ports.comports()]
        print(self.portList)

    def update_portInfo_allPorts(self):
        self.portList = []
        for port in serial.tools.list_ports.comports():
            port_info = {
                'device': port.device,
                'description': port.description,
                'manufacturer': port.manufacturer,
                'product': port.product,
                'vid': port.vid,
                'pid': port.pid
            }
            self.portList.append(port_info)
        selected_port = self.portList[1]  # Change the index as needed

        for port_info in self.portList:
            print("Port Information:")
            for key, value in port_info.items():
                print(f"{key}: {value}")
            print()

    def update_portInfo(self):
        self.portList = []
        for port in serial.tools.list_ports.comports():
            port_info = {
                'device': port.device,
                'description': port.description,
                'manufacturer': port.manufacturer,
                'product': port.product,
                'vid': port.vid,
                'pid': port.pid
            }
            self.portList.append(port_info)
        
        selected_port = self.portList[1]  # Change the index as needed
        
        for key, value in selected_port.items():
            print(f"{key}: {value}")

        
    def connect_serial(self):
        try:
            self.serialPort.open()
            if(self.serialPort.is_open):
                self.start_thread()
                print("Successful connection")
        except:
            print('Unable to connect')
    
    def disconnect_serial(self):
        self.stop_thread()
        self.serialPort.close()

    def read_serial(self):
        while (self.alive.isSet() and self.serialPort.is_open):
            data = self.serialPort.readline().decode("utf-8").strip()
            if(len(data)>1):
                self.data_available.emit(data)
            print(data)
    
    def send_data(self, data):
        if(self.serialPort.is_open):
            messages = str(data) + "\n"
            self.serialPort.write(messages.encode())


    def start_thread(self):
        self.thread = Thread(target = self.read_serial)
        self.thread.setDaemon(1)
        self.alive.set()
        self.thread.start()
    
    def stop_thread(self):
        if(self.thread is not None):
            self.alive.clear()
            self.thread.join()
            self.thread = None
