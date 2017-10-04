from math import cos, pi

from draw import *
from helper import randoms_from
from signal import fourier_spectrum, repaired_signal, polyharmonic_signal

N = 64
TEST_SIGNAL = lambda signal_index, N: 10 * cos((2 * pi * signal_index) / N)
TEST_AMPLITUDES = [1, 3, 5, 8, 10, 12, 16]
TEST_PHASES = [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]

TEST_SPECTRUM = list(zip(list(randoms_from(TEST_AMPLITUDES, N)), list(randoms_from(TEST_PHASES, N))))
LABELS = ['Original signal', 'Repaired signal']

if __name__ == '__main__':
    # Task 2)
    original_signal_values = [TEST_SIGNAL(i, N) for i in range(N)]
    spectrum = fourier_spectrum(original_signal_values)
    repaired_signal_values = [repaired_signal(i, spectrum) for i in range(N)]
    harmonic_signals_values = [original_signal_values, repaired_signal_values]
    # Task 3)
    test_polyharmonic_signal = lambda signal_index, N: polyharmonic_signal(signal_index, N, 30, TEST_SPECTRUM)
    repaired_polyharmonic_signal = lambda signal_index, spectrum: spectrum[0][0] / 2 + repaired_signal(signal_index,
                                                                                                       spectrum)
    original_poly_signal_values = [test_polyharmonic_signal(i, N) for i in range(N)]
    poly_spectrum = fourier_spectrum(original_poly_signal_values)
    repaired_poly_signal_values = [repaired_polyharmonic_signal(i, poly_spectrum) for i in range(N)]
    polyharmonic_signals_values = [original_poly_signal_values, repaired_poly_signal_values]

    draw_signal_comparison(harmonic_signals_values, polyharmonic_signals_values, spectrum, poly_spectrum, LABELS)
