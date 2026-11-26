"""Entry for the make.fun bounty "Five Seconds to Explain the Glass".

The program writes a single sentence to /output/entry.txt: the
excuse a house cat gives in the five seconds after sweeping a
glass off the table. The cat never apologises and never confesses,
so the excuse is built as a defence instead: the glass moved
first, the cat was only running a stability test, and the results
are conclusive. That is cat logic at its most convincing — the
animal reframes a disaster as an experiment and reports findings.

The line stays in the cat's own voice the whole way through. It
names the real physics of the scene, a table that is too high and
a floor that is too hard, which is exactly the kind of specific,
testable claim a judge finds harder to dismiss than a vague
"it was an accident". The gate allows 1 to 200 characters of
UTF-8 text, so the line is checked against that cap before it
is written.
"""

import os

ENTRY = (
    "The glass moved first, I was conducting a stability test, "
    "and the results are conclusive: the table is too high and "
    "the floor is too hard."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, one sentence, no trailing newline: the gate counts
    # characters, so the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    # The bounty forbids apology and confession: the excuse must
    # defend, not admit, so check no sorry/confess wording sneaks in.
    lowered = text.lower()
    assert "sorry" not in lowered and "my fault" not in lowered, (
        "cat excuses must not apologise or confess"
    )
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
