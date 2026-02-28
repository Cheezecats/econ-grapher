# econgrapher

A Python package for drawing economic graphs using the `turtle` library.

## Elements

### `Element` (base class)
Abstract base class. All elements inherit from this and implement `render(turtle: Turtle)`.

### `Label(text, pos, font)`
Draws text at a position.
- `text`: string to display
- `pos`: `(x, y)` tuple
- `font`: `("FontName", size, "style")` — default `("Helvetica", 24, "bold")`

### `Line(start, end, style)`
Draws a line between two points.
- `start`, `end`: `(x, y)` tuples
- `style`: `"solid"` or `"dashed"` (default `"solid"`)

### `Axes(x_label, y_label, font)`
Creates a coordinate system with perpendicular axes.
- `x_label`: default `"Q"`
- `y_label`: default `"P"`

### `Tags(axes, sub, inter, font)`
Marks an intersection point with dashed lines to axes and labels.
- `axes`: an `Axes` instance
- `sub`: subscript string (e.g., `"1"`, `"e"`)
- `inter`: `(x, y)` intersection point

## Usage

```python
from turtle import Turtle
from econgrapher import Axes, Line, Label, Tags

t = Turtle()

# Draw axes
axes = Axes("Q", "P")
axes.render(t)

# Draw a demand curve
demand = Line((-100, 100), (100, -100))
demand.render(t)

# Mark equilibrium point
tags = Tags(axes, "e", (0, 0))
tags.render(t)