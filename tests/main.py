from src.atgui import core as atgui

ATGUI = atgui.Manager()

result = ATGUI.show_gui(
    "files",
    title = "Files",
    files = ["file.txt", "file2.txt", {"folder": ["subfile.txt"]}],
    style = "double",
    color = "MAGENTA"
)
