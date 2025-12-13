import colorama
import keyboard
import os
import ctypes
import time
import platform

if (platform.system() == "Linux"): # If on Linux, import a function for Linux to get the pressed key
    from .utils import linux_get_key

from . import menus
class Manager:
    def __init__(self):
        self.guis = menus.guis

    def is_terminal_focused(self):
        """
        - Returns true/false depending if you're focused on the console
        """
        foreground = ctypes.windll.user32.GetForegroundWindow()
        console = ctypes.windll.kernel32.GetConsoleWindow()
        return foreground == console
        
    def cls(self = None):
        """
        - Clears the console for the currently using Operating System
        """
        if platform.uname().system == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def print_symbol(self, num: int, symbol: str):
        """
        - Prints (num) times the (symbol) symbol you provide
        """
        print(symbol * num)

    def list(self = None):
        """
        - Prints every available GUI from the GUI list.
        """
        for gui in self.guis:
            print(gui)

    def register_gui(self, name, cb_function, menu, delay: float | None = None):
        """
        Register Custom GUI.
        
        :param name: Name of the function
        :type name: str
        
        :param cb_function: Callback function that will run when GUI is shown
        :type cb_function: function

        :param menu: Bool, if True, is interactable with arrow keys and will return index of the selected option
        :type Menu: bool

        :param delay: Seconds in between interaction, if None, there is no delay
        :type delay: float | None

        ```python
        colors = ["Red", "Black", "White"]

        def customfunction(title: str, description: str, options: list, selected_option: int):
            print(title)
            print(description)

            for i, option in enumerate(options):
                print("> " + option if i + 1 == selected_option else option)

        ATGUI.register_gui("custom_gui", customfunction, True, 0.3)

        selected_option = ATGUI.show_gui(
            "custom_gui",
            title = "Custom GUI",
            description = "Custom description",
            options = colors,
        )

        print("You chose:", colors[selected_option])
        ```
        """
        self.guis[name] = {"function": cb_function, "menu": menu, "delay": delay}

    def show_gui(self, gui_name: str, able_to_select: bool = True, able_to_escape = True, *args, **kwargs):
        """
        Shows a registered GUI.

        :param gui_name: Name of the GUI to display from the registry
        :type gui_name: str

        :param able_to_select: If the user should be able to interact with the menu. The GUI must also be a menu in the registry.
        :type able_to_select: bool

        :param able_to_escape: If the user should be able to exit the GUI with escape key.
        :type able_to_escape: bool

        The rest of the args and kwargs will be passed to the callback function.

        ```python
        options = ["Save file", "Open new file", "Save and exit"]

        selected_option = show_gui(
            "equalsbar", #default
            True,
            True,
            title = "Select an option",
            options = options
        )
        
        """
        try:
            colorama.init(autoreset=True)

            if gui_name not in self.guis:
                raise KeyError("GUI not found")
            
            gui = self.guis[gui_name]

            if gui["menu"] == "select" and able_to_select:
                selected_option = 1
                gui["function"](*args, **kwargs, selected_option=selected_option)

                ctrl_held = False
                os_name = platform.system()

                while True:
                    if os_name == "Windows": # IF WINDOWS
                        key = keyboard.read_key(suppress=True)

                        if self.is_terminal_focused():
                            continue

                        if key == keyboard.KEY_DOWN:
                            if selected_option < len(kwargs["options"]):
                                selected_option += 1
                            else:
                                selected_option = 1
                            ctrl_held = False

                        elif key == keyboard.KEY_UP:
                            if selected_option > 1:
                                selected_option -= 1
                            else:
                                selected_option = len(kwargs["options"])
                            ctrl_held = False

                        elif key == "enter":
                            ctrl_held = False
                            return selected_option - 1

                        elif key == "esc" and able_to_escape:
                            ctrl_held = False
                            exit()

                        elif key == "ctrl":
                            ctrl_held = True
                        elif key == "c" and ctrl_held:
                            exit()

                        self.cls()
                        gui["function"](*args, **kwargs, selected_option=selected_option)

                        if gui["delay"]:
                            time.sleep(gui["delay"])

                    else: # Linux
                        key = linux_get_key()

                        if key == "down":
                            if selected_option < len(kwargs["options"]):
                                selected_option += 1
                            else:
                                selected_option = 1
                            ctrl_held = False

                        elif key == "up":
                            if selected_option > 1:
                                selected_option -= 1
                            else:
                                selected_option = len(kwargs["options"])
                            ctrl_held = False

                        elif key == "enter":
                            ctrl_held = False
                            return selected_option - 1

                        elif key == "esc" and able_to_escape:
                            ctrl_held = False
                            exit()

                        elif key == "ctrl":
                            ctrl_held = True
                        elif key == "c" and ctrl_held:
                            exit()

                        self.cls()
                        gui["function"](*args, **kwargs, selected_option=selected_option)

                        if gui["delay"]:
                            time.sleep(gui["delay"])

            elif gui["menu"] == "input" and able_to_select:
                pass            
            else:
                gui["function"](*args, **kwargs)

        except KeyboardInterrupt:
            return
