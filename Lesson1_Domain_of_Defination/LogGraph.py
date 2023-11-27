import math

from manim import *


class PlotLog(Scene):

    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[-9, 8, 1],  # step size determines num_decimal_places.
            y_range=[-9, 5, 1],
            x_length=14,
            y_length=7.5,
            x_axis_config={
                "numbers_to_include": np.arange(-9, 7 + 1, 1),
                "font_size": 24,
                "include_tip": True,
                'tip_shape': StealthTip,
            },
            y_axis_config={
                "numbers_to_include": np.arange(-9, 4 + 1, 1),
                "font_size": 24,
                "color": RED,
                "include_tip": True,
                'tip_shape': StealthTip,
            },
            axis_config={
                "color": RED
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", buff=0.1)
        x_label = grid.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)

        graphs = VGroup()
        graphs += grid.plot(lambda x: math.log((x - 1) / x, math.e),
                            x_range=[1.001, 7.001, 0.001],
                            color=BLUE,
                            use_smoothing=False)
        graphs += grid.plot(lambda x: math.log(x - 1, math.e) - math.log(x, math.e),
                            x_range=[1.001, 7.001, 0.001],
                            color=YELLOW_E,
                            use_smoothing=False)
        graphs += grid.plot(lambda x: math.log((x - 1) / x, math.e),
                            x_range=[-8.999, -0.021, 0.001],
                            color=BLUE,
                            use_smoothing=False)

        self.add(grid, grid_labels, graphs)