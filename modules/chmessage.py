#Christian Emanuel Wijaya (C) - 2026
#ChMessage module
#ChMessage Version 1.0.0

import sys
from datetime import datetime

try:
    from . import chcolor as chc
    _HAS_COLOR = True
except ImportError:
    _HAS_COLOR = False


# ============================================================
# Konfigurasi default
# ============================================================
DEFAULT_SHOW_TIME = False
DEFAULT_STREAM = sys.stdout


# ============================================================
# Helper internal
# ============================================================
def _color(text: str, fg: str | None = None, bold: bool = False) -> str:
    """Warnai teks kalau chcolor tersedia."""
    if not _HAS_COLOR or fg is None:
        return text
    return chc.Color.paint(text, fg=fg, bold=bold)


def _format(label: str, message: str, color: str | None,
            show_time: bool, time_fmt: str) -> str:
    """Bangun string pesan: [TIME] LABEL: message."""
    parts = []
    if show_time:
        parts.append(_color(f"[{datetime.now().strftime(time_fmt)}]", chc.Color.BRIGHT_BLACK if _HAS_COLOR else None))
    parts.append(_color(f"{label}:", color, bold=True))
    parts.append(message)
    return " ".join(parts)


def _emit(text: str, stream, end: str = "\n") -> None:
    print(text, file=stream, end=end)


# ============================================================
# API publik
# ============================================================
def info(message: str, *, show_time: bool | None = None,
         time_fmt: str = "%H:%M:%S", stream=None, end: str = "\n") -> None:
    """INFO: pesan informasi."""
    show_time = DEFAULT_SHOW_TIME if show_time is None else show_time
    stream = stream or DEFAULT_STREAM
    color = chc.Color.BRIGHT_CYAN if _HAS_COLOR else None
    _emit(_format("INFO", message, color, show_time, time_fmt), stream, end)


def error(message: str, *, show_time: bool | None = None,
          time_fmt: str = "%H:%M:%S", stream=None, end: str = "\n") -> None:
    """ERROR: pesan error (ke stderr secara default)."""
    show_time = DEFAULT_SHOW_TIME if show_time is None else show_time
    stream = stream or sys.stderr
    color = chc.Color.BRIGHT_RED if _HAS_COLOR else None
    _emit(_format("ERROR", message, color, show_time, time_fmt), stream, end)


def warn(message: str, *, show_time: bool | None = None,
         time_fmt: str = "%H:%M:%S", stream=None, end: str = "\n") -> None:
    """WARN: pesan peringatan."""
    show_time = DEFAULT_SHOW_TIME if show_time is None else show_time
    stream = stream or sys.stderr
    color = chc.Color.BRIGHT_YELLOW if _HAS_COLOR else None
    _emit(_format("WARN", message, color, show_time, time_fmt), stream, end)


def success(message: str, *, show_time: bool | None = None,
            time_fmt: str = "%H:%M:%S", stream=None, end: str = "\n") -> None:
    """SUCCESS: pesan sukses."""
    show_time = DEFAULT_SHOW_TIME if show_time is None else show_time
    stream = stream or DEFAULT_STREAM
    color = chc.Color.BRIGHT_GREEN if _HAS_COLOR else None
    _emit(_format("SUCCESS", message, color, show_time, time_fmt), stream, end)


def debug(message: str, *, show_time: bool | None = None,
          time_fmt: str = "%H:%M:%S", stream=None, end: str = "\n") -> None:
    """DEBUG: pesan debug."""
    show_time = DEFAULT_SHOW_TIME if show_time is None else show_time
    stream = stream or DEFAULT_STREAM
    color = chc.Color.BRIGHT_MAGENTA if _HAS_COLOR else None
    _emit(_format("DEBUG", message, color, show_time, time_fmt), stream, end)


def custom(label: str, message: str, *, color: str | None = None,
           show_time: bool | None = None, time_fmt: str = "%H:%M:%S",
           stream=None, end: str = "\n") -> None:
    """Pesan dengan label & warna bebas."""
    show_time = DEFAULT_SHOW_TIME if show_time is None else show_time
    stream = stream or DEFAULT_STREAM
    _emit(_format(label.upper(), message, color, show_time, time_fmt), stream, end)


def blank(lines: int = 1, stream=None) -> None:
    """Cetak baris kosong."""
    stream = stream or DEFAULT_STREAM
    print("\n" * (lines - 1), file=stream)


def set_defaults(*, show_time: bool | None = None, stream=None) -> None:
    """Ubah default global."""
    global DEFAULT_SHOW_TIME, DEFAULT_STREAM
    if show_time is not None:
        DEFAULT_SHOW_TIME = show_time
    if stream is not None:
        DEFAULT_STREAM = stream


# Alias pendek
inf = info
err = error
wrn = warn
ok = success
dbg = debug

__all__ = [
    "info", "error", "warn", "success", "debug", "custom", "blank",
    "set_defaults", "inf", "err", "wrn", "ok", "dbg",
]