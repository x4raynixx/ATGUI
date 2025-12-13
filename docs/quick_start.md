# Quick Start

1. Import the library:
```py
from atgui import core as atgui
```

2. Get the manager:
```py
ATGUI = atgui.Manager()
```

3. Use it!
```py
result = ATGUI.show_gui(
    "box", # for people that like rounded corners like me :)
    True,
    True,
    line_wrap = True,
    title = "ATGUI",
    description = "This is the Description for this GUI",
    options = ["Save file", "Open new file"],
    color = "magenta",
)

print("Saved file!" if result == 0 else "Opened new file!")
```