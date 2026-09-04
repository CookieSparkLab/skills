#!/usr/bin/env python3
"""把 theme.css 注入 SKILL.md 的 css 代码块，保证两者永远逐字一致。

theme.css 是唯一真源。改完 theme.css 后跑一次：

    python3 build.py
"""
import pathlib
import re
import sys

here = pathlib.Path(__file__).parent
css = (here / "theme.css").read_text(encoding="utf-8").rstrip("\n")
md_path = here / "SKILL.md"
md = md_path.read_text(encoding="utf-8")

new, n = re.subn(r"```css\n.*?\n```", lambda m: "```css\n" + css + "\n```", md, count=1, flags=re.S)
if n != 1:
    sys.exit("SKILL.md 里找不到 css 代码块")

if new == md:
    print("已经一致，无需改动")
else:
    md_path.write_text(new, encoding="utf-8")
    print("SKILL.md 已从 theme.css 重新生成")
