from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(GREEN, opacity=0.9)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


# ffmpeg -ss 30 -t 3 -i SquareToCircle.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif