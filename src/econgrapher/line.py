from turtle import Turtle
from typing import Literal
import numpy as np

from .element import Element


class Line(Element):
    sx: int
    sy: int
    ex: int
    ey: int
    style: Literal["solid"] | Literal["dashed"]

    def __init__(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        style: Literal["solid"] | Literal["dashed"] = "solid",
    ) -> None:
        super().__init__()
        self.sx, self.sy = start
        self.ex, self.ey = end
        self.style = style

    def render(self, turtle: Turtle) -> None:
        if self.style == "solid":
            turtle.penup()
            turtle.goto(self.sx, self.sy)
            turtle.pensize(4)
            turtle.pendown()
            turtle.goto(self.ex, self.ey)
            turtle.penup()
        else:  # dashed
            dx = self.ex - self.sx
            dy = self.ey - self.sy
            total_length = np.sqrt(dx**2 + dy**2)
            theta = np.arctan2(dy, dx)

            increments = np.arange(0, total_length + 1, 12)

            for incr in increments[::2]:
                x1 = self.sx + incr * np.cos(theta)
                y1 = self.sy + incr * np.sin(theta)

                x2 = self.sx + (incr + 10) * np.cos(theta)
                y2 = self.sy + (incr + 10) * np.sin(theta)

                turtle.penup()
                turtle.goto(x1, y1)
                turtle.pensize(4)
                turtle.pendown()
                turtle.goto(x2, y2)
                turtle.penup()
