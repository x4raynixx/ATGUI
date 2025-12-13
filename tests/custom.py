from src.atgui import core as atgui

ATGUI = atgui.Manager()

result = ATGUI.show_gui(
    "plusminus",
    True,
    True,
    line_wrap = True,
    title = "ATGUI",
    description = "This is the Description for this GUI lfldsdsklfsdjflksdjfsldkffj",
    options = ["Save file", "Open new file"],
    color = "purple",
)

print(result)