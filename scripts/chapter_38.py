import numpy as np
# Simulated 50-Hz sensor waveform sampled at 1000 Hz.
fs=1000
x=np.arange(fs)/fs
signal=np.sin(2*np.pi*50*x)+0.3*np.sin(2*np.pi*120*x)
frequency=np.fft.rfftfreq(len(signal),d=1/fs)
power=np.abs(np.fft.rfft(signal))
top=np.argsort(power)[-2:]
print('Dominant frequencies (Hz):',sorted(frequency[top].astype(int).tolist()))
print('Window duration (s):',round(len(signal)/fs,3))
