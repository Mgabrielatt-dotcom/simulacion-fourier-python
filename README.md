# Simulación y análisis de señales con la Transformada de Fourier

## Objetivo
Generar señales elementales, analizarlas en el dominio del tiempo y la frecuencia, y comprobar propiedades de la Transformada de Fourier.

## Requisitos
- Python 3
- NumPy
- Matplotlib

Instalación:
```bash
pip install numpy matplotlib
```

## Ejecución
```bash
python simulacion_fourier.py
```

El programa crea la carpeta `graficas` con los espectros de magnitud y fase del pulso rectangular, la función escalón y una señal senoidal, además de gráficas de comparación y desplazamiento temporal.

## Señales incluidas
- Pulso rectangular de amplitud 1 entre 0.2 y 0.4 segundos.
- Función escalón que comienza en 0.5 segundos.
- Señal senoidal de 10 Hz.

## Propiedades analizadas
- **Linealidad:** la transformada de una combinación lineal es la misma combinación lineal de las transformadas.
- **Desplazamiento temporal:** desplazar una señal modifica la fase de su espectro, mientras que la magnitud se conserva en un desplazamiento circular.
- **Escalamiento temporal/frecuencial:** al aumentar la frecuencia de la sinusoide de 10 Hz a 20 Hz, el pico espectral se desplaza de 10 Hz a 20 Hz.

## Nota
La FFT analiza una cantidad finita de muestras. El escalón y el pulso son señales limitadas en el tiempo y su espectro calculado depende de la duración y del muestreo elegidos.
