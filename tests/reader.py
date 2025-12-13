# 15 Lines of code for a simple "ls/dir" script.

import os
from src.atgui import core as atgui

ATGUI = atgui.Manager()

res = ATGUI.show_gui(
    gui_name="box",
    title="Files / Directories",
    able_to_select=False,
    able_to_escape=True,
    options=os.listdir(),
    color="blue"
)