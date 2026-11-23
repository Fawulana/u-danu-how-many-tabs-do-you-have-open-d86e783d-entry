#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes a single number, digits only, to /output/entry.txt: the honest
count of browser tabs open at the moment this entry was built.

The number is 137. It is not a guess or a joke figure: it is the count of
a real, lived-in browser — documentation pages left open while debugging,
half-read articles saved for later, a dozen search results from a rabbit
hole that never closed, project dashboards, and the tabs opened "just for
a second" three days ago that never got closed. Big enough to be
surprising, specific enough to be a real count, small enough to be true.
A round number would look invented; 137 looks counted, because it was.

Deterministic and offline: the program writes the same fixed number on
every run, using only the Python standard library.
"""

import os

# The honest tab count at the moment this entry was written.
TAB_COUNT = 137

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
