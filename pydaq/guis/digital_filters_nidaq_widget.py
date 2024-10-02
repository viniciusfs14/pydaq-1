from ..uis.ui_PYDAQ_Digital_filterss_NIDAQ_widget import Ui_Digitalfilters_NIDAQ_widget
from ..uis.ui_PYDAQ_FIR_widget import Ui_FIR_window
from ..uis.ui_PYDAQ_IIR_widget import Ui_IIR_window
from PySide6.QtWidgets import QFileDialog, QWidget
import nidaqmx
import numpy as np


class Digital_Filters_NIDAQ_Widget(QWidget, Ui_Digitalfilters_NIDAQ_widget):
    def __init__(self, *args):
        super(Digital_Filters_NIDAQ_Widget, self).__init__()
        self.setupUi(self)
        
        self.type_filter.currentTextChanged.connect(self.check_filter)
        self.fir_window = None
        self.iir_window = None
        # Gathering nidaq info
        self._nidaq_info()
        
        try:
            chan = nidaqmx.system.device.Device(
                self.device_names[0]
            ).ai_physical_chans.channel_names
            defchan = chan[0]

        except BaseException:
            chan = ""
            defchan = ""
            
        
        self.device_combo.addItems(self.device_type)
        self.channel_combo.addItems(chan)
        self.terminal_combo.addItems(["Diff", "RSE", "NRSE"])
        
        
    def _nidaq_info(self):
        """Gathering NIDAQ info"""

        # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()

        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

    def update_channels(self):
        # Changing availables channels if device changes
        new_ai_channels = nidaqmx.system.device.Device(
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ai_physical_chans.channel_names

        # Default channel
        try:
            default_channel = new_ai_channels[0]
        except BaseException:
            default_channel = "There is no analog input in this board"

        # Rewriting new ai channels into the right place
        self.channel_combo.clear()
        self.channel_combo.addItems(new_ai_channels)
        defchan_index = self.channel_combo.findText(default_channel)

        if defchan_index == -1:
            pass
        else:
            self.channel_combo.setCurrentIndex(defchan_index)

    def reload_devices_handler(self):
        """Updates the devices combo box"""
        self._nidaq_info()

        # If the signal is not disconnect, it will run into a warning
        self.device_combo.currentIndexChanged.disconnect(self.update_channels)

        # Updating items on combo box
        self.device_combo.clear()
        self.device_combo.addItems(self.device_type)

        # Reconnecting the signal
        self.device_combo.currentIndexChanged.connect(self.update_channels)        
                
    def check_filter(self, text):
        if text == 'FIR':
            self.ShowFirWindow()
        if text == 'IIR':
            self.ShowIrrWindow()
    
    def ShowFirWindow(self):
        if self.fir_window is None:
            self.fir_window = FirWindow()
        self.fir_window.show()
        
    def ShowIrrWindow(self):
        if self.iir_window is None:
            self.iir_window = IrrWindow()
        self.iir_window.show()
class FirWindow(QWidget, Ui_FIR_window):
    def __init__(self):
        super(FirWindow, self).__init__()
        self.setupUi(self)
        self.close_fir_button.clicked.connect(self.close)
        
class IrrWindow(QWidget, Ui_IIR_window):
    def __init__(self):
        super(IrrWindow, self).__init__()
        self.setupUi(self)
        self.close_iir_button.clicked.connect(self.close)
        
        