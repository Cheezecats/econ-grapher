from abc import abstractmethod, ABC
from turtle import Turtle


class Element(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def render(self, turtle: Turtle) -> None:
        pass
