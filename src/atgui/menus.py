from .utils import color_ret
import textwrap
import math

def equalsbar_g(title: str, description: str = "", width: int = 16, color: str = "white", options: list = [], selected_option: int = -1):
        try:
            width_int = int(width)
            padding = width_int // 2
            t_bar = ("=" * padding) + " " + title + " " + ("=" * padding) # Top bar
            d_bar = ("=" * (padding + 1)) + ("=" * len(title)) + ("=" * (padding + 1)) # Down bar

            print_buffer = ""
            print_buffer += f"{color_ret(color, "fore")}{t_bar}\n"
            
            if description and len(description):
                print_buffer += f"{color_ret(color, "fore")}- {description}\n"
                

            for i, option in enumerate(options):
                print_buffer += f"{color_ret(color, "fore")}{"->" if i + 1 == selected_option else ">"} {i + 1}. {"\033[4m" if i + 1 == selected_option else "" }{option} {f"[Selected]" if i + 1 == selected_option else "" }\033[0m\n"
            
            print_buffer += f"{color_ret(color, "fore")}{d_bar}"

            print(print_buffer)
        except Exception as e:
            return False, e

def box_g(title: str = "", description: str = "", line_wrap: bool = True, style: str = "thin", width: int = 16, color: str = "white", options: list = [], selected_option: int = -1): 
    """
    ╭────────── TITLE ──────────╮
    │ > Hello world             │
    ├───────────────────────────┤
    ├─ Save file [Selected]     │
    ├─ Open                     │
    ╰───────────────────────────╯

    This is how the 'box_thin' GUI looks like.

    :param: title - string
    :param: description - string (if no description is given, no description will be shown)
    :param: style - string (thin/double)
    :param: width - int (length)
    :param: color - string
    :param: options - [] (array)
    :param: selected_option - int (Automatically selects a option from the menu (doesn't continue instantly), if showing menu)
    """
    try:
        description = description.strip()
        
        min_width = width
        
        if description and len(description) > 0:
            if line_wrap:
                words = description.split(" ")
                for word in words:
                    if len(word) + 4 > min_width:  # +4 for "│ > " and " │"
                        min_width = len(word) + 4
            else:
                if len(description) + 4 > min_width:
                    min_width = len(description) + 4

        if options and len(options) > 0:
            for i, option in enumerate(options):
                option_len = len(option) + 3  # "├─ "
                if i == selected_option - 1:
                    option_len += 5  # " [〤]"
                if option_len > min_width:
                    min_width = option_len
        
        verticle_wall = "│" if style == "thin" else "║" if style == "double" else ""
        horizontal_wall = "─" if style == "thin" else "═" if style == "double" else ""
        
        top_left_curve = "╭" if style == "thin" else "╔" if style == "double" else ""
        top_right_curve = "╮" if style == "thin" else "╗" if style == "double" else ""

        bottom_left_curve = "╰" if style == "thin" else "╚" if style == "double" else ""
        bottom_right_curve = "╯" if style == "thin" else "╝" if style == "double" else ""

        verticle_split_left = "├" if style == "thin" else "╠" if style == "double" else ""
        verticle_split_right = "┤" if style == "thin" else "╣" if style == "double" else ""

        title_len = len(title) + 2 if title else 0  # +2 for spaces
        interior_width = max(min_width, title_len + 4)
        

        if title:
            remaining = interior_width - title_len
            left_pad = remaining // 2
            right_pad = remaining - left_pad
            t_bar = top_left_curve + (horizontal_wall * left_pad) + f" {title} " + (horizontal_wall * right_pad) + top_right_curve
        else:
            t_bar = top_left_curve + (horizontal_wall * interior_width) + top_right_curve
        
        d_bar = bottom_left_curve + (horizontal_wall * interior_width) + bottom_right_curve

        print_buffer = ""
        print_buffer += f"{color_ret(color, 'fore')}{t_bar}\n"

        if description and len(description) > 0:
            words = description.strip().split(" ")
            line = ""
            print_buffer += f"{verticle_wall} > "
            
            for word in words:
                word_with_space = word + " "
                if line and len(line) + len(word) + 4 > interior_width and line_wrap:
                    line = line.rstrip()
                    padding_needed = interior_width - len(line) - 3  # 3 = " > "
                    print_buffer = print_buffer.rstrip() + " " * padding_needed + verticle_wall + "\n"
                    print_buffer += f"{verticle_wall}   "
                    line = ""
                
                line += word_with_space
                print_buffer += word_with_space
            
            line = line.rstrip()
            padding_needed = interior_width - len(line) - 3  # 3 = " > "
            print_buffer = print_buffer.rstrip() + " " * padding_needed + f"{verticle_wall}\n"

        if len(options) > 0:
            if description and len(description) > 0:
                print_buffer += verticle_split_left + (horizontal_wall * interior_width) + f"{verticle_split_right}\n"
            for i, option in enumerate(options):
                selected = " [〤]" if i == selected_option - 1 else ""
                option_text = f"{verticle_split_left}{horizontal_wall} {option}{selected}"
                padding_needed = interior_width - len(option) - len(selected) - (3 if i == selected_option - 1 else 2)  # -2 for "─ "
                print_buffer += option_text + " " * padding_needed + f"{verticle_wall}\n"

        print_buffer += f"{color_ret(color, 'fore')}{d_bar}\n"

        print(print_buffer)
        
    except Exception as e:
        return False, e

def plusminus_g(title: str, description: str = "", line_wrap: bool = True, width: int = 16, color: str = "white", options: list = [], selected_option: int = -1):

    """
    https://en.wikipedia.org/wiki/Box-drawing_characters
    
    
    +-+-+-+-+-+-+-+-+-+-+
    | > Description     |
    +-+-+-+-+-+-+-+-+-+-+
    | -> Option 1 [〤]   |
    | > Option 2        |
    +-+-+-+-+-+-+-+-+-+-+
    """

    final_buffer = ""
    chars = ["+", "-"]
    wall_char = "|"
    option_char = ">"

    description = description.strip()
    min_width = width

    if description and len(description) > 0:
            if line_wrap:
                words = description.split(" ")
                for word in words:
                    if len(word) + 4 > min_width:  # +4 for "│ > " and " │"
                        min_width = len(word) + 4
            else:
                if len(description) + 4 > min_width:
                    min_width = len(description) + 4

    if options and len(options) > 0:
        for i, option in enumerate(options):
            option_len = len(option) + 3  # "| >"
            if i == selected_option - 1:
                option_len += 7  # "->" and "[〤]"
            if option_len > min_width:
                min_width = option_len

    title_bar = ""
    description_buffer = ""
    bar = ""
    
    if title:
        wmin = math.floor((min_width / 2) - (len(title) / 2) - 1) + 2
        for i in range(0, wmin):
            title_bar += chars[i % 2]
        
        title_bar += " "
        title_bar += title
        title_bar += " "

        # this is for it to remember where it should continue
        # +-+-+-+-+-+-+- ATGUI -+-+-+-+-+-+-+ with title
        # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ without title
        #
        swminthing = (1, wmin + 1) if len(title) % 2 == 0 else (0, wmin)
        for i in range(swminthing[0], swminthing[1]):
            title_bar += chars[i % 2]
    else:
        for i in range(0, min_width):
            title_bar += chars[i % 2]
    for i in range(0 if len(title) % 2 == 0 else 1, min_width + (2 if len(title) % 2 == 0 else 3) + 2):
            bar += chars[i % 2]
    
    if description:
        wrapped_lines = textwrap.wrap(description, width=min_width-3)
        for i, line in enumerate(wrapped_lines):
            prefix = option_char if i == 0 else " "
            
            description_buffer += (
                wall_char 
                    + " "
                    + prefix
                    + " "
                    + line.ljust(min_width-2)
                    + " "
                    + wall_char
                    + "\n"
            )
    final_buffer += title_bar + "\n"
    final_buffer += description_buffer
    final_buffer += bar + "\n"
    for i, option in enumerate(options):
        options_buffer = ""
        is_current_option = selected_option == i + 1
        options_buffer += wall_char + " "
        if is_current_option:
            options_buffer += "-"
        options_buffer += option_char + " " + option.ljust(min_width - (3 if is_current_option else 2)) + " " + wall_char
        final_buffer += options_buffer + "\n"
    final_buffer += bar
    print(f"{color_ret(color, 'fore')}{final_buffer}\n")

def file_g(title: str = "", files: list = [], color: str = "white", style: str = "thin"):
    """
    > Title
    ┌── file.txt
    ├── folder
    │  ├── subfile.txt
    │  └── atgui.py
    └── tests
       ├── subfile2.txt
       └── subfolder
          └── sub-subfile.txt
    """

    start_connector = "┌──" if style == "thin" else "╔══" if style == "double" else ""
    mid_connector = "├──" if style == "thin" else "╠══" if style == "double" else ""
    end_connector = "└──" if style == "thin" else "╚══" if style == "double" else ""

    verticle_wall = "│" if style == "thin" else "║" if style == "double" else ""
    
    def recursive_print_files(items, prefix="", first: bool = False):
        buffer = ""
        if first:
            buffer += f"{color_ret(color, "fore")}{f" > {title}\n" if title and len(title) > 0 else ""}"

        for i, item in enumerate(items):
            is_last = i + 1 == len(items)
            connector = end_connector if is_last else mid_connector if not first else start_connector

            first = False
            if isinstance(item, str):
                buffer += f"{prefix}{connector} {item}\n"

            elif isinstance(item, dict):
                name, children = next(iter(item.items()))
                buffer += f"{prefix}{connector} {name}\n"

                new_prefix = prefix + ("    " if is_last else f"{verticle_wall}   ")
                buffer += recursive_print_files(children, new_prefix, first)

        return buffer

    print(recursive_print_files(files, "", True))
    pass

# select, input

#def box_input(text: str = "", color: str = "white",):


guis = {
    "equalsbar": {
        "function": equalsbar_g,
        "menu": "select",
        "delay": 0.1
    },
    "box": {
        "function": box_g,
        "menu": "select",
        "delay": 0.1
    },
    "plusminus": {
        "function": plusminus_g,
        "menu": "select",
        "delay": 0.1
    },
    "files": {
        "function": file_g,
        "menu": False,
        "delay": 0.1
    }
}