from turtle import Turtle

from .element import Element
from .label import Label
from .line import Line
from .axes import Axes


class Tags(Element):
    x_dashed: Line
    y_dashed: Line
    x_label: Label
    y_label: Label

    def __init__(
        self,
        axes: Axes,
        sub: str,
        inter: tuple[int, int],
        font=("Helvetica", 24, "bold"),
    ) -> None:
        super().__init__()
        self.x_dashed = Line(inter, (inter[0], -200), "dashed")
        self.y_dashed = Line(inter, (-200, inter[1]), "dashed")
        self.x_label = Label(f"{axes.x_label.text}_{sub}", (inter[0], -240), font)
        self.y_label = Label(f"{axes.y_label.text}_{sub}", (-225, inter[1]), font)

    def render(self, turtle: Turtle) -> None:
        self.x_dashed.render(turtle)
        self.y_dashed.render(turtle)
        self.x_label.render(turtle)
        self.y_label.render(turtle)
