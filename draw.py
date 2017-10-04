from matplotlib import pyplot as plt


def plot_values(signal_values):
    return list(zip(*enumerate(signal_values)))


def draw_signal_comparison(harmonic_signals_values, polyharmonic_signals_values, labels):
    assert len(harmonic_signals_values) == len(labels)
    plt.subplots_adjust(bottom=0.25)
    plt.subplot(1, 2, 1)
    lines = []
    for signal_values in harmonic_signals_values:
        x_points, y_points = plot_values(signal_values)
        line, = plt.plot(x_points, y_points)
        lines.append(line)
    plt.subplot(1, 2, 2)
    for signal_values in polyharmonic_signals_values:
        x_points, y_points = plot_values(signal_values)
        line, = plt.plot(x_points, y_points)
    plt.figlegend(lines, labels, loc='lower center')
    plt.show()
