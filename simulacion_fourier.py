"""
Actividad formativa 2: Simulación y análisis de señales con la Transformada de Fourier
Requisitos: pip install numpy matplotlib
Ejecutar: python simulacion_fourier.py
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

CARPETA = Path("graficas")
CARPETA.mkdir(exist_ok=True)

# Parámetros de muestreo
Fs = 1000                 # Frecuencia de muestreo: 1000 muestras por segundo
T = 1.0                   # Duración de la simulación en segundos
t = np.arange(0, T, 1/Fs)
N = len(t)

# 1. Definición de señales en el dominio del tiempo
pulso = np.where((t >= 0.2) & (t < 0.4), 1.0, 0.0)
escalon = np.where(t >= 0.5, 1.0, 0.0)
f0 = 10                   # Frecuencia de la señal senoidal: 10 Hz
senoidal = np.sin(2 * np.pi * f0 * t)

def analizar_espectro(x, nombre, archivo):
    """Calcula y grafica señal, magnitud unilateral y fase de su FFT."""
    X = np.fft.rfft(x)
    frecuencias = np.fft.rfftfreq(N, d=1/Fs)
    magnitud = np.abs(X) / N
    fase = np.angle(X)

    fig, ax = plt.subplots(3, 1, figsize=(10, 8))
    ax[0].plot(t, x)
    ax[0].set_title(f"{nombre}: dominio del tiempo")
    ax[0].set_xlabel("Tiempo (s)")
    ax[0].set_ylabel("Amplitud")
    ax[0].grid(True)

    ax[1].stem(frecuencias, magnitud, basefmt=" ")
    ax[1].set_title("Espectro de magnitud")
    ax[1].set_xlabel("Frecuencia (Hz)")
    ax[1].set_ylabel("Magnitud normalizada")
    ax[1].set_xlim(0, 100)
    ax[1].grid(True)

    ax[2].plot(frecuencias, fase)
    ax[2].set_title("Espectro de fase")
    ax[2].set_xlabel("Frecuencia (Hz)")
    ax[2].set_ylabel("Fase (radianes)")
    ax[2].set_xlim(0, 100)
    ax[2].grid(True)

    fig.tight_layout()
    fig.savefig(CARPETA / archivo, dpi=160)
    plt.close(fig)

    return frecuencias, magnitud, fase

analizar_espectro(pulso, "Pulso rectangular", "pulso_rectangular.png")
analizar_espectro(escalon, "Función escalón", "funcion_escalon.png")
analizar_espectro(senoidal, "Señal senoidal de 10 Hz", "senal_senoidal.png")

# 2. Propiedad de linealidad: FFT(a*x + b*y) = a*FFT(x) + b*FFT(y)
x = senoidal
y = np.sin(2 * np.pi * 25 * t)
a, b = 2.0, 0.5
izquierda = np.fft.fft(a*x + b*y)
derecha = a*np.fft.fft(x) + b*np.fft.fft(y)
error_linealidad = np.max(np.abs(izquierda - derecha))

# 3. Desplazamiento temporal: desplazar la señal cambia la fase, no la magnitud ideal
desplazamiento = 0.1
muestras = int(desplazamiento * Fs)
x_desplazada = np.roll(x, muestras)
X_original = np.fft.fft(x)
X_desplazada = np.fft.fft(x_desplazada)
error_magnitud_desplazamiento = np.max(
    np.abs(np.abs(X_original) - np.abs(X_desplazada))
)

# 4. Escalamiento temporal: comprimir en el tiempo eleva las frecuencias
# Señal original de 10 Hz y una señal de 20 Hz para ilustrar la relación.
senal_10hz = np.sin(2 * np.pi * 10 * t)
senal_20hz = np.sin(2 * np.pi * 20 * t)
freq = np.fft.rfftfreq(N, d=1/Fs)
mag10 = np.abs(np.fft.rfft(senal_10hz)) / N
mag20 = np.abs(np.fft.rfft(senal_20hz)) / N

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(freq, mag10, label="Senoidal de 10 Hz")
ax.plot(freq, mag20, label="Senoidal de 20 Hz")
ax.set_xlim(0, 40)
ax.set_xlabel("Frecuencia (Hz)")
ax.set_ylabel("Magnitud normalizada")
ax.set_title("Comparación del espectro: 10 Hz y 20 Hz")
ax.grid(True)
ax.legend()
fig.tight_layout()
fig.savefig(CARPETA / "comparacion_frecuencias.png", dpi=160)
plt.close(fig)

# Gráfica para verificar el desplazamiento temporal
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, x, label="Original")
ax.plot(t, x_desplazada, "--", label="Desplazada 0.1 s")
ax.set_xlim(0, 0.5)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud")
ax.set_title("Desplazamiento temporal de una señal senoidal")
ax.grid(True)
ax.legend()
fig.tight_layout()
fig.savefig(CARPETA / "desplazamiento_temporal.png", dpi=160)
plt.close(fig)

print("Simulación finalizada. Gráficas guardadas en la carpeta 'graficas'.")
print(f"Error numérico de linealidad: {error_linealidad:.3e}")
print(f"Error máximo de magnitud tras desplazamiento circular: {error_magnitud_desplazamiento:.3e}")
print("La señal de 10 Hz presenta un pico en 10 Hz; la de 20 Hz, en 20 Hz.")
