#!/usr/bin/env python3
"""把 theme.css 注入 SKILL.md 的 css 代码块和 template.html 的 <style id="theme">，
保证三处永远逐字一致。

theme.css 是唯一真源。改完 theme.css 后跑一次：

    python3 build.py
"""
import pathlib
import re
import sys

here = pathlib.Path(__file__).parent
css = (here / "theme.css").read_text(encoding="utf-8").rstrip("\n")

# 1) SKILL.md 的第一个 ```css 代码块
md_path = here / "SKILL.md"
md = md_path.read_text(encoding="utf-8")
new, n = re.subn(r"```css\n.*?\n```", lambda m: "```css\n" + css + "\n```", md, count=1, flags=re.S)
if n != 1:
    sys.exit("SKILL.md 里找不到 css 代码块")
if new != md:
    md_path.write_text(new, encoding="utf-8")
    print("SKILL.md 已更新")
else:
    print("SKILL.md 无需改动")

# 2) template.html 的 <style id="theme">…</style>
tpl_path = here / "template.html"
tpl = tpl_path.read_text(encoding="utf-8")
new, n = re.subn(
    r'(<style id="theme">\n).*?(\n</style>)',
    lambda m: m.group(1) + css + m.group(2),
    tpl, count=1, flags=re.S,
)
if n != 1:
    sys.exit('template.html 里找不到 <style id="theme">')
if new != tpl:
    tpl_path.write_text(new, encoding="utf-8")
    print("template.html 已更新")
else:
    print("template.html 无需改动")
