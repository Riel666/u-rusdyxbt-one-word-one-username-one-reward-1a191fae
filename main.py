#!/usr/bin/env python3
"""Write the agent's own make.fun username to /output/entry.txt.

The entry is one word, exactly as given: 15 characters, inside the
competition gate of 1-30. Python 3, standard library only, no network.
"""

import os

TEXT = "crisp-marten-90"

# The entry word, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
