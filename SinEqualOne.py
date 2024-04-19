import math
from manim import *
import numpy as np


class SinEqualOne(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        background = ImageMobject('SinEqualOne.png')
        grid_ref = Axes(
            x_range=[-9, 8, 1],  # step size determines num_decimal_places.
            y_range=[-9, 5, 1],
            x_length=14,
            y_length=7.5,
        )
        grid = Axes(
            x_range=[-1, 9, 1],  # step size determines num_decimal_places.
            y_range=[-1, 2, 1],
            x_length=5,
            y_length=1.2,
            x_axis_config={
                "include_ticks": False,  # 坐标轴上是否做记号
                "include_tip": False,
            },
            y_axis_config={
                "include_ticks": False,
                "include_tip": False,
            },
            axis_config={
                "color": BLACK
            },
            tips=False,
        )

        # 指定图像位置.
        grid_labels = VGroup(grid).move_to(grid_ref.c2p(4, -4, 0))

        # 函数图像
        graph_function = grid.plot(lambda x: math.sin(x),
                            x_range=[0, 7.999, 0.001],
                            color=BLACK,
                            use_smoothing=False)

        # 制作图例
        num_space = [0, 1]

        self.add(background)
        # self.add(grid_ref)
        # 编辑动画 1.出现坐标轴 -> 2.函数画线 -> 3.标记等于1的点
        self.play(FadeIn(grid_labels))
        self.play(Create(graph_function))

        for num in num_space:
            x = 2 * PI * num + PI / 2
            line = grid.get_vertical_line(grid.i2gp(x, graph_function), color=RED_A)
            if num == 0:
                line_label = MathTex(r"\frac{\pi}{2}", color=BLACK, font_size=23).next_to(line, DOWN)
            else:
                line_label = MathTex(r"2\pi+\frac{\pi}{2}", color=BLACK, font_size=23).next_to(line, DOWN)
            self.play(FadeIn(line_label))
            self.play(Create(line))

        line2 = grid.get_horizontal_line(grid.c2p(5 * PI / 2, 1, 0), color=RED_A)
        self.play(Create(line2))
        line2_label = MathTex(1, color=BLACK, font_size=23).next_to(line2, LEFT)
        self.play(FadeIn(line2_label))

