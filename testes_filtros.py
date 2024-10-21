import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz

time_way = "C:\\Users\\55319\\Desktop\\testes\\time.dat"
data_way = "C:\\Users\\55319\\Desktop\\testes\\data.dat"

# originais
time = np.loadtxt(time_way)
data = np.loadtxt(data_way)

numtaps = 9
cutoff = 0.1
fs = 1/np.mean(np.diff(time))

fir_coeff = firwin(numtaps, cutoff, window='hamming', fs=fs)
filtered_signal = lfilter(fir_coeff, 1.0, data)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(time, data, label = 'Sinal original')
plt.title('Sinal Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2,1,2)
plt.plot(time, filtered_signal, label='Sinal Filtrado', color='r')
plt.grid()

plt.tight_layout()
plt.show()