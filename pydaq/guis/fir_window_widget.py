from PySide6.QtWidgets import QFileDialog, QWidget
from ..uis.ui_PYDAQ_FIR_widget import Ui_FIR_window

class FirWindow(QWidget, Ui_FIR_window): # Call the FirWindow widget
    def __init__(self):
        super(FirWindow, self).__init__()
        self.setupUi(self)

        #signals
        self.save_fir_button.released.connect(self.save_fir_and_close)
    
    def save_fir_and_close(self):
        
        self.numtaps = self.numtaps_line.text()
        self.fs = self.fs_combo.text()
        
        self.saved_numtaps = self.numtaps
        self.saved_fs = self.fs
    
        # Fechar a janela
        self.close()
        
        
        
        