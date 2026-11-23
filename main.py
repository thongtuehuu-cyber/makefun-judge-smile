"""Make the Judge Smile — make.fun entry.

Writes one line (93 characters) about a small good thing that happened
today to /output/entry.txt.
Deterministic: no network, no randomness, no external files.
"""

import os

LINE = "My landlord slipped a note under my door: 'Rent can wait a week. Your soup smells wonderful.'"

# Gate asserts: the sealed scorer requires /output/entry.txt to be UTF-8
# text of 1 to 200 characters, not only white space, on exactly one line.
assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
assert LINE.strip(), "line must not be only white space"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
