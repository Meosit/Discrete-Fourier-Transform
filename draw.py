from matplotlib import pyplot as plt


def plot_values(signal_values):
    return list(zip(*enumerate(signal_values)))


def draw_signal_comparison(signals_values, labels):
    assert len(signals_values) == len(labels)
    plt.subplots_adjust(bottom=0.25)
    lines = []
    for signal_values in signals_values:
        x_points, y_points = plot_values(signal_values)
        line, = plt.plot(x_points, y_points)
        lines.append(line)
    plt.figlegend(lines, labels, loc='lower center')
    plt.show()
