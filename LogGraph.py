import math
from manim import *

config.background_color = GREEN


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
                "decimal_number_config": {
                    "color": "#010101",
                    "num_decimal_places": 0,
                },
                "include_tip": True,
                'tip_shape': StealthTip,
            },
            y_axis_config={
                "numbers_to_include": np.arange(-9, 4 + 1, 1),
                "font_size": 24,
                "decimal_number_config": {
                    "color": "#010101",
                    "num_decimal_places": 0,
                },
                "include_tip": True,
                'tip_shape': StealthTip,
            },
            axis_config={
                "color": BLACK
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", buff=0.1).set_color(BLACK)
        x_label = grid.get_x_axis_label("x").set_color(BLACK)
        grid_labels = VGroup(grid, x_label, y_label)

        # 函数图像
        graph_function1 = grid.plot(lambda x: math.log((x - 1) / x, math.e),
                            x_range=[1.001, 7.001, 0.001],
                            color=BLUE,
                            use_smoothing=False)
        graph_function2 = grid.plot(lambda x: math.log(x - 1, math.e) - math.log(x, math.e),
                            x_range=[1.001, 7.001, 0.001],
                            color=YELLOW_E,
                            use_smoothing=False)
        graph_function12 = grid.plot(lambda x: math.log((x - 1) / x, math.e),
                            x_range=[-8.999, -0.021, 0.001],
                            color=BLUE,
                            use_smoothing=False)

        # 制作图例
        legend1 = Square(side_length=0.2, color=BLUE).set_fill(BLUE, opacity=1).move_to(grid.c2p(-8, -6, 0))
        legend2 = Square(side_length=0.2, color=YELLOW_E).set_fill(YELLOW_E, opacity=1).next_to(legend1, direction=DOWN, buff=1)
        function1 = MathTex(r"y=ln\frac{x-1}{x}").set_color(BLACK).next_to(legend1, direction=RIGHT, buff=0.2)
        function2 = MathTex(r"y=ln(x-1)-lnx").set_color(BLACK).next_to(legend2, direction=RIGHT, buff=0.2)
        function_label1 = VGroup(legend1, function1)
        function_label2 = VGroup(legend2, function2)

        # self.add(grid, grid_labels, graphs, legends)
        # 编辑动画 1.出现坐标轴 -> 2.函数画线 -> 3.生成图例
        self.play(FadeIn(grid_labels))
        self.play(Create(graph_function1), Create(graph_function12))
        self.play(FadeIn(function_label1))
        self.play(Create(graph_function2))
        self.play(FadeIn(function_label2))