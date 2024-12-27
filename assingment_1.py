import numpy as np
import matplotlib.pyplot as plt

# Определение сигналов
def delta(n, shift=0):
    """Функция δ[n - shift]."""
    return np.array([1 if i == shift else 0 for i in n])

# Диапазон для n
n = np.arange(-10, 10, 1)

# Определение x[n] и h[n]
x = delta(n) + 2 * delta(n, shift=1) - delta(n, shift=3)
h = 2 * delta(n, shift=-1) + 2 * delta(n, shift=1)

# Свёртка y1[n] = x[n] * h[n]
y1 = np.convolve(x, h, mode='full')
n_y1 = np.arange(n[0] + n[0], n[-1] + n[-1] + 1)

# Свёртка y2[n] = x[n+2] * h[n]
x_shifted_2 = delta(n + 2) + 2 * delta(n + 2, shift=1) - delta(n + 2, shift=3)
y2 = np.convolve(x_shifted_2, h, mode='full')
n_y2 = np.arange(n[0] + n[0], n[-1] + n[-1] + 1)

# Свёртка y3[n] = x[n] * h[n+2]
h_shifted_2 = 2 * delta(n + 2, shift=-1) + 2 * delta(n + 2, shift=1)
y3 = np.convolve(x, h_shifted_2, mode='full')
n_y3 = np.arange(n[0] + n[0], n[-1] + n[-1] + 1)

# Построение графиков
plt.figure(figsize=(12, 8))

# График y1[n]
plt.subplot(3, 1, 1)
plt.stem(n_y1, y1, basefmt=" ")
plt.title(r'$y_1[n] = x[n] * h[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# График y2[n]
plt.subplot(3, 1, 2)
plt.stem(n_y2, y2, basefmt=" ")
plt.title(r'$y_2[n] = x[n+2] * h[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# График y3[n]
plt.subplot(3, 1, 3)
plt.stem(n_y3, y3, basefmt=" ")
plt.title(r'$y_3[n] = x[n] * h[n+2]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
