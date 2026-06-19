---
name: vibe-coding-saturday-style
description: >-
  把任意网页 / Web App 换成「VIBE CODING SATURDAY」活动官网同款视觉风格——
  neo-brutalism 新野兽派：暖米色纸张底 + 橄榄绿网格 + 珊瑚红/雾蓝点缀 +
  3px 纯黑硬边 + 实心偏移阴影（无模糊）+ Anton/Audiowide 标题字 + 直角无圆角。
  当用户想让页面「好看一点 / 不那么 AI 味 / 套用活动网站风格 / 同款风格 /
  做成复古杂志感 / neo-brutalism / 野兽派」时使用。适用于纯 HTML、React、Vue 等任意前端项目。
---

# VIBE CODING SATURDAY · 同款设计系统

这是一套「即插即用」的视觉风格。照着下面做，普通页面 1 分钟变得有设计感。
**核心心法：暖底 + 硬边 + 实心阴影 + 直角。所有圆角都去掉，所有阴影都不要模糊。**

## 第 0 步 · 设计原则（先理解再动手）

- **纸张感暖底**：背景不是纯白，是米色 `#f5f1e8`，叠一层淡橄榄绿网格 + 一道绿→粉的横向渐变。
- **硬边框**：元素用 `3px solid #0e0e0e`（黑）的边，**直角，绝不圆角**。
- **实心偏移阴影**：阴影是「一块实心黑往右下偏移」，`4px 4px 0 0 #0e0e0e`，**没有 blur**。这是野兽派的灵魂。
- **点缀色克制**：大面积留给米底和白卡，珊瑚红/雾蓝/粉/绿只用在标签、按钮、强调块上。
- **字体有对比**：大标题用极粗的 Anton（英文）/ 系统中文粗体；小标签用 Audiowide；正文用 Inter / 苹方。
- **交互是「按压感」**：hover 往左上挪 2px、阴影变大；点下去往右下挪、阴影变小，像真的按下一块牌子。

## 第 1 步 · 引入字体

在 HTML `<head>` 里加一行（标题字 Anton + 标签字 Audiowide，正文用系统/Inter 即可）：

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Audiowide&display=swap" rel="stylesheet">
```

## 第 2 步 · 贴入这段 CSS（这是核心资源，整段复制）

```css
:root {
  /* —— 配色 —— */
  --paper: #f5f1e8;   /* 暖米色，整页背景 */
  --ink:   #0e0e0e;   /* 近黑，文字 + 所有边框 + 阴影 */
  --coral: #DC5C5D;   /* 珊瑚红，主强调色（按钮/重点标签） */
  --mist:  #B6CEED;   /* 雾蓝 */
  --pink:  #ffe9f8;   /* 浅粉 */
  --sage:  #d7e7d4;   /* 浅绿 */
  --mint:  #cde2da;   /* 青绿 */

  /* —— 实心偏移阴影（无模糊，野兽派灵魂）—— */
  --shadow:    4px 4px 0 0 var(--ink);
  --shadow-lg: 6px 6px 0 0 var(--ink);
  --shadow-sm: 2px 2px 0 0 var(--ink);

  /* —— 字体 —— */
  --font-display: "Anton", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  --font-kicker:  "Audiowide", "PingFang SC", sans-serif;
  --font-body:    "Inter", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
}

/* —— 暖底 + 橄榄绿网格 + 绿→粉横向渐变 —— */
body {
  margin: 0;
  color: var(--ink);
  font-family: var(--font-body);
  background-color: var(--paper);
  background-image:
    linear-gradient(90deg, rgba(144,153,26,.22) 1px, transparent 1px),
    linear-gradient( 0deg, rgba(144,153,26,.22) 1px, transparent 1px),
    linear-gradient(90deg, rgba(206,228,219,.55), transparent 38%, rgba(255,76,178,.18));
  background-size: 32px 32px, 32px 32px, 100% 100%;
  background-attachment: scroll, scroll, fixed;
  -webkit-font-smoothing: antialiased;
}
::selection { background: var(--mist); color: var(--ink); }

/* —— 大标题 / 小标签字 —— */
.display { font-family: var(--font-display); font-weight: 900; line-height: .95; letter-spacing: -.01em; }
.kicker  { font-family: var(--font-kicker);  letter-spacing: .02em; text-transform: uppercase; }

/* —— 卡片：白底 + 黑硬边 + 实心阴影 + 直角 —— */
.card {
  background: #fff;
  border: 3px solid var(--ink);
  border-radius: 0;
  box-shadow: var(--shadow);
  padding: 1.25rem 1.5rem;
}
.card-lg { box-shadow: var(--shadow-lg); }

/* —— 标签 —— */
.tag {
  display: inline-flex; align-items: center; gap: .5rem;
  padding: .25rem .75rem;
  border: 2px solid var(--ink); border-radius: 0;
  box-shadow: var(--shadow-sm);
  font-weight: 500; font-size: .85rem;
}

/* —— 按钮：带「按压感」交互 —— */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: .5rem;
  padding: .75rem 1.25rem;
  border: 3px solid var(--ink); border-radius: 0;
  background: var(--coral); color: var(--ink);
  font-weight: 600; cursor: pointer; user-select: none;
  box-shadow: var(--shadow);
  transition: transform .15s ease, box-shadow .15s ease;
}
.btn:hover  { transform: translate(-2px,-2px); box-shadow: var(--shadow-lg); }
.btn:active { transform: translate( 2px, 2px); box-shadow: var(--shadow-sm); }

/* —— 任意元素想要 hover 抬起感，加这个类 —— */
.lift { transition: transform .15s ease, box-shadow .15s ease; }
.lift:hover { transform: translate(-2px,-2px); box-shadow: var(--shadow-lg); }
```

## 第 3 步 · 套用到结构（HTML 例子）

```html
<span class="tag" style="background:var(--mist)">PEOPLE · 一起来玩的人</span>

<h1 class="display" style="font-size:3rem">把想法变成产品</h1>

<div class="card card-lg">
  <h3 class="kicker">今日 Demo</h3>
  <p>一句话说清你要做什么，剩下交给 AI。</p>
  <button class="btn">开工 →</button>
</div>
```

## 配色用法速查

| 变量 | 颜色 | 用在哪 |
|------|------|--------|
| `--paper` | 暖米 | 整页背景（别用纯白） |
| `--ink` | 近黑 | 文字、**所有边框、所有阴影** |
| `--coral` | 珊瑚红 | 主按钮、最重要的标签（克制用） |
| `--mist` / `--pink` / `--sage` / `--mint` | 雾蓝/粉/绿/青 | 不同标签、卡片底色轮换，制造活泼感 |

## ✅ Do / ❌ Don't

- ✅ 直角（`border-radius: 0`）、3px 黑边、实心无模糊阴影、米色底。
- ✅ 标题用 `.display`（Anton 极粗），小标签用 `.kicker`（Audiowide）。
- ✅ 阴影颜色永远是黑（`--ink`），永远往右下偏移。
- ❌ 不要圆角、不要 `box-shadow` 带 blur、不要渐变按钮、不要纯白背景。
- ❌ 点缀色不要大面积铺满，留白和米底是主角。

## 给 AI 的一句话用法

> 用 `vibe-coding-saturday-style` 这个 skill，把我的页面换成活动官网同款风格：珊瑚红做主按钮，卡片轮换雾蓝/粉/绿底。

AI 会：① 加字体 `<link>` ② 注入上面的 CSS 变量与基础类 ③ 把现有按钮/卡片/标题替换成 `.btn` `.card` `.display` 等类，并去掉圆角与模糊阴影。
