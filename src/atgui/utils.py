import colorama
import platform
if (platform.system() != "Windows"): # Import these for Linux to access Keyboard Presses
    import termios
    import tty
    import sys

def color_ret(color: str, type: str):
        if type == "fore": # ALWAYS expect the user to be stupid
            attributeExists = hasattr(colorama.Fore, color.upper())
            if attributeExists:
                return colorama.Fore.__getattribute__(color.upper())
        else:
            attributeExists = hasattr(colorama.Back, color.upper())
            if attributeExists:
                return colorama.Back.__getattribute__(color.upper())
        
        return "" # now if it doesnt exist it returns this
def linux_get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':  # Escape sequence
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 'up'
                    elif ch3 == 'B':
                        return 'down'
                    elif ch3 == 'C':
                        return 'right'
                    elif ch3 == 'D':
                        return 'left'
            elif ch1 == '\r' or ch1 == '\n':
                return 'enter'
            elif ch1 == '\x03':
                return 'ctrl_c'
            elif ch1 == '\x1b':
                return 'esc'
            else:
                return ch1
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)