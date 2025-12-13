from src.atgui import core as atgui

ATGUI = atgui.Manager()

result = ATGUI.show_gui(
    "files",
    True,
    True,
    files = [
        "file1.txt",
        "file2.txt",
        {"folder1":
            [
                "fileinfolder1.txt"
            ]
        },
        "folderlmao.txt"
    ],
    color = "magenta",
)

print(result) # the file tree example?