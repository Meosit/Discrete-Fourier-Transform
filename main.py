from math import cos, pi

from draw import *
from signal import fourier_spectrum, repaired_signal

TEST_SIGNAL = lambda i, N: 10 * cos((2 * pi * i) / N)
N = 256
LABELS = ['Original signal', 'Repaired signal']


if __name__ == '__main__':
    original_signal_values = [TEST_SIGNAL(i, N) for i in range(N)]
    spectrum = fourier_spectrum(original_signal_values)
    repaired_signal_values = [repaired_signal(i, spectrum) for i in range(N)]
    draw_signal_comparison([original_signal_values, repaired_signal_values], LABELS)
