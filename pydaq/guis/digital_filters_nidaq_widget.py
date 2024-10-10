import nidaqmx
import os
import matplotlib.pyplot as plt
import numpy as np

from ..uis.ui_PYDAQ_Digital_filterss_NIDAQ_widget import Ui_Digitalfilters_NIDAQ_widget
# from ..uis.ui_PYDAQ_FIR_widget import Ui_FIR_window
# from ..uis.ui_PYDAQ_IIR_widget import Ui_IIR_window
from ..guis.fir_window_widget import FirWindow
from ..guis.iir_window_widget import IrrWindow
from PySide6.QtWidgets import QFileDialog, QWidget


from ..get_data import GetData
from .error_window_gui import Error_window
from pydaq.utils.signals import GuiSignals

class Digital_Filters_NIDAQ_Widget(QWidget, Ui_Digitalfilters_NIDAQ_widget):
    def __init__(self, *args):
        super(Digital_Filters_NIDAQ_Widget, self).__init__()
        self.setupUi(self)
        self.signals = GuiSignals()
        
        self._nidaq_info()
        
        try:
            chan = nidaqmx.system.device.Device(
                self.device_names[0]
            ).ai_physical_chans.channel_names
            defchan = chan[0]

        except BaseException:
            chan = ""
            defchan = ""
            
       
        # Gathering nidaq info
        self.device_combo.addItems(self.device_type)
        self.channel_combo.addItems(chan)
        self.terminal_combo.addItems(["Diff", "RSE", "NRSE"])
        
        defchan_index = self.channel_combo.findText(defchan)

        if defchan_index == -1:
            pass
        else:
            self.channel_combo.setCurrentIndex(defchan_index)
            
        self.path_line.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        )
        
        # Signals 
        self.type_filter.currentTextChanged.connect(self.check_filter)
        
        self.fir_window = None
        self.iir_window = None
        
        self.filter_button.clicked.connect(self.start_func_get_data)
        self.browse_button.clicked.connect(self.locate_path)
        self.device_combo.currentIndexChanged.connect(self.update_channels)
        #self.fr_button.clicked.connect(self.check)
        self.signals.returned.connect(self.frequency_response)
        
        
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
            
    def locate_path(self):  # Calling the Folder Browser Widget
        output_folder_path = QFileDialog.getExistingDirectory(
            self, caption="Choose a folder to save the data file"
        )
        if output_folder_path == "":
            pass
        else:
            self.path_line.setText(output_folder_path.replace("/", "\\"))

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
       
                
    def check_filter(self, text):
        if text == 'FIR':
            self.ShowFirWindow()
        if text == 'IIR':
            self.ShowIrrWindow()
    
    def ShowFirWindow(self):
        # Open FIR window
        if self.fir_window is None:
            self.fir_window = FirWindow()
        self.fir_window.show()
        
    def ShowIrrWindow(self):
        # Open IIR window
        if self.iir_window is None:
            self.iir_window = IrrWindow()
        self.iir_window.show()
        
    def start_func_get_data(self):  # Start getting data
        try:
            # Instantiating the GetData class
            g = GetData()

            # Separating variables
            g.device = self.channel_combo.currentText().split("/")[0]
            g.channel = self.channel_combo.currentText().split("/")[1]
            g.terminal = g.term_map[self.terminal_combo.currentText()]
            g.ts = self.sample_line.value()
            g.session_duration = self.session_line.value()
            g.plot = True if self.ratio_plot.checkedId() == -2 else False
            g.save = True if self.ratio_save.checkedId() == -2 else False
            g.path = self.path_line.text()

            # Checking if a path was set
            if self.path_line.text() == "":
                raise BaseException

            # Restarting variables
            g.data = []
            g.time_var = []
            g.error_path = False
            
    
        except BaseException:
            error_w = Error_window()
            error_w.exec()
            g.error_path = True

        if not g.error_path:
            # Calling data aquisition method
            g.get_data_nidaq()
            self.signals.returned.emit(g)
            
    def frequency_response(self):
        if self.yes_fr.isChecked():
            # open the data.dat and time.dat and make the fft
            self.time_way = self.path_line.text() + '\\' + 'time.dat'
            self.data_way = self.path_line.text() + '\\' + 'data.dat'
            
            # load the archive
            self.time = np.loadtxt(self.time_way)
            self.data = np.loadtxt(self.data_way)
            
            # tests
            self.T = np.mean(np.diff(self.time))
            self.Fs = 1/self.T 
            
            self.N = len(self.data)
            
            self.fft_sinal = np.fft.fft(self.data)
            self.fft_sinal = np.abs(self.fft_sinal[:self.N//2])
            self.freqs = np.fft.fftfreq(self.N, self.T)[:self.N//2]
            
            plt.figure()
            plt.plot(self.freqs, self.fft_sinal)
            #plt.plot(self.time, self.data)
            plt.xlabel('Frequency [Hz]')
            plt.ylabel('Amplitude')
            plt.title('Frequency Response')
            plt.grid()
            plt.show()
            
        else:
            return
    
            

