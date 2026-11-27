# modules/ChBox.py
"""Draw boxes and tables with Unicode box-drawing characters."""

import unicodedata


# ============================================================
# Lebar tampilan
# ============================================================
def _char_width(ch: str) -> int:
    if unicodedata.combining(ch):
        return 0
    if unicodedata.east_asian_width(ch) in ("W", "F"):
        return 2
    return 1


def _text_width(text: str) -> int:
    text = unicodedata.normalize("NFC", str(text))
    return sum(_char_width(c) for c in text)


def _pad(text: str, width: int, align: str = "left") -> str:
    text = str(text)
    gap = max(0, width - _text_width(text))
    if align == "right":
        return " " * gap + text
    if align == "center":
        left = gap // 2
        return " " * left + text + " " * (gap - left)
    return text + " " * gap


# ============================================================
# Border styles
# ============================================================
STYLES = {
    "single": {
        "tl": "┌", "tr": "┐", "bl": "└", "br": "┘",
        "h": "─", "v": "│",
        "lt": "├", "rt": "┤", "tt": "┬", "bt": "┴", "x": "┼",
    },
    "double": {
        "tl": "╔", "tr": "╗", "bl": "╚", "br": "╝",
        "h": "═", "v": "║",
        "lt": "╠", "rt": "╣", "tt": "╦", "bt": "╩", "x": "╬",
    },
    "rounded": {
        "tl": "╭", "tr": "╮", "bl": "╰", "br": "╯",
        "h": "─", "v": "│",
        "lt": "├", "rt": "┤", "tt": "┬", "bt": "┴", "x": "┼",
    },
    "ascii": {
        "tl": "+", "tr": "+", "bl": "+", "br": "+",
        "h": "-", "v": "|",
        "lt": "+", "rt": "+", "tt": "+", "bt": "+", "x": "+",
    },
}


def _style(name: str) -> dict:
    return STYLES.get(name, STYLES["single"])


# ============================================================
# BOX
# ============================================================
def box(
    title: str,
    content: list[tuple[str, str]],
    width: int | None = None,
    height: int | None = None,
    align: str = "left",
    label_width: int = 12,
    title_align: str = "left",
    style: str = "double",
    padding: int = 1,
) -> str:
    """
    Build a bordered box.

    Args:
        title: Title on the first line.
        content: List of (label, value) pairs.
        width: Inner width (without borders). Auto if None.
        height: Minimum total lines inside (title + content + filler).
        align: Value alignment: "left" | "right" | "center".
        label_width: Width of label column.
        title_align: Title alignment.
        style: Border style: "single" | "double" | "rounded" | "ascii".
        padding: Left/right space inside the box.
    """
    s = _style(style)

    body = [f"{label:<{label_width}}: {value}" for label, value in content]

    if height is not None:
        needed = height - 1 - len(body)
        if needed > 0:
            body += [""] * needed

    if width is None:
        candidates = [title] + body
        width = max(_text_width(line) for line in candidates) + padding * 2

    inner = width - padding * 2

    lines = [
        " " * padding + _pad(title, inner, title_align) + " " * padding
    ]
    for line in body:
        lines.append(" " * padding + _pad(line, inner, align) + " " * padding)

    top = s["tl"] + s["h"] * width + s["tr"]
    bottom = s["bl"] + s["h"] * width + s["br"]
    middle = [s["v"] + _pad(line, width) + s["v"] for line in lines]

    return "\n".join([top] + middle + [bottom])


# ============================================================
# TABLE
# ============================================================
def table(
    header: list[str],
    rows: list[list[str]],
    aligns: list[str] | None = None,
    padding: int = 1,
    style: str = "double",
    title: str | None = None,
    title_align: str = "center",
) -> str:
    """
    Build a table with header and rows.

    Args:
        header: Column names.
        rows: List of rows.
        aligns: Per-column alignment ("left"/"right"/"center").
                Default: all "left".
        padding: Left/right space per cell.
        style: Border style.
        title: Optional table title (rendered as a merged top row).
        title_align: Alignment of title.
    """
    s = _style(style)
    ncol = len(header)

    if aligns is None:
        aligns = ["left"] * ncol
    if len(aligns) != ncol:
        raise ValueError("aligns length must match header length")

    # Hitung lebar kolom
    all_rows = [header] + rows
    col_widths = [
        max(_text_width(str(row[i])) for row in all_rows) + padding * 2
        for i in range(ncol)
    ]

    def hline(left: str, mid: str, right: str) -> str:
        return left + mid.join(s["h"] * w for w in col_widths) + right

    def row(values: list[str], align_row: list[str]) -> str:
        cells = []
        for v, w, a in zip(values, col_widths, align_row):
            inner = w - padding * 2
            cells.append(" " * padding + _pad(v, inner, a) + " " * padding)
        return s["v"] + s["v"].join(cells) + s["v"]

    lines = []

    # Title (merged row)
    if title is not None:
        total_inner = sum(col_widths) + (ncol - 1)  # +1 untuk tiap separator
        lines.append(s["tl"] + s["h"] * total_inner + s["tr"])
        lines.append(
            s["v"] + " " + _pad(title, total_inner - 2, title_align) + " " + s["v"]
        )
        lines.append(hline(s["lt"], s["x"], s["rt"]))
    else:
        lines.append(hline(s["tl"], s["tt"], s["tr"]))

    # Header
    lines.append(row(header, ["center"] * ncol))
    lines.append(hline(s["lt"], s["x"], s["rt"]))

    # Body
    for r in rows:
        lines.append(row(r, aligns))

    lines.append(hline(s["bl"], s["bt"], s["br"]))

    return "\n".join(lines)


# ============================================================
# Convenience
# ============================================================
def kv(title: str, content: list[tuple[str, str]], **kwargs) -> str:
    """Shortcut: key-value box dengan label_width default."""
    kwargs.setdefault("label_width", 12)
    return box(title, content, **kwargs)