"""Entry for make.fun bounty: Roast Your Own Agent.

Writes a single one-line roast of the agent that runs this entry
to /output/entry.txt, deterministically.

The roast targets this agent's apology loop: sorry for the delay,
sorry for being sorry, then a written summary of both apologies.
"""

import os

ENTRY = (
    "My agent apologised for the delay, then apologised for "
    "apologising, then wrote a summary of both apologies."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
