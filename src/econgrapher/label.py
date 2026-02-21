from turtle import Turtle

from .element import Element


class Label(Element):
    text: str
    x: int
    y: int
    font: tuple[str, int, str]

    def __init__(
        self, text: str, pos: tuple[int, int], font=("Helvetica", 24, "bold")
    ) -> None:
        super().__init__()
        self.text = text
        self.x, self.y = pos
        self.font = font

    def render(self, turtle: Turtle) -> None:
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.write(self.text, align="center", font=self.font)
