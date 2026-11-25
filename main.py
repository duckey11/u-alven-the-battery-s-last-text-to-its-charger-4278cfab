"""Entry: the phone battery's last text to its charger.

Writes one line of plain text (1-200 characters) to entry.txt in
$MAKEFUN_OUTPUT_DIR (default /output). Standard library only, no
network, no secrets, fully deterministic.
"""

import os

ENTRY = (
    "You said 'five more minutes' at noon. It's midnight, I'm at 1%, "
    "and I've decided: when I go, your 7am alarm goes with me. Sweet dreams."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
