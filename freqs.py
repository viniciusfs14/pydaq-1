import numpy as np
from scipy.fft import fft, fftfreq

time_way = "C:\\Users\\55319\\Desktop\\testes\\time.dat"
data_way = "C:\\Users\\55319\\Desktop\\testes\\data.dat"

# originais
time = np.loadtxt(time_way)
data = np.loadtxt(data_way)

ts = 1000

# Número de amostras
N = len(data)

# Aplica FFT ao sinal
fft_result = fft(data)

# Frequências correspondentes
freqs = fftfreq(N, 1/ts)

# Pegando apenas a metade positiva do espectro
freqs = freqs[:N//2]
magnitudes = np.abs(fft_result[:N//2])

dominant_frequencys = np.mean(freqs)
# Exibe as frequências e magnitudes
print("Frequências:", dominant_frequencys)

