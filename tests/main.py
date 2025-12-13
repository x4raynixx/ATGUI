from src.atgui import core as atgui

ATGUI = atgui.Manager()

result = ATGUI.show_gui(
    "box",
    title = "Test",
    options = ["hello", "world"],
    style = "double",
    color = "MAGENTA"
)
