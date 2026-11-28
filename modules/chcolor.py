#Christian Emanuel Wijaya (C) - 2026
#ChColor Module
#ChColor Version 1.0.0

import os
import ctypes
# Enable ANSI on Windows
def enable_ansi():
    if os.name != "nt":
        return True
    
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint()

        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False

        mode.value |= 0x0004

        return bool(
            kernel32.SetConsoleMode(
                handle,
                mode.value
            )
        )
    except Exception:
        return False


class Color:
     # HORIZONTAL RGB GRADIENT
    @staticmethod
    def gradient(text, colors, reverse=False):
        """
        Create a horizontal RGB gradient.

        Args:
            text (str): Text or ASCII art.
            colors (list): List of RGB tuples.
            reverse (bool): Reverse gradient direction.

        Example:
            colors = [
                (255, 0, 0),
                (0, 0, 255)
            ]
        """

        if not colors:
            return text

        if reverse:
            colors = colors[::-1]

        # Interpolate RGB colors
        def interpolate(start, end, factor):
            return tuple(
                int(start[i] + (end[i] - start[i]) * factor)
                for i in range(3)
            )

        # Get color at a specific position
        def color_at(position):
            if len(colors) == 1:
                return colors[0]

            segment = position * (len(colors) - 1)
            index = min(int(segment), len(colors) - 2)
            factor = segment - index

            return interpolate(
                colors[index],
                colors[index + 1],
                factor
            )

        result = []

        for line in text.split("\n"):
            output = []
            length = len(line)

            for i, char in enumerate(line):
                position = i / max(length - 1, 1)
                r, g, b = color_at(position)

                output.append(
                    f"\033[38;2;{r};{g};{b}m{char}"
                )

            result.append("".join(output) + Color.RESET)

        return "\n".join(result)

    # RESET
    RESET = "\033[0m"

    # NORMAL TEXT
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # BRIGHT TEXT
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # BACKGROUND
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # BRIGHT BACKGROUND
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"

    # TEXT STYLE
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    STRIKE = "\033[9m"

    # TERMINAL
    CLEAR = "\033[2J"
    CLEAR_LINE = "\033[2K"
    HOME = "\033[H"
    CURSOR_HIDE = "\033[?25l"
    CURSOR_SHOW = "\033[?25h"

    # RGB TRUE COLOR
    @staticmethod
    def rgb(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def bg_rgb(r, g, b):
        return f"\033[48;2;{r};{g};{b}m"

    # 256 COLORS
    @staticmethod
    def color256(code):
        return f"\033[38;5;{code}m"

    @staticmethod
    def bg256(code):
        return f"\033[48;5;{code}m"

    # COMBINED STYLE
    @staticmethod
    def paint(text, fg=None, bg=None, bold=False,
              italic=False, underline=False):

        style = ""

        if fg:
            style += fg

        if bg:
            style += bg

        if bold:
            style += Color.BOLD

        if italic:
            style += Color.ITALIC

        if underline:
            style += Color.UNDERLINE

        return f"{style}{text}{Color.RESET}"


# Enable ANSI when module is imported
enable_ansi()
