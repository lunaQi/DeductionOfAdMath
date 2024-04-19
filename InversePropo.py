import math
from manim import *

class InversePropo(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        background = ImageMobject('assets/InverseTransition.jpeg')
        grid_ref = Axes(
            x_range=[-9, 8, 1],  # step size determines num_decimal_places.
            y_range=[-9, 5, 1],
            x_length=14,
            y_length=7.5,
        )
        grid_inverse = Axes(
            x_range=[0, 2, 1],  # step size determines num_decimal_places.
            y_range=[0.8, 3, 1],
            x_length=1,
            y_length=1.1,
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
        inverse_function = grid_inverse.plot(lambda x: 1 / x,
                                           x_range=[0.34, 1, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)

        # 指定图像位置.
        inverse_graph = VGroup(grid_inverse, inverse_function).move_to(grid_ref.c2p(5, 0.8, 0))

        self.add(background)

        self.play(FadeIn(inverse_graph))
        self.wait(5)

        # t = 1的辅助线
        line = grid_inverse.get_horizontal_line(grid_inverse.c2p(1, 1, 0), color=RED_A)
        line_label = MathTex(r"t=1", color=RED, font_size=23).next_to(grid_inverse.c2p(0, 1, 0), LEFT)
        line_group = VGroup(line, line_label)

        self.play(FadeIn(line_group))