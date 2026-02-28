from turtle import Turtle

from .element import Element
from .line import Line
from .label import Label


class Axes(Element):
    x_label: Label
    y_label: Label
    x_axis: Line
    y_axis: Line

    def __init__(
        self, x_label: str = "Q", y_label: str = "P", font=("Helvetica", 24, "bold")
    ) -> None:
        super().__init__()
        self.x_label = Label(x_label, (200, -240), font)
        self.y_label = Label(y_label, (-225, 190), font)
        self.x_axis = Line((-220, -200), (200, -200))
        self.y_axis = Line((-200, -220), (-200, 200))

    def render(self, turtle: Turtle) -> None:
        self.x_axis.render(turtle)
        self.y_axis.render(turtle)
        self.x_label.render(turtle)
        self.y_label.render(turtle)
