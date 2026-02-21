from turtle import Turtle

from .element import Element


class Line(Element):
    sx: int
    sy: int
    ex: int
    ey: int

    def __init__(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        super().__init__()
        self.sx, self.sy = start
        self.ex, self.ey = end

    def render(self, turtle: Turtle) -> None:
        turtle.penup()
        turtle.goto(self.sx, self.sy)
        turtle.pendown()
        turtle.goto(self.ex, self.ey)
        turtle.penup()
