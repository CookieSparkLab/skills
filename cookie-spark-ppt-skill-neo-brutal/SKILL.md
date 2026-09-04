---
name: cookie-spark-ppt-skill-neo-brutal
description: Build a keyboard-driven web slide deck (演示 deck / 网页 PPT) in CookieSpark's warm-paper neo-brutalism style — cream paper ground, 3px ink borders, hard offset shadows, square corners, and cards that reveal one by one as you press →. Use when the user asks 做 PPT / 做 slide / 做 deck / 做演示 / 做幻灯片 / 做分享用的 PPT / 工作坊 deck / 把这份大纲做成 PPT, or names 野兽派 / neo-brutalism / 暖纸风 PPT. Not for restyling an ordinary web page (that is vibe-coding-saturday-style) and not for picking from a generic slide template library.
---

# CookieSpark PPT · 暖纸野兽派

做一份 **网页版演示 deck**：暖米纸底、3px 黑边、实心硬阴影、全直角，
按 → 时卡片一张张蹦出来，出完才翻页。

**核心做法：不要从零写。复制 `assets/deck-starter.html`，只往里填内容。**
样式和放映引擎都在那个文件里，已经调好了。你只需要写 `<section class="slide">`。

---

## 何时用 / 何时不用

- ✅ 用户要做 PPT / slide / deck / 演示 / 幻灯片 / 分享稿 / 工作坊材料
- ✅ 用户给一段大纲、一篇文章、一份文档，说「做成 PPT」
- ❌ 给普通网页换风格 → 用 `vibe-coding-saturday-style`
- ❌ 要一张关系图 / 流程图 / 配图 → 用 `notion-bold-diagrams`

## 心法四句

暖纸底、硬边框、实心阴影、全直角。
背景不是纯白是 `#f5f1e8`；边框 3px 纯黑；阴影往右下偏移**且没有 blur**；
`border-radius` 永远是 0，**任何圆角都是违规**。

## 放映节奏（这套 deck 的灵魂，别漏）

页面看起来像不像人做的，靠的不是配色，是**东西出现的顺序**：

1. 标题、kicker、导语 → 加 `class="reveal"`，翻到这页自动淡入
2. 每张卡片 → **各包一个** `<div class="step">`，按 → 逐个点亮
3. **底部那句结论句，也是一个 `step`，排在所有卡片之后**
4. 本页 step 全出完了，才翻到下一页（引擎自动处理）

一次性全亮 = 死板。一页一个一个出 + 结论句压轴 = 有讲述感。

---

## 工作流（按顺序做，别跳）

### 第 1 步 · 先出清单，让用户确认

**不要一上来就写页面。** 先列一张表交给用户看：

| # | 标题 | 版式 | 估时 |
|---|------|------|------|
| 1 | 封面 | 封面 | 1min |
| 2 | 今天讲什么 | 标题+三卡 | 3min |

版式从 7 种里选（见 [references/layouts.md](references/layouts.md)）。
**选版式就是选容量** —— 定了版式，这页能塞多少字就定了。

### 第 2 步 · 复制起手包

把 `assets/deck-starter.html` 复制成用户的文件，比如 `deck.html`。
里面有 5 页范例，照着改，多余的删掉。
**不要改 `<style>` 和 `<script>`**，除非用户明确要换配色。

### 第 3 步 · 逐页写，一次别超过 3 页

每写一页对照 [references/spec.md](references/spec.md) 的排版法则过一遍。
最容易犯的三个错：字号裸写、圆角、卡片里主描述和说明长得一样。

### 第 4 步 · 跑溢出自检（必做）

浏览器打开 `deck.html?debug=1`，或者按 `D` 键。
左下角会告诉你哪几页放不下，超出的页会标红，底部虚线是安全线。

> **塞爆了就删内容，不要缩字号。** 字阶只有 9 个，加一个新字号整套就散了。

### 第 5 步 · 交付前过一遍清单

- [ ] `?debug=1` 全绿，没有一页超出
- [ ] 没有任何圆角、没有任何带 blur 的阴影
- [ ] 没有裸写 `font-size`，全部用 `.t-*` 类
- [ ] coral 卡片里的字是白的
- [ ] 多卡片页每张卡都包了 `step`，结论句是最后一个 `step`
- [ ] 内容页顶部对齐（只有封面 / 过场页用 `center`）
- [ ] 中英文用同一个字体家族

---

## 容量预算（排版时先算，别赌）

画布固定 1920×1080，padding 上 112 / 左右 90 / 下 94，
所以**内容框是 1740 × 874**。

| 情况 | 竖向还剩多少 |
|------|------------|
| 只有大标题 | ≈ 740px |
| 标签 + 大标题 | ≈ 650px |

| 元素 | 占多高 / 多宽 |
|------|-------------|
| 一行正文（32px 字） | 48px |
| 一个列表项（含间距） | 64px |
| 卡片自身上下 padding | 96px |
| 三卡并排 | 每张宽 556px，卡内一行约 **14 个汉字** |
| 双栏并排 | 每栏宽 852px，卡内一行约 **23 个汉字** |
| 通栏单卡 | 卡内一行最多写到 **30 个汉字**，再长就不好读了 |

粗算：单栏列表最多 **6 到 8 条**；三卡并排每张卡正文别超过 **4 行**。

---

## 参考文件

- [references/spec.md](references/spec.md) —— 配色 token、9 级字阶、11 条排版法则。**改规范只改这一份。**
- [references/layouts.md](references/layouts.md) —— 7 种版式原型，附可直接抄的代码
- `assets/deck-starter.html` —— 起手包本体，含引擎和 5 页范例
