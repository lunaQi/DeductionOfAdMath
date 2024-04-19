import math
from manim import *
import numpy as np


class BoundednessFun(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        background = ImageMobject('assets/BoundednessFun.jpeg')
        grid_ref = Axes(
            x_range=[-9, 8, 1],  # step size determines num_decimal_places.
            y_range=[-9, 5, 1],
            x_length=14,
            y_length=7.5,
        )
        grid_fun = Axes(
            x_range=[-1, 2, 1],  # step size determines num_decimal_places.
            y_range=[-4, 2, 1],
            x_length=6,
            y_length=5,
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
        def func(x):
            return (1 / x) * math.sin(1 / x)

        function = grid_fun.plot(lambda x: func(x),
                                           x_range=[0.25, 0.99, 0.001],
                                           color=BLACK,
                                           use_smoothing=False)

        # 指定图像位置.
        graph = VGroup(grid_fun, function).move_to(grid_ref.c2p(-4, -4.5, 0))

        self.add(background)

        self.play(FadeIn(grid_fun))
        self.play(FadeIn(function))
        self.wait(3)

        # 点的移动
        t = ValueTracker(0.99)  # 起始点：x=0.99
        initial_point = [grid_fun.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point, color=BLACK)
        dot.add_updater(lambda x: x.move_to(grid_fun.c2p(t.get_value(), func(t.get_value()))))

        x_space = np.array([0.99, 0.5, 0.3, 0.25])

        for x in x_space:
            self.play(t.animate.set_value(x))    # 第二镜：点的运动
            intersection_point = Dot(
                point=[grid_fun.coords_to_point(t.get_value(), func(t.get_value()))],
                color=RED_C,
                fill_opacity=1
            )
            self.add(intersection_point)

