import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import hann, hamming
from scipy.fft import fft
from scipy.stats import ttest_ind


def load_emg_signal(filename):
    data = np.loadtxt(filename)
    return data

def apply_window(signal, window_type='hann'):
    if window_type == 'hann':
        window = hann(len(signal))
    elif window_type == 'hamming':
        window = hamming(len(signal))
    else:
        raise ValueError("Tipo de ventana no soportado")
    return signal * window

def compute_fft(signal, fs):
    N = len(signal)
    freq = np.fft.fftfreq(N, d=1/fs)
    fft_values = np.abs(fft(signal))
    power_spectrum = fft_values ** 2
    return freq[:N//2], fft_values[:N//2], power_spectrum[:N//2]

def analyze_fatigue(freq, power_spectrum):
    peak_freq = freq[np.argmax(power_spectrum)]
    return peak_freq

def process_emg(filename, fs=1000, num_contractions=37):
    emg_signal = load_emg_signal(filename)
    segment_length = len(emg_signal) // num_contractions
    
    peak_frequencies_early = []
    peak_frequencies_late = []
    windows = ['hann', 'hamming']

    for i in range(num_contractions):
        segment = emg_signal[i*segment_length:(i+1)*segment_length]
        windowed_segment = apply_window(segment, 'hann')  
        freq, _, power_spectrum = compute_fft(windowed_segment, fs)
        peak_freq = analyze_fatigue(freq, power_spectrum)

        if i < 5:
            peak_frequencies_early.append(peak_freq)
        elif i >= num_contractions - 5:
            peak_frequencies_late.append(peak_freq)

    plt.figure(figsize=(10, 6))
    plt.plot(emg_signal, label="Señal EMG original")
    plt.title("Señal EMG Completa")
    plt.legend()
    plt.show()

    t_stat, p_value = ttest_ind(peak_frequencies_early, peak_frequencies_late, equal_var=False)

    print("\n===== Análisis de Fatiga Muscular =====")
    print("Hipótesis nula H₀: No hay diferencia significativa en la frecuencia dominante.")
    print("Hipótesis alternativa H₁: Sí hay diferencia significativa (indicio de fatiga).")
    print(f"\nFrecuencias tempranas: {np.round(peak_frequencies_early, 2)}")
    print(f"Frecuencias tardías: {np.round(peak_frequencies_late, 2)}")
    print(f"\nT-Student: t = {t_stat:.4f}, p = {p_value:.4f}")

    if p_value < 0.05:
        print("✅ Se rechaza H₀. Existe evidencia de fatiga muscular (frecuencia disminuye).")
    else:
        print("❌ No se rechaza H₀. No hay evidencia significativa de fatiga.")

txt_filename = r"C:\Users\Usuario\Desktop\Lab4\emg_signal_fatiga_estilo_original.txt"
process_emg(txt_filename)
