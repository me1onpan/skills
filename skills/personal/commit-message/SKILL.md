---
name: commit-message
description: Use when writing a commit message.
---

Write the commit message in this format:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Every line fits in 72 columns of display width: CJK characters and full-width punctuation take 2 columns, everything else 1. A line containing a URL is exempt: keep the URL whole on one line.

The message is done when piping it into `python scripts/check-width.py` (relative to this skill's directory) prints nothing and exits 0. Otherwise rewrap each reported line and check again.
