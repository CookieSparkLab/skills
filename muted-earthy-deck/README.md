# muted-earthy-deck

Muted Earthy Tones 风格的 HTML PPT skill：深紫灰画布 + 白色大字 + 细框浅色 block，单文件 HTML，浏览器直接放映。

## 文件

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 规范全文：设计原则、配色/字阶速查、8 种页型、Do/Don't |
| `theme.css` | 唯一真源：所有 design token 与组件样式 |
| `template.html` | 可直接改内容的完整模板（8 种页型各一页示例） |
| `build.py` | 改完 `theme.css` 后跑一次，同步注入 SKILL.md 和 template.html |

## 快速开始

复制 `template.html`，替换每页文字即可。规则看 `SKILL.md`。
