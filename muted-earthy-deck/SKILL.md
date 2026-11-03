---
name: muted-earthy-deck
description: >-
  把任意内容做成「Muted Earthy Tones」风格的 HTML 演示稿（PPT）——
  深紫灰画布 #6d6875 + 白色大标题（#e5989b 高亮词）+ 浅粉 kicker #f5cac3 +
  细框 block（白 / #f2e9e4 / #ebd4cb 三色循环）+ 1920×1080 定尺等比缩放 +
  逐条揭示 + 键盘翻页，中西文同族 HarmonyOS Sans SC 900 字重 / IBM Plex Mono 角标。
  当用户想「把内容做成 PPT / 演示稿 / slides / 路演稿」、「把现有 PPT 换成这个风格」、
  或拿到同风格截图要求「照这个做一套 PPT」时使用。
  产出是单文件 HTML，浏览器直接放映，适用于任何静态托管。
---

# MUTED EARTHY DECK · HTML PPT 设计系统

这是一套「即插即用」的 HTML 演示稿风格。照着下面做，任何内容 5 分钟变成一套设计统一的幻灯片。

**核心心法：深色画布 + 白色大字 + 细框浅色 block。渐变只存在于背景格纹层，其他一切纯色。**

## 第 0 步 · 设计原则（先理解再动手）

- **画布永远是深紫灰 `#6d6875`**：所有页面（包括封面、转场、结尾）都是它，叠一层白色低透明度网格 + 极淡的横向 wash。不许换背景色。
- **文字二级制**：画布上的正文和大标题一律白色；大标题里要强调某个词，用 `#e5989b`（Cotton Candy），**一条标题最多一个高亮词**。
- **kicker（大标题顶上的小小小标题）用 `#f5cac3`**，Plex Mono 等宽大写 + 一条 `#e5989b` 标尺线。
- **序号 / 编号 / 块内小标题用 `#b5838d`**（Dusty Rose）。
- **block 只有三种底色**：白 `#ffffff` / `#f2e9e4` / `#ebd4cb`。块内文字和边框一律 `#6d6875`。
- **block 配色循环规则**：同页并列 block 要么全白，要么按 白 → `#f2e9e4` → `#ebd4cb` 循环交替。**禁止整页白色里只给单个 block 上色**——那是没有规则的突兀强调。
- **细边框**：所有边框 2px `#6d6875`，圆角一律 4px，**全 deck 无阴影**。
- **渐变禁令**：文字、卡片、按钮、标签上一律纯色。唯一允许的渐变是背景格纹层（网格 + 横向 wash）。
- **中西文同族**：标题正文都用 HarmonyOS Sans SC（真 900 字重），角标用 IBM Plex Mono。绝对不要中文一套字、拉丁一套字。
- **并列卡片内容一律顶对齐**，不垂直居中——文字行数不一会把序号顶得高低不齐。

## 第 1 步 · 引入字体

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- 标题 + 正文：中西文同族 -->
<link href="https://cdn.jsdelivr.net/npm/harmonyos-sans-sc-webfont-splitted@1.1.0/dist/index.css" rel="stylesheet">
<!-- 角标 / 编号 / kicker -->
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&display=swap" rel="stylesheet">
```

## 第 2 步 · 贴入这段 CSS（这是核心资源，整段复制）

> 和同目录的 `theme.css` 完全一致。能 `<link>` 就 link，单文件交付就整段内联。

```css
/* ============================================================================
 * MUTED EARTHY DECK · HTML PPT 设计系统  v1
 * 深紫灰画布 #6d6875 + 白色大标题（#e5989b 高亮词）+ 细框 block（白 / #f2e9e4 / #ebd4cb）
 * ----------------------------------------------------------------------------
 * 用法：<link> 或整段复制本文件，然后：
 *   舞台    .viewport > .stage > section.slide × N（1920×1080 定尺，自动等比缩放）
 *   页头    .head-row > .kicker-rule(.kicker) + .headline(.hi) + .page-index
 *   页型    .s-cover / .s-list / .s-cols / .s-grid / .s-big / .s-hi / .s-break / .s-end
 *   block   .card（+.tone-cream / .tone-sand）、.row-card、.pill、.faq
 *   逐条揭示  .step（JS 点亮 .in，全部出完才翻页）
 *   HUD     .progress > i + .hud
 * ----------------------------------------------------------------------------
 * <head> 里先引字体：
 *   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 *   <link href="https://cdn.jsdelivr.net/npm/harmonyos-sans-sc-webfont-splitted@1.1.0/dist/index.css" rel="stylesheet">
 *   <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&display=swap" rel="stylesheet">
 * ========================================================================== */

:root {
  /* ---------- 画布与文字 ---------- */
  --canvas:  #6D6875;   /* Stormy Plum · 所有页面背景，每一页都是它，不许换 */
  --text:    #FFFFFF;   /* 画布上的正文与大标题 */
  --hi:      #E5989B;   /* Cotton Candy · 大标题里的高亮词，别无他用 */
  --sub:     #B5838D;   /* Dusty Rose · 序号 / 编号 / 块内小标题 */
  --kicker-c:#F5CAC3;   /* 大标题顶上的 kicker 小小小标题 */

  /* ---------- block 三色（只允许这三种底色） ---------- */
  --block:       #FFFFFF;
  --block-cream: #F2E9E4;
  --block-sand:  #EBD4CB;
  --ink:         #6D6875;   /* block 内的深色文字 + 所有细边框 */
  --muted-on-block: rgba(109,104,117,.72);

  /* ---------- 边框 / 形状 ---------- */
  --bw:       2px;      /* 所有细边框，全系统统一 */
  --bw-thin:  2px;
  --radius:   4px;      /* 唯一圆角值 */
  --line:     rgba(109,104,117,.25);  /* block 内部分隔线 */

  /* ---------- 字体：中西文同族，不要中文一套拉丁一套 ---------- */
  --font-display: "HarmonyOS Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  --font-body:    "HarmonyOS Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  --font-mono:    "IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}

/* ============ 舞台：1920×1080 定尺，等比缩放居中 ============ */
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; overflow: hidden; }
body { background: #3a363f; font-family: var(--font-body); color: var(--text); }
.viewport { position: fixed; inset: 0; overflow: hidden; }
.stage {
  position: absolute; left: 50%; top: 50%;
  width: 1920px; height: 1080px;
  transform: translate(-50%, -50%);
  transform-origin: center center;
  background: var(--canvas);
  overflow: hidden;
}

/* ============ 幻灯片通用 ============
   网格 + 一层极淡 wash：全 deck 唯一允许渐变的地方。
   文字、卡片、按钮上一律禁止渐变。 */
.slide {
  position: absolute; inset: 0;
  padding: 100px;     /* 四边统一 100px 留白，不许偷减任何一边 */
  display: flex; flex-direction: column;
  opacity: 0; visibility: hidden;
  transition: opacity .45s ease;
  background-color: var(--canvas);
  background-image:
    linear-gradient(90deg, rgba(255,255,255,.07) 1px, transparent 1px),
    linear-gradient( 0deg, rgba(255,255,255,.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(229,152,155,.10), transparent 42%, rgba(255,180,162,.08));
  background-size: 32px 32px, 32px 32px, 100% 100%;
  color: var(--text);
}
.slide.active { opacity: 1; visibility: visible; z-index: 1; }

/* ============ 页头 ============ */
/* kicker：Plex Mono 等宽小字 + 标尺线 */
.kicker {
  font-family: var(--font-mono);
  font-size: 22px; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase;
  color: var(--kicker-c);
}
.kicker-rule { display: flex; align-items: center; gap: 20px; }
.kicker-rule::after { content: ""; width: 72px; height: 2px; background: var(--hi); }

.head-row { display: flex; align-items: flex-end; justify-content: space-between; margin-bottom: 54px; }
.headline {
  font-family: var(--font-display);
  font-size: 96px; font-weight: 900;
  line-height: 1.15; letter-spacing: -0.01em;
  margin-top: 24px;
  color: var(--text);
}
.hi { color: var(--hi); }   /* 大标题里的高亮词，一条标题最多一个 */
.page-index {
  font-family: var(--font-mono);
  font-size: 22px; font-weight: 500; letter-spacing: .1em;
  color: var(--sub); white-space: nowrap; padding-bottom: 14px;
}
.page-index b { color: var(--text); font-weight: 700; }

/* ============ block：白 / cream / sand 三种底色 ============
   配色规则：同页并列 block 要么全白，要么按 白 → cream → sand 循环交替；
   禁止整页白色里只给一个 block 上色。 */
.card {
  background: var(--block);
  color: var(--ink);        /* 必须显式写，块内文字一律深色 */
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
}
.card.tone-cream, .row-card.tone-cream { background: var(--block-cream); }
.card.tone-sand,  .row-card.tone-sand  { background: var(--block-sand); }

/* 标签 pill */
.pill {
  display: inline-block;
  font-size: 24px; font-weight: 700;
  padding: 10px 24px;
  border-radius: var(--radius);
  border: var(--bw-thin) solid var(--ink);
  background: var(--block); color: var(--ink);
}
.pill.rose { background: var(--sub); border-color: var(--sub); color: #fff; }
.pill.line { color: var(--sub); border-color: var(--sub); }

/* 逐条揭示（JS 逐个点亮 .in） */
.step { opacity: 0; transform: translateY(24px); transition: opacity .55s cubic-bezier(.16,1,.3,1), transform .55s cubic-bezier(.16,1,.3,1); }
.step.in { opacity: 1; transform: none; }

/* ============ 页型 1 · 封面 .s-cover ============ */
.s-cover { align-items: center; justify-content: center; text-align: center; }
.s-cover .tag {
  display: inline-block;
  font-size: 24px; font-weight: 700;
  border: var(--bw-thin) solid rgba(255,255,255,.5);
  border-radius: var(--radius);
  padding: 14px 30px;
  margin-bottom: 72px;
  background: transparent;
  color: var(--text);
}
.s-cover .display {
  font-family: var(--font-display);
  font-size: 150px; font-weight: 900;
  line-height: 1.12; letter-spacing: -0.015em;
  color: var(--text);
}
.s-cover .display .line { display: block; white-space: nowrap; }
.s-cover .display em { font-style: normal; color: var(--hi); }
.s-cover .meta {
  margin-top: 80px;
  font-family: var(--font-mono);
  font-size: 20px; font-weight: 500; letter-spacing: .18em;
  color: rgba(255,255,255,.5); text-transform: uppercase;
}

/* ============ 页型 2 · 编号清单 .s-list ============ */
.s-list .rows { display: flex; flex-direction: column; gap: 36px; flex: 1; justify-content: center; }
.row-card {
  display: flex; align-items: center; gap: 44px;
  background: var(--block); color: var(--ink);
  border: var(--bw) solid var(--ink); border-radius: var(--radius);
  padding: 46px 56px;
}
.row-card .num {
  font-family: var(--font-mono);
  font-size: 56px; font-weight: 700; line-height: 1;
  color: var(--sub);
}
.row-card .txt { font-size: 46px; font-weight: 900; line-height: 1.3; }

/* ============ 页型 3 · 两栏对比 .s-cols ============ */
.s-cols .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 36px; flex: 1; }
.col-card { padding: 48px 52px; display: flex; flex-direction: column; gap: 36px; }
.col-card .pill { align-self: flex-start; }
.col-card .items { display: flex; flex-direction: column; gap: 24px; font-size: 31px; line-height: 1.5; font-weight: 500; }
.x-mark { color: var(--hi); font-weight: 900; margin-right: 16px; }
.check-mark { color: var(--sub); font-weight: 900; margin-right: 16px; }
.punchline {
  margin-top: 50px; text-align: center;
  font-family: var(--font-display);
  font-size: 56px; font-weight: 900; letter-spacing: -0.01em;
  color: var(--text);
}

/* ============ 页型 4 · 网格卡 .s-grid（3×2 六宫格） ============ */
.s-grid .grid6 { flex: 1; display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: 1fr 1fr; gap: 28px; }
.flow-card { display: flex; flex-direction: column; justify-content: space-between; padding: 36px 40px; }
.flow-card .fnum { font-family: var(--font-mono); font-size: 22px; font-weight: 700; letter-spacing: .1em; color: var(--sub); }
.flow-card .ftitle { font-family: var(--font-display); font-size: 46px; font-weight: 900; margin-bottom: 12px; }
.flow-card .fnote { font-size: 25px; color: var(--muted-on-block); line-height: 1.45; }

/* ============ 页型 5 · 单张大卡 .s-big（PRD / 长文） ============ */
.s-big .big-card { flex: 1; padding: 52px 64px; display: flex; flex-direction: column; }
.s-big .big-head { display: flex; align-items: baseline; gap: 40px; padding-bottom: 32px; border-bottom: var(--bw) solid var(--ink); margin-bottom: 36px; }
.s-big .big-word { font-family: var(--font-display); font-size: 92px; font-weight: 900; letter-spacing: -0.01em; line-height: 1; color: var(--sub); }
.s-big .big-sub { font-size: 30px; color: var(--muted-on-block); }
.s-big .big-sub u { text-decoration: underline dashed var(--sub) 2px; text-underline-offset: 8px; }
.s-big .two-cols { display: grid; grid-template-columns: 1fr 1fr; flex: 1; }
.s-big .col-a { padding-right: 56px; }
.s-big .col-b { padding-left: 56px; border-left: var(--bw-thin) solid var(--line); }
.faq { margin-bottom: 26px; }
.faq:last-child { margin-bottom: 0; }
.faq .q { font-size: 28px; font-weight: 900; margin-bottom: 8px; }
.faq .a { font-size: 25px; line-height: 1.55; color: var(--muted-on-block); }

/* ============ 页型 6 · 高亮卡列 .s-hi（三要素等） ============ */
/* 同列卡片内容一律顶对齐：不垂直居中，否则文字行数不一会把序号顶得高低不齐 */
.s-hi .grid3 { flex: 1; display: grid; grid-template-columns: repeat(3, 1fr); gap: 36px; }
.hi-card { display: flex; flex-direction: column; justify-content: flex-start; gap: 28px; padding: 56px 48px; }
.hi-card .hnum {
  font-family: var(--font-display);
  font-size: 120px; font-weight: 900; line-height: 1;
  color: var(--sub);
}
.hi-card .htxt { font-family: var(--font-display); font-size: 48px; font-weight: 900; line-height: 1.35; }

/* ============ 页型 7 · 大字转场 .s-break ============ */
.s-break { align-items: center; justify-content: center; text-align: center; }
/* 章节转场：上方环节名需要在投屏时清晰可读。 */
.s-break .kicker { font-size: 40px; }
.s-break .display {
  font-family: var(--font-display);
  font-size: 132px; font-weight: 900; line-height: 1.2; letter-spacing: -0.015em;
  color: var(--text);
  margin: 44px 0 48px;
}
.s-break .display .line { display: block; }
.s-break .sub { font-size: 32px; font-weight: 500; color: rgba(255,255,255,.7); }

/* ============ 页型 8 · 结尾大字 .s-end ============ */
.s-end { align-items: center; justify-content: center; text-align: center; }
.s-end .display {
  font-family: var(--font-display);
  font-size: 250px; font-weight: 900; line-height: 1; letter-spacing: -0.02em;
  color: var(--hi);
  margin-top: 36px;
}

/* ============ HUD：进度条 + 页码 ============ */
.hud {
  position: fixed; right: 30px; bottom: 26px; z-index: 50;
  font-family: var(--font-mono);
  font-size: 15px; font-weight: 500; letter-spacing: .12em;
  color: rgba(255,255,255,.6);
  user-select: none;
}
.progress { position: fixed; left: 0; top: 0; right: 0; height: 4px; z-index: 60; background: rgba(255,255,255,.12); }
.progress i { display: block; height: 100%; background: var(--hi); transition: width .4s ease; }
```

## 第 3 步 · 舞台与翻页骨架（固定结构，不要改）

每套 deck 的 HTML 骨架固定如下，同目录 `template.html` 是可直接改内容的完整成品：

```html
<div class="viewport">
  <div class="stage" id="stage">
    <section class="slide s-cover active">…</section>
    <section class="slide s-list">…</section>
    <!-- 更多 section.slide -->
  </div>
</div>
<div class="progress"><i id="bar"></i></div>
<div class="hud" id="hud">1 / 8</div>
<script>/* template.html 里的固定 JS：等比缩放 + 键盘/点击翻页 + .step 逐条揭示 */</script>
```

- 舞台定尺 **1920×1080**，JS 自动等比缩放适配窗口，所有字号按 1920 宽度设计。
- 翻页：→ / 空格 / 点击右半屏前进，← / 点击左半屏后退，Home 回封面。
- **逐条揭示**：一页里有多张卡片时，每张卡片包一个 `class="step"`，按键逐个点亮，全部出完才翻页；**页面底部的收束句也要作为最后一个 `.step`**。页头（kicker + 大标题）和单张大卡不加 `.step`，随页进入。

## 第 4 步 · 八种页型（只许用这八种，不许现编新版式）

| 页型 | 类 | 用途 | 结构要点 |
|------|-----|------|----------|
| 封面 | `.s-cover` | 第 1 页 | `.tag` + `.display`（每行包 `.line`，高亮词用 `<em>`）+ `.meta` |
| 编号清单 | `.s-list` | 3–4 条要点 | `.rows > .row-card × N`，`.num` + `.txt`，底色循环 |
| 两栏对比 | `.s-cols` | 不是/它是、前/后 | `.cols > .col-card × 2`，左白右 cream，`.pill` 开头，底部 `.punchline` 最后出 |
| 网格卡 | `.s-grid` | 流程、6 个要点 | `.grid6 > .flow-card × 6`，`.fnum` + `.ftitle` + `.fnote`，底色循环 |
| 单张大卡 | `.s-big` | 长文、PRD、问答 | `.big-card` 内 `.big-head`（`.big-word` + `.big-sub`）+ `.two-cols`（`.faq` 问答对） |
| 高亮卡列 | `.s-hi` | 三要素、划重点 | `.grid3 > .hi-card × 3`，`.hnum` + `.htxt`，顶对齐，底色循环 |
| 大字转场 | `.s-break` | 章节分隔 | `.kicker`（40px）+ `.display`（132px 白字）+ `.sub`；标题建议不超过两行 |
| 结尾 | `.s-end` | 最后一页 | `.kicker` + 250px `.display`（`#e5989b` 大字） |

每页页头固定为（封面 / 转场 / 结尾除外）：

```html
<div class="head-row">
  <div>
    <div class="kicker-rule"><span class="kicker">ENGLISH KICKER · 中文小标题</span></div>
    <h2 class="headline">页标题，<span class="hi">高亮词</span>最多一个</h2>
  </div>
  <span class="page-index"><b>02</b> / 08</span>
</div>
```

block 底色循环的标准写法（按阅读顺序轮流加类）：

```html
<div class="card">…</div>                    <!-- 白 -->
<div class="card tone-cream">…</div>         <!-- #f2e9e4 -->
<div class="card tone-sand">…</div>          <!-- #ebd4cb -->
<div class="card">…</div>                    <!-- 回到白 -->
```

## 配色速查

| 变量 | 色值 | 用在哪 | 禁区 |
|------|------|--------|------|
| `--canvas` | `#6d6875` | 所有页面背景 + block 内文字 + 所有边框 | 不许当文字色用在画布上（会隐身） |
| `--text` | `#ffffff` | 画布上的正文与大标题 | 不许用在浅色 block 里 |
| `--hi` | `#e5989b` | 大标题高亮词、封面 `<em>`、结尾大字、进度条、kicker 标尺线 | 一条标题最多一处 |
| `--sub` | `#b5838d` | 序号、编号、`.big-word`、`.pill.rose` | 画布上的小字正文（对比度不够） |
| `--kicker-c` | `#f5cac3` | 只给 kicker | 别无他用 |
| `--block` / `--block-cream` / `--block-sand` | 白 / `#f2e9e4` / `#ebd4cb` | block 底色，循环交替 | 只有这三种，禁止第四种 |

## 字阶速查（@1920，不许新增字号）

| 角色 | 尺寸 / 字重 | 用在哪 |
|------|------------|--------|
| 封面 `.display` | 150px / 900 | 仅封面 |
| 转场 `.display` | 132px / 900，行高 1.2 | 仅 `.s-break`；长标题按语义拆行，建议最多两行 |
| 结尾 `.display` | 250px / 900 | 仅 `.s-end` |
| 页标题 `.headline` | 96px / 900 | 每页一个 |
| 收束句 `.punchline` | 56px / 900 | 页底总结 |
| 卡片标题 `.ftitle` / `.txt` | 46px / 900 | 网格卡、清单行 |
| 高亮卡文字 `.htxt` | 48px / 900 | `.s-hi` |
| 大序号 `.hnum` | 120px / 900 | `.s-hi` |
| 大卡主题词 `.big-word` | 92px / 900 | `.s-big` |
| 正文 `.items` / `.faq .a` | 25–31px | 块内正文 |
| 注释 `.fnote` | 25px / muted | 网格卡注释 |
| 转场 kicker | 40px / 700 等宽 | `.s-break .kicker`，章节名要让投屏观众看清 |
| 内容页 kicker / 编号 | 22px / 700 等宽 | 内容页 `.kicker`、`.fnum`、`.page-index` |

## 布局硬规则

1. **四边留白统一 100px**（`.slide` padding），任何一边都不许偷减——底部贴边是最常见的翻车。
2. **并列卡片顶对齐**：同一张格里并排的卡片，内容一律从顶部开始排，不垂直居中。
3. **block 三色循环**：要么全白，要么 白 → cream → sand 交替，禁止孤立单块上色。
4. **内容必须放得下**：1920×1080 定尺，文字多了就减内容或收紧行距，不许溢出裁切。
5. 大标题行高 1.15 是下限——中文多行标题行高低于 1.15 会挤在一起。
6. **转场主标题与环节名**：使用 132px / 40px 的默认比例；按语义手动断行，建议最多两行，避免单字成行。每行用 `<span class="line">`；内容较长时可适当缩小标题，保证四边留白、不裁切。内容页 kicker 仍为 22px。

## ✅ Do / ❌ Don't

- ✅ 画布永远 `#6d6875`，每页都是。
- ✅ 大标题白色，高亮词 `#e5989b`，一条标题最多一个。
- ✅ block 只用白 / `#f2e9e4` / `#ebd4cb`，并列时循环交替或全白。
- ✅ 块内文字、边框一律 `#6d6875`。
- ✅ 换底色一律用 `.tone-cream` / `.tone-sand` 修饰类，不要写 inline style。
- ✅ 多卡片逐条 `.step` 揭示，收束句最后出。
- ❌ 不要给文字、卡片、按钮用渐变——渐变只属于背景格纹层。
- ❌ 不要阴影（任何形式）、不要 4px 以外的圆角、不要 2px 以外的边框。
- ❌ 不要新增字号、不要新增页型、不要新增 block 底色。
- ❌ 不要中文一套字、拉丁一套字。
- ❌ 不要把画布色 `#6d6875` 当文字色用在画布上（同色隐身）。
- ❌ 不要让内容贴底边，四边 100px 留白是硬约束。
- ❌ 并列卡片不要垂直居中内容。

## 给 AI 的一句话用法

> 用 `muted-earthy-deck` 这个 skill，把这份大纲做成一套 HTML PPT。

AI 会：① 加字体 `<link>` ② 注入 `theme.css` ③ 复制 `template.html` 的骨架与 JS ④ 按内容选页型填文字，遵守配色循环与逐条揭示规则。

## 维护

`theme.css` 是唯一真源。改完它之后跑一次 `python3 build.py`，
SKILL.md 的 CSS 代码块和 `template.html` 的内联样式会自动重新生成，三处保证逐字一致。
