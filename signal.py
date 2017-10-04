from math import sin, cos, pi, hypot, atan2


def cosine_amplitude(signal_values, harmonic_index, N):
    _sum = sum(x * cos(2 * pi * i * harmonic_index / N) for i, x in enumerate(signal_values))
    return (2 / N) * _sum


def sine_amplitude(signal_values, harmonic_index, N):
    _sum = sum(x * sin(2 * pi * i * harmonic_index / N) for i, x in enumerate(signal_values))
    return (2 / N) * _sum


def harmonic_amplitude(sine, cosine):
    return hypot(sine, cosine)


def harmonic_phase(sine, cosine):
    return atan2(sine, cosine)


def fourier_transformation(signal_values, harmonic_index, N):
    cosine = cosine_amplitude(signal_values, harmonic_index, N)
    sine = sine_amplitude(signal_values, harmonic_index, N)
    return harmonic_amplitude(sine, cosine), harmonic_phase(sine, cosine)


def fourier_spectrum(signal_values):
    N = len(signal_values)
    return [fourier_transformation(signal_values, j, N) for j in range(N)]


def polyharmonic_signal(signal_index, N, summand_number, spectrum):
    amplitudes, phases = zip(*spectrum)

    def summand(sum_index):
        return amplitudes[sum_index] * cos((2 * pi * sum_index * signal_index / N) - phases[sum_index])

    return sum(summand(j) for j in range(summand_number))


def repaired_signal(signal_index, fourier_spectrum):
    N = len(fourier_spectrum)
    return polyharmonic_signal(signal_index, N, N // 2 - 1, fourier_spectrum)
