import math
from manim import *
import numpy as np


class SquArc(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        background = ImageMobject('assets/SquArc.jpeg')
        grid_ref = Axes(
            x_range=[-9, 8, 1],  # step size determines num_decimal_places.
            y_range=[-9, 5, 1],
            x_length=14,
            y_length=7.5,
        )
        grid_square = Axes(
            x_range=[-1, 7, 1],  # step size determines num_decimal_places.
            y_range=[-5, 6, 1],
            x_length=2,
            y_length=3,
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

        grid_arcsin = Axes(
            x_range=[-1.5, 1.5, 0.5],  # step size determines num_decimal_places.
            y_range=[-2, 2, 1],
            x_length=2,
            y_length=2.7,
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

        # 函数图像
        square_function = grid_square.plot(lambda x: -x ** 2 + 6 * x - 4,
                                           x_range=[0, 5.999, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)
        arcsin_function = grid_arcsin.plot(lambda x: math.asin(x),
                                           x_range=[-1, 1, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)

        # 函数表达式
        square_label = MathTex(r"y=-x^2+6x-4", color=BLACK, font_size=23).next_to(grid_square.c2p(7, 4, 0), RIGHT)
        arcsin_label = MathTex(r"y=arcsin(x)", color=BLACK, font_size=23).next_to(grid_arcsin.c2p(1, 1.5, 0), RIGHT)

        # 指定图像位置.
        square_graph = VGroup(grid_square, square_function, square_label).move_to(grid_ref.c2p(5, 1, 0))
        arcsin_graph = VGroup(grid_arcsin, arcsin_function, arcsin_label).move_to(grid_ref.c2p(6, -6, 0))

        self.add(background)
        # self.add(grid_ref)
        # 编辑动画 1.出现函数 -> 2.函数取绝对值 -> 3.标记界限M
        self.play(FadeIn(square_graph))
        self.play(FadeIn(arcsin_graph))

        abs_square = grid_square.plot(lambda x: abs(-x ** 2 + 6 * x - 4),
                                           x_range=[0, 5.999, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)

        abs_arcsin = grid_arcsin.plot(lambda x: abs(math.asin(x)),
                                           x_range=[-1, 1, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)

        self.play(FadeTransform(square_function, abs_square, dim_to_match=1),
                  FadeTransform(arcsin_function, abs_arcsin, dim_to_match=1))

        # 有界性：标记最大值 -> 界限M
        dot1 = Dot(point=grid_arcsin.c2p(-1, PI / 2, 0), color=BLACK)
        dot2 = Dot(point=grid_arcsin.c2p(1, PI / 2, 0), color=BLACK)
        dots = VGroup(dot1, dot2)
        self.play(FadeIn(dots))

        line1_M = grid_arcsin.get_horizontal_line(grid_arcsin.c2p(-1, PI / 2, 0), color=RED_A)
        line2_M = grid_arcsin.get_horizontal_line(grid_arcsin.c2p(1, PI / 2, 0), color=RED_A)
        M_label = MathTex(r"M=\frac{\pi}{2}", color=RED, font_size=23).next_to(grid_arcsin.c2p(-1, 1.5, 0), LEFT)
        line_M = VGroup(line1_M, line2_M, M_label)
        self.play(FadeIn(line_M))

        self.wait(5)

        # 无界：函数持续增大
        inf_square = grid_square.plot(lambda x: abs(-x ** 2 + 6 * x - 4),
                                           x_range=[-1, 5.999, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)
        self.play(FadeIn(inf_square))