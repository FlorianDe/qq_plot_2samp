import numpy as np
from matplotlib import pyplot as plt

from qq_plot_2samp.qq_plot import draw_qq_plot, QQReferenceLine
from qq_plot_2samp.typing import PlotData, PlotOptions, Locale


def test_draw_qq_plot():
    np.random.seed(42)
    n = 5000
    d1 = np.linspace(-1, 1, int(n / 2))
    d2 = np.random.normal(50, 10, n)
    res = draw_qq_plot(
        PlotData(data=d1, label='Real Values'),
        PlotData(data=d2, label='Theoretical quantiles'),
        50,
        {
            # QQReferenceLine.THEORETICAL_LINE,
            QQReferenceLine.FIRST_THIRD_QUARTIL,
            QQReferenceLine.LEAST_SQUARES_REGRESSION
        },
        [0.25, 0.5, 0.75],
        plot_options=PlotOptions(title="QQ-Plot Test", locale=Locale.EN)
    )
    plt.show()
