from ..uis.ui_PYDAQ_Digital_filters_widget import Ui_Digitalfilters_arduino_widget
from PySide6.QtWidgets import QFileDialog, QWidget
import serial

class Digital_Filters_Arduino_Widget(QWidget, Ui_Digitalfilters_arduino_widget):
    def __init__(self, *args):
        super(Digital_Filters_Arduino_Widget, self).__init__()
        self.setupUi(self)
        self.filter_combox.currentTextChanged.connect(self.update_filter)
        self.update_filter(self.filter_combox.currentText())
        self.reload_devices.clicked.connect(self.update_com_ports)
        
        # setting starting values
        self.update_com_ports()
        
    
    # function that show and hide fir or iir widgets    
    def update_filter(self, text):
        if text == 'FIR':
            self.fir_configs.show()
            self.iir_configs.hide()
        else:
            self.iir_configs.show()
            self.fir_configs.hide()
            
                
    def update_com_ports(self):  # Updating com ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        selected = self.arduino_board.currentText()

        self.arduino_board.clear()
        self.arduino_board.addItems(self.com_ports)
        index_current = self.arduino_board.findText(selected)

        if index_current == -1:
            pass
        else:
            self.arduino_board.setCurrentIndex(index_current)