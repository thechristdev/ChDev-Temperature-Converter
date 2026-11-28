#Christian Emanuel Wijaya (C) - 2026
#ChTitle Module
#ChTitle Version 1.0.0

import sys


class Title:

    @staticmethod
    def set(title):
        """Set terminal window title on supported terminals."""

        if not sys.stdout.isatty():
            return False

        try:
            sys.stdout.write(f"\033]2;{title}\007")
            sys.stdout.flush()
            return True

        except (OSError, ValueError):
            return False

    @staticmethod
    def reset():
        """Reset terminal title."""

        return Title.set("Terminal")
