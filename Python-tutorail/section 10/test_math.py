from manim import *


class Parabola(Scene):
    def construct(self):

        # محور مختصات
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 9, 1],
            axis_config={"include_numbers": True},
        )

        # تابع f(x) = x²
        graph = axes.plot(
            lambda x: x**2,
            x_range=[-3, 3],
        )

        # نمایش محور
        self.play(Create(axes))

        # رسم متحرک سهمی
        self.play(Create(graph))

        self.wait(2)