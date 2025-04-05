import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import hann,hamming
from scipy.signal import fftconvolve
from scipy.fft import fft



def load_emg_signal(filename):
    """Carga la señal EMG desde un archivo de texto."""
    data = np.loadtxt(filename)
    return data

def apply_window(signal, window_type='hann'):
    """Aplica una ventana a la señal EMG."""
    if window_type == 'hann':
        window = hann(len(signal))
    elif window_type == 'hamming':
        window = hamming(len(signal))
    else:
        raise ValueError("Tipo de ventana no soportado")
    return signal * window

def compute_fft(signal, fs):
    """Calcula la Transformada de Fourier de la señal EMG."""
    N = len(signal)
    freq = np.fft.fftfreq(N, d=1/fs)
    fft_values = np.abs(fft(signal))
    power_spectrum = fft_values ** 2  # Espectro de potencia
    return freq[:N//2], fft_values[:N//2], power_spectrum[:N//2]

def analyze_fatigue(freq, power_spectrum):
    """Detecta signos de fatiga basándose en el desplazamiento del espectro de frecuencia."""
    peak_freq = freq[np.argmax(power_spectrum)]
    return peak_freq

def process_emg(filename, fs=1000, num_contractions=37):
    """Procesa la señal de EMG para graficarla, aplicar ventanas y calcular FFT y espectro."""
    emg_signal = load_emg_signal(filename)
    segment_length = len(emg_signal) // num_contractions
    
    # Graficar la señal original completa
    plt.figure(figsize=(10, 6))
    plt.plot(emg_signal, label="Señal EMG original")
    plt.title("Señal EMG Completa")
    plt.legend()
    plt.show()
    
    selected_contractions = [0, 1, num_contractions - 2, num_contractions - 1]  # Dos primeras y dos últimas
    windows = ['hann', 'hamming']
    
    peak_frequencies = []
    
    for i in selected_contractions:
        segment = emg_signal[i*segment_length:(i+1)*segment_length]
        
        # Graficar señal original de la contracción
        plt.figure(figsize=(10, 4))
        plt.plot(segment, label=f"Contracción {i+1} (original)")
        plt.title(f"Señal EMG - Contracción {i+1}")
        plt.legend()
        plt.show()
        
        for window_type in windows:
            windowed_segment = apply_window(segment, window_type)
            freq, fft_values, power_spectrum = compute_fft(windowed_segment, fs)
            
            # Graficar señal después de aplicar la ventana
            plt.figure(figsize=(10, 4))
            plt.plot(windowed_segment, label=f"Contracción {i+1} ({window_type})")
            plt.title(f"Señal EMG Ventanada ({window_type}) - Contracción {i+1}")
            plt.legend()
            plt.show()
            
            # Graficar FFT de la contracción con la ventana aplicada
            plt.figure(figsize=(10, 4))
            plt.plot(freq, fft_values, label=f"FFT de Contracción {i+1} ({window_type})")
            plt.title(f"Transformada de Fourier ({window_type}) - Contracción {i+1}")
            plt.legend()
            plt.show()
            
            # Graficar el espectro de potencia
            plt.figure(figsize=(10, 4))
            plt.plot(freq, power_spectrum, label=f"Espectro de Potencia {i+1} ({window_type})")
            plt.title(f"Espectro de Potencia ({window_type}) - Contracción {i+1}")
            plt.legend()
            plt.show()
            
            # Análisis de fatiga
            peak_freq = analyze_fatigue(freq, power_spectrum)
            peak_frequencies.append((i+1, window_type, peak_freq))
    
    # Mostrar análisis de fatiga
    for contraction, window, peak in peak_frequencies:
        print(f"Contracción {contraction} ({window}): Frecuencia dominante = {peak:.2f} Hz")

# Ejecutar procesamiento
txt_filename = r"C:\Users\juany\OneDrive - unimilitar.edu.co\Univerisidad (Academico)\Sexto semestre\Sistemas de embebidos2.0\LabEmbebidos2.0\Lab4\emg_signal.txt"  # Cambia esto al nombre real de tu archivo
process_emg(txt_filename)
