# List of available GUIs

## equalsbar
> This is a simple choice GUI for systems that don't support unicode.

- How it looks:
```
======== ATGUI ========
- This is the Description for this GUI
-> 1. Save file [Selected]
> 2. Open new file 
=======================
```

- Usage:
```py
ATGUI.show_gui(
    gui_name        = "equalsbar",
    able_to_select  = True,
    able_to_escape  = True,
    title           = "ATGUI",
    description     = "Select an Option",
    options         = ["Save file", "Open new file"],
    color           = "magenta"
) # will return the index of option selected | None
```
## box
> Clean and aesthetic choice GUI for people that like rounded corners

- How it looks:
```
╭───── ATGUI ─────╮
│ > Select an     │
│   Option        │
├─────────────────┤
├─ Save file [〤]  │
├─ Open new file  │
╰─────────────────╯
```

- Usage:
```py
ATGUI.show_gui(
    gui_name        = "box",
    able_to_select  = True,
    able_to_escape  = True,
    line_wrap       = True,
    title           = "ATGUI",
    description     = "Select an Option",
    options         = ["Save file", "Open new file"],
    color           = "magenta",
) # will return the index of option selected | None
```

## plusminus
> Another ASCII friendly choice GUI if you don't like the first one

- How it looks:
```
+-+-+-+- ATGUI +-+-+-+-
| > Select an Option  |
-+-+-+-+-+-+-+-+-+-+-+-
| -> Save file        |
| > Open new file     |
-+-+-+-+-+-+-+-+-+-+-+-
```

- Usage:
```py
ATGUI.show_gui(
    gui_name        = "plusminus",
    able_to_select  = True,
    able_to_escape  = True,
    line_wrap       = True,
    title           = "ATGUI",
    description     = "Select an Option",
    options         = ["Save file", "Open new file"],
    color           = "magenta",
) # will return the index of option selected | None
```

## files
> A file tree, nice for outputting project layouts, etc etc etc

- How it looks:
```
┌── file1.txt
├── file2.txt
├── folder1
│   └── fileinfolder1.txt
└── folderlmao.txt
```

- Usage:
```py
ATGUI.show_gui(
    gui_name        = "files",
    able_to_select  = True,
    able_to_escape  = True,
    color           = "magenta",
    files           = [
        "file1.txt",
        "file2.txt",
        {
            "folder1": [
                "fileinfolder1.txt"
            ]
        },
        "folderlmao.txt"
    ],
)
```