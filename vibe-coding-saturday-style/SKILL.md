---
name: vibe-coding-saturday-style
description: >-
  把任意网页 / Web App 换成「VIBE CODING SATURDAY」活动官网同款视觉风格——
  neo-brutalism 新野兽派：暖米色纸张底 + 橄榄绿网格 + 珊瑚红/雾蓝点缀 +
  3px 纯黑硬边 + 实心偏移阴影（无模糊）+ 直角无圆角 +
  中西文同族的 HarmonyOS Sans SC 标题字 / 等宽 IBM Plex Mono 角标。
  当用户想让页面「好看一点 / 不那么 AI 味 / 套用活动网站风格 / 同款风格 /
  做成复古杂志感 / neo-brutalism / 野兽派」时使用。适用于纯 HTML、React、Vue 等任意前端项目。
---

# VIBE CODING SATURDAY · 同款设计系统 v2

这是一套「即插即用」的视觉风格。照着下面做，普通页面 1 分钟变得有设计感。

**核心心法：暖底 + 硬边 + 实心阴影 + 直角。所有圆角都去掉，所有阴影都不要模糊。**

## 第 0 步 · 设计原则（先理解再动手）

- **纸张感暖底**：背景不是纯白，是米色 `#f5f1e8`，叠一层淡橄榄绿网格。
- **硬边框**：元素用 `3px solid #0e0e0e`（黑）的边，**直角，绝不圆角**。
- **实心偏移阴影**：阴影是「一块实心黑往右下偏移」，`4px 4px 0 0 #0e0e0e`，**没有 blur**。这是野兽派的灵魂。
- **点缀色克制**：大面积留给米底和白卡，珊瑚红/雾蓝/粉/绿只用在标签、按钮、强调块上。
- **中西文用同一个字体家族**：标题正文都用 HarmonyOS Sans SC，角标用等宽 IBM Plex Mono。
  **绝对不要「中文一套字、拉丁一套字」** —— 同一行里粗细字宽对不上，是最容易露馅的地方。
- **字号只有 5 个角色**：display / headline / subhead / body / label，外加一个 note 说明层。
  想做层级就用**字重和灰度**，不要新增字号。
- **交互是「按压感」**：hover 往左上挪 2px、阴影变大；点下去往右下挪、阴影变小，像真的按下一块牌子。

## 第 1 步 · 引入字体

在 HTML `<head>` 里加这几行：

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- 标题 + 正文：中西文同族 -->
<link href="https://cdn.jsdelivr.net/npm/harmonyos-sans-sc-webfont-splitted@1.1.0/dist/index.css" rel="stylesheet">
<!-- 角标 / 编号 / kicker -->
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&display=swap" rel="stylesheet">
<!-- 可选：只有「纯英文大标题」想要 Anton 的冲击力时才加 -->
<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
```

> Anton 和 Audiowide 都**只有拉丁字符**，中文会静默 fallback 成系统字。
> 所以 v2 把它们从默认字体里拿掉了 —— Anton 只保留给 `.display-en`（纯英文大标题），Audiowide 直接弃用。

## 第 2 步 · 贴入这段 CSS（这是核心资源，整段复制）

> 和同目录的 `theme.css` 完全一致。能 `<link>` 文件就 link 文件，别复制。

```css
/* ============================================================================
 * VIBE CODING SATURDAY · 同款设计系统  v2  (neo-brutalism)
 * 暖纸底 + 3px 黑硬边 + 实心偏移阴影（无模糊）+ 直角
 * ----------------------------------------------------------------------------
 * 用法：<link> 或 @import 本文件，然后给元素加类：
 *   排版  .display / .display-tight / .display-en / .headline / .subhead / .body / .label / .note
 *   组件  .card / .card-lg / .btn / .btn-secondary / .btn-ghost / .btn-sm / .tag
 *   配色  .tone-coral / .tone-mist / .tone-pink / .tone-sage / .tone-mint / .tone-ok / .tone-warn / .tone-err
 *   交互  .lift
 *   改造  .vcs-takeover（抹掉已有页面的圆角）
 * ----------------------------------------------------------------------------
 * <head> 里先引字体：
 *   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 *   <link href="https://cdn.jsdelivr.net/npm/harmonyos-sans-sc-webfont-splitted@1.1.0/dist/index.css" rel="stylesheet">
 *   <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&display=swap" rel="stylesheet">
 *   <!-- 可选，只有纯英文大标题要 Anton 的冲击力时才加 -->
 *   <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
 * ========================================================================== */

:root {
  /* ---------- 底色 ---------- */
  --paper:   #f5f1e8;   /* 暖米色，整页背景。别用纯白 */
  --surface: #ffffff;   /* 卡面 */
  --ink:     #0e0e0e;   /* 近黑：文字 + 所有边框 + 所有阴影 */
  --muted:   #5a5a55;   /* 次要文字。别拿纯黑当说明文字，页面会一片死黑 */

  /* ---------- 强调色 ---------- */
  /* 主强调色：主按钮 / 最重要的标签。品牌原色，配白字。
   * 白字对比度 3.65:1 —— 过 WCAG AA 的「大字号」档（≥24px，或 ≥18.7px 加粗），
   * 不过正文小字档。所以 coral 只用来托按钮和大标签，别拿它当小字的底色。 */
  --coral: #DC5C5D;
  --mist:  #B6CEED;     /* 雾蓝 */
  --pink:  #ffe9f8;     /* 浅粉 */
  --sage:  #d7e7d4;     /* 浅绿 */
  --mint:  #a9cfc4;     /* 青绿（v2 已与 sage 拉开距离，原值 #cde2da 和 sage 肉眼分不出） */

  /* ---------- 语义色 ---------- */
  /* 全部是浅底 + 黑字，和 --coral 拉开：主按钮和报错提示绝不能长一样 */
  --ok:   #c7e3ad;
  --warn: #ffd9a8;
  --err:  #ffc2be;

  /* ---------- 边框 / 形状 / 阴影 ---------- */
  --bw:      3px;       /* 标准硬边 */
  --bw-thin: 2px;       /* 小元素（tag / 小按钮） */
  --radius:  0;         /* 永远是 0。这套风格没有圆角 */
  --line: rgba(14,14,14,.14);  /* 表格 / 列表内部的细分隔线。外框仍然是 3px 实黑 */
  --shadow-sm: 2px 2px 0 0 var(--ink);
  --shadow:    4px 4px 0 0 var(--ink);
  --shadow-lg: 6px 6px 0 0 var(--ink);

  /* ---------- 间距刻度（8px 基准） ---------- */
  --sp-1: 8px;  --sp-2: 16px; --sp-3: 24px;
  --sp-4: 32px; --sp-6: 48px; --sp-8: 64px;

  /* ---------- 字体 ---------- */
  /* 中西文同一家族。别中文一套、拉丁一套 —— 那是 v1 最大的坑 */
  --font-display: "HarmonyOS Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  --font-body:    "HarmonyOS Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  --font-mono:    "IBM Plex Mono","JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  --font-en:      "Anton",var(--font-display);   /* 只给纯英文大标题 */
  --font-kicker:  var(--font-mono);              /* v1 兼容别名 */

  /* ---------- 字号角色（只有这 5 个 + note，别再新增） ---------- */
  --fs-display:  clamp(38px, 6.5vw, 72px);   /* 封面大标题 */
  --fs-headline: clamp(26px, 3.6vw, 40px);   /* 每屏大标题 */
  --fs-subhead:  20px;                       /* 卡片标题 / 副标题 */
  --fs-body:     16px;                       /* 正文 */
  --fs-label:    13px;                       /* 角标 / 编号 / tag */
}

/* ---------- 暖底 + 橄榄绿网格 + 绿→粉横向渐变 ----------
 * 关于「不要渐变」这条规则的准确口径：
 *   禁的是【按钮 / 卡片 / 标签】上的渐变 —— 那是廉价感的来源。
 *   页面底纹这层绿→粉的横向渐变是例外，它是纸张感的一部分，属于品牌资产。
 * 小屏会关掉 background-attachment:fixed（见文件末尾的 @media）。 */
body {
  margin: 0;
  color: var(--ink);
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: 1.75;
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

/* ============================ 排版 ============================ */
/* 中文换行安全的行高。1.3 是默认值，不是可选项 */
.display  { font-family: var(--font-display); font-weight: 900; font-size: var(--fs-display);  line-height: 1.3; letter-spacing: -.01em; }
.headline { font-family: var(--font-display); font-weight: 900; font-size: var(--fs-headline); line-height: 1.3; letter-spacing: -.01em; }
.subhead  { font-weight: 700; font-size: var(--fs-subhead); line-height: 1.4; }
.body     { font-weight: 400; font-size: var(--fs-body); line-height: 1.75; max-width: 34em; }

/* 只有「单行、不会换行」的大标题才配用紧凑行高 */
.display-tight { line-height: 1.05; }

/* 纯英文大标题想要 Anton 的冲击力时用。Anton 只有 400 字重，别写 900（会被合成假粗） */
.display-en { font-family: var(--font-en); font-weight: 400; line-height: .95; letter-spacing: 0; text-transform: uppercase; }

/* 角标 / 编号 / kicker：等宽体。等宽的工程感和野兽派天然合拍，中文 fallback 后也协调 */
.label, .kicker { font-family: var(--font-mono); font-weight: 700; font-size: var(--fs-label);
                  letter-spacing: .08em; text-transform: uppercase; line-height: 1.3; }

/* 次要说明：和正文同字号，靠「灰度 + 左竖线」拉开层级，不新增字号 */
.note { border-left: var(--bw) solid var(--muted); padding-left: var(--sp-2);
        color: var(--muted); line-height: 1.7; }

/* ============================ 卡片 ============================ */
.card {
  background: var(--surface);
  color: var(--ink);          /* 必须显式写。只写 background 不写 color，
                                 这张卡放进 .tone-coral 里就会继承白字 → 白底白字 */
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: var(--sp-3);
}
.card-lg { box-shadow: var(--shadow-lg); }

/* ============================ 标签 ============================ */
.tag {
  display: inline-flex; align-items: center; gap: var(--sp-1);
  padding: 4px 12px;
  background: var(--surface);            /* v1 忘了给底色，网格线会穿过标签内部 */
  color: var(--ink);                     /* 同上：自带底色的组件必须自带文字色 */
  border: var(--bw-thin) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  font-weight: 500; font-size: var(--fs-label); line-height: 1.5;
}

/* ============================ 按钮 ============================ */
/* 交互是「按压感」：hover 往左上抬、按下往右下沉，像按一块实体牌子 */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--sp-1);
  padding: 12px 20px;
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  background: var(--coral); color: #fff;   /* 白字是绑定在 coral 底上的。
     想要别的底色，用 .btn-secondary / .btn-quiet / .btn-ghost / .tone-*，
     千万别用 inline style 只改 background —— 文字还是白的，直接变成白底白字 */
  font-family: inherit; font-weight: 700; font-size: var(--fs-body);
  cursor: pointer; user-select: none;
  box-shadow: var(--shadow);
  transition: transform .15s ease, box-shadow .15s ease;
}
.btn:hover  { transform: translate(-2px,-2px); box-shadow: var(--shadow-lg); }
.btn:active { transform: translate( 2px, 2px); box-shadow: var(--shadow-sm); }
.btn:disabled, .btn[aria-disabled="true"] {
  opacity: .45; cursor: not-allowed; transform: none; box-shadow: var(--shadow-sm);
}

.btn-secondary { background: var(--surface); color: var(--ink); }
.btn-ghost     { background: transparent; color: var(--ink); border-color: transparent; box-shadow: none; }
.btn-ghost:hover { background: var(--surface); border-color: var(--ink); box-shadow: var(--shadow-sm); transform: none; }
.btn-sm { padding: 6px 12px; font-size: var(--fs-label); border-width: var(--bw-thin); box-shadow: var(--shadow-sm); }

/* ============================ 配色修饰类 ============================ */
/* 加在 .card / .tag / 任意块上换底色。别再手写 inline style —— 那是 v1 输出不一致的主因 */
.tone-paper { background: var(--paper);   color: var(--ink); }
.tone-white { background: var(--surface); color: var(--ink); }
.tone-coral { background: var(--coral);   color: #fff; }
.tone-mist  { background: var(--mist);    color: var(--ink); }
.tone-pink  { background: var(--pink);    color: var(--ink); }
.tone-sage  { background: var(--sage);    color: var(--ink); }
.tone-mint  { background: var(--mint);    color: var(--ink); }
.tone-ok    { background: var(--ok);      color: var(--ink); }
.tone-warn  { background: var(--warn);    color: var(--ink); }
.tone-err   { background: var(--err);     color: var(--ink); }

/* 深色卡上的按钮要换白底，否则和卡片糊在一起 */
.tone-coral .btn { background: var(--surface); color: var(--ink); }
.tone-coral .note { border-left-color: #fff; color: #fff; }

/* ============================ 高密度界面 ============================ */
/* 后台 / 表格 / 工具栏这类密集界面，4px 硬阴影会糊成一片、3px 边会把页面压得又黑又挤。
 * 给容器加 .dense，作用域内的边框和阴影整体降一档 —— 组件不用换，改的是 token。 */
.dense {
  --bw: 2px;
  --bw-thin: 2px;
  --shadow-sm: 1px 1px 0 0 var(--ink);
  --shadow:    2px 2px 0 0 var(--ink);
  --shadow-lg: 3px 3px 0 0 var(--ink);
}

/* 无阴影卡：嵌套在别的卡里、或者密集网格里用，只留边框 */
.card-flat { box-shadow: none; }

/* 安静按钮：表格行内、工具栏里的次要操作。
 * 密集界面里成排的实心阴影按钮非常吵，这个只在 hover 时才浮起来 */
.btn-quiet {
  background: var(--surface); color: var(--ink);
  border-width: var(--bw-thin); box-shadow: none;
}
.btn-quiet:hover { box-shadow: var(--shadow-sm); transform: none; }
.btn-quiet:active { box-shadow: none; transform: translate(1px,1px); }

/* ============================ 交互 ============================ */
.lift { transition: transform .15s ease, box-shadow .15s ease; }
.lift:hover { transform: translate(-2px,-2px); box-shadow: var(--shadow-lg); }

/* 键盘焦点。按压感只对鼠标生效，键盘用户也得看得见自己在哪 */
:where(a, button, input, select, textarea, summary, [tabindex]):focus-visible {
  outline: var(--bw) solid var(--coral);
  outline-offset: 3px;
}

/* ============================ 改造已有页面 ============================ */
/* 这套风格「绝不圆角」，但光加新类去不掉页面上已有的圆角。
 * 把 .vcs-takeover 加在 <body> 或某个容器上，作用域内所有圆角被抹平。 */
.vcs-takeover, .vcs-takeover *,
.vcs-takeover *::before, .vcs-takeover *::after { border-radius: 0 !important; }

/* 再狠一点：连别人带 blur 的柔和阴影一起抹掉，只留本设计系统自己的实心阴影 */
.vcs-takeover-hard *:not(.card):not(.card-lg):not(.btn):not(.tag):not(.lift):not([class*="tone-"]) {
  box-shadow: none !important;
}

/* ============================ 表单 ============================ */
/* 原生控件自带圆角和系统蓝，不接管的话整页只有按钮是野兽派、其余全是 macOS 默认 */
.field {
  display: block; width: 100%;
  padding: 10px 12px;
  font: inherit; font-size: var(--fs-body); color: var(--ink);
  background: var(--surface);
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  outline: none;
}
.field::placeholder { color: var(--muted); }
.field:disabled { opacity: .5; cursor: not-allowed; }
textarea.field { resize: vertical; min-height: 88px; line-height: 1.6; }

/* 下拉箭头用两道斜切拼出实心三角，不引任何图片 */
select.field {
  appearance: none; -webkit-appearance: none; padding-right: 36px;
  background-image:
    linear-gradient(45deg, transparent 50%, var(--ink) 50%),
    linear-gradient(135deg, var(--ink) 50%, transparent 50%);
  background-position: calc(100% - 20px) center, calc(100% - 14px) center;
  background-size: 6px 6px, 6px 6px;
  background-repeat: no-repeat;
}

/* 勾选框 / 单选框：一律方的。圆的单选框在这套语言里是异物 */
.check {
  appearance: none; -webkit-appearance: none;
  width: 20px; height: 20px; flex: none; margin: 0;
  background: var(--surface);
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  cursor: pointer;
}
.check:checked {
  background-color: var(--coral);
  background-image: linear-gradient(var(--surface), var(--surface));
  background-size: 8px 8px; background-position: center; background-repeat: no-repeat;
}

.field-label { display: block; font-weight: 700; font-size: var(--fs-body); margin-bottom: var(--sp-1); }
.field-row   { display: flex; gap: 10px; align-items: center; cursor: pointer; }

/* ============================ 表格 ============================ */
/* 外框是 3px 实黑，行与行之间用细线 —— 每行都描 3px 会变成一堆黑格子 */
.table {
  width: 100%; border-collapse: collapse;
  background: var(--surface); color: var(--ink);
  border: var(--bw) solid var(--ink);
  box-shadow: var(--shadow);
}
.table th, .table td {
  padding: 10px 14px; text-align: left;
  font-size: var(--fs-body); line-height: 1.5;
  border-bottom: var(--bw-thin) solid var(--line);
}
.table thead th {
  background: var(--paper);
  font-family: var(--font-mono); font-weight: 700; font-size: var(--fs-label);
  letter-spacing: .06em; text-transform: uppercase;
  border-bottom: var(--bw) solid var(--ink);
}
.table tbody tr:last-child td { border-bottom: 0; }

/* ============================ 导航 ============================ */
.nav { display: flex; gap: var(--sp-1); align-items: center; flex-wrap: wrap; }
.nav-item {
  display: inline-flex; align-items: center; padding: 6px 12px;
  font-weight: 700; font-size: var(--fs-body); color: var(--ink); text-decoration: none;
  background: transparent; border: var(--bw-thin) solid transparent; border-radius: var(--radius);
}
.nav-item:hover { background: var(--surface); border-color: var(--ink); }
/* 选中态用反白。这套风格没有主题色高亮可用，黑底白字是最有力也最自洽的表达 */
.nav-item.is-active, .nav-item[aria-current] {
  background: var(--ink); color: var(--surface); border-color: var(--ink);
}

/* ============================ 列表 ============================ */
/* 浏览器默认的小圆点在一套「全是硬边」的语言里非常突兀，换成 3px 黑边的小色块 */
.list { list-style: none; padding: 0; margin: 0; }
.list > li { display: flex; gap: 10px; align-items: flex-start; line-height: 1.9; }
.list > li::before {
  content: ""; flex: none; width: 9px; height: 9px; margin-top: .58em;
  background: var(--coral); border: var(--bw-thin) solid var(--ink);
}
.list-mist > li::before { background: var(--mist); }
.list-sage > li::before { background: var(--sage); }

.list-num { list-style: none; padding: 0; margin: 0; counter-reset: vcs; }
.list-num > li { display: flex; gap: 12px; align-items: flex-start; line-height: 1.9; counter-increment: vcs; }
.list-num > li::before {
  content: counter(vcs); flex: none;
  min-width: 24px; height: 24px; display: grid; place-content: center; margin-top: .2em;
  font-family: var(--font-mono); font-weight: 700; font-size: var(--fs-label);
  background: var(--surface); border: var(--bw-thin) solid var(--ink); box-shadow: var(--shadow-sm);
}

/* ============================ 代码 / 引用 / 分隔 / 图片 ============================ */
code, kbd, samp {
  font-family: var(--font-mono); font-size: .92em;
  background: var(--mint); color: var(--ink);
  border: var(--bw-thin) solid var(--ink); padding: 0 5px;
}
.code-block {
  font-family: var(--font-mono); font-size: 14px; line-height: 1.7;
  background: var(--surface); color: var(--ink);
  border: var(--bw) solid var(--ink); border-radius: var(--radius); box-shadow: var(--shadow);
  padding: var(--sp-2); overflow-x: auto; margin: 0;
}
.code-block code { background: none; border: 0; padding: 0; font-size: inherit; }

blockquote, .quote {
  margin: 0; padding-left: var(--sp-2);
  border-left: var(--bw) solid var(--ink);
  color: var(--muted); line-height: 1.8;
}

hr, .divider { border: 0; border-top: var(--bw) solid var(--ink); margin: var(--sp-4) 0; }

/* 图片要边框就用 3px 黑边 + 硬阴影，别用圆角 + 白色光晕 */
.frame {
  display: block; max-width: 100%; height: auto;
  background: var(--surface);
  border: var(--bw) solid var(--ink); border-radius: var(--radius); box-shadow: var(--shadow);
}

/* ============================ 提示条 ============================ */
/* 语义靠 .tone-ok / .tone-warn / .tone-err，别拿 --coral 当错误色（它是主按钮色） */
.alert {
  display: flex; gap: var(--sp-1); align-items: flex-start;
  padding: 12px 16px;
  background: var(--surface); color: var(--ink);
  border: var(--bw) solid var(--ink); border-radius: var(--radius); box-shadow: var(--shadow);
}
.alert b { flex: none; }

/* ============================ 移动端降级 ============================ */
/* 32px 网格在 390px 屏上会变成粗糙的大格子；3px 边和 4px 阴影在小屏的视觉权重接近翻倍。
 * 字号已经用 clamp() 自适应，这里降的是「密度」。 */
@media (max-width: 640px) {
  :root {
    --bw: 2px;
    --bw-thin: 2px;
    --shadow-sm: 1px 1px 0 0 var(--ink);
    --shadow:    3px 3px 0 0 var(--ink);
    --shadow-lg: 4px 4px 0 0 var(--ink);
    --fs-subhead: 18px;
    --sp-3: 20px;
  }
  body {
    background-size: 22px 22px, 22px 22px, 100% 100%;
    /* iOS Safari 上 fixed 会被强制降级、长页滚动还会掉帧，小屏直接关掉 */
    background-attachment: scroll, scroll, scroll;
  }
  .card { padding: var(--sp-2); }
  .body { max-width: none; }
  .table th, .table td { padding: 8px 10px; }
  .code-block { font-size: 13px; }
}

/* 用户在系统里关了动效就别再位移 */
@media (prefers-reduced-motion: reduce) {
  .btn, .lift, .btn-quiet { transition: none; }
  .btn:hover, .btn:active, .lift:hover, .btn-quiet:hover, .btn-quiet:active { transform: none; }
}
```

## 第 3 步 · 套用到结构（HTML 例子）

```html
<!-- 角标：等宽体 -->
<span class="tag label tone-mist">PEOPLE · 一起来玩的人</span>

<!-- 大标题：默认行高 1.3，中文换行不会挤 -->
<h1 class="display">把想法变成产品</h1>

<!-- 纯英文大标题想更狠，才用 Anton -->
<h1 class="display display-en display-tight">TURN IDEAS INTO PRODUCTS</h1>

<!-- 卡片：换底色用 .tone-*，不要写 inline style -->
<div class="card card-lg tone-mist">
  <h3 class="subhead">今日 Demo</h3>
  <p class="body">一句话说清你要做什么，剩下交给 AI。</p>
  <p class="note">次要说明用 .note：同字号 + 灰 + 左竖线，靠结构拉层级。</p>
  <button class="btn">开工 →</button>
  <button class="btn btn-secondary">再想想</button>
</div>

<!-- 反馈状态：用语义色，不要拿主强调色当报错色 -->
<div class="card tone-ok"><b>✓ 报名成功</b></div>
<div class="card tone-warn"><b>! 名额快满了</b></div>
<div class="card tone-err"><b>✕ 提交失败</b></div>
```

## 配色速查

| 变量 | 颜色 | 用在哪 |
|------|------|--------|
| `--paper` `#f5f1e8` | 暖米 | 整页背景（别用纯白） |
| `--surface` `#ffffff` | 白 | 卡面 |
| `--ink` `#0e0e0e` | 近黑 | 文字、**所有边框、所有阴影** |
| `--muted` `#5a5a55` | 灰 | 次要说明文字。**别拿纯黑当说明文字** |
| `--coral` `#DC5C5D` | 珊瑚红 | 主按钮、最重要的标签（克制用）。**配白字**。白字 3.65:1 只过大字号档，所以 coral 上**别放小字** |
| `--mist` `--pink` `--sage` `--mint` | 雾蓝/粉/绿/青 | 标签、卡片底色轮换，制造活泼感 |
| `--ok` `--warn` `--err` | 浅绿/浅橙/浅红 | 成功 / 警告 / 错误。**语义色和主按钮色必须分开** |

换底色一律用修饰类：`.tone-coral` `.tone-mist` `.tone-pink` `.tone-sage` `.tone-mint` `.tone-ok` `.tone-warn` `.tone-err`。

## 字号与间距速查

| 角色 | 类 | 尺寸 | 行高 |
|------|-----|------|------|
| 封面大标题 | `.display` | `clamp(38px, 6.5vw, 72px)` / 900 | **1.3**（中文换行安全） |
| 每屏大标题 | `.headline` | `clamp(26px, 3.6vw, 40px)` / 900 | 1.3 |
| 卡片标题 | `.subhead` | 20px / 700 | 1.4 |
| 正文 | `.body` | 16px / 400 | 1.75，限宽 34em |
| 角标 / 编号 | `.label`（= `.kicker`） | 13px / 700 等宽 | 1.3 |
| 次要说明 | `.note` | 同正文字号 + 灰 + 左竖线 | 1.7 |

单行、确定不会换行的英文大标题，再加 `.display-tight`（行高 1.05）。

间距只用这 6 档：`--sp-1` 8 / `--sp-2` 16 / `--sp-3` 24 / `--sp-4` 32 / `--sp-6` 48 / `--sp-8` 64。

## 组件速查

真实页面里表单、表格、导航、列表占了元素总量的一大半。**这些全部有现成的类，不要自己现编** ——
现编就是同一个 skill 两次结果不一样的根源。

| 要做的东西 | 用什么 |
|---|---|
| 输入框 / 文本域 / 下拉 | `.field`（`input` / `textarea` / `select` 都用它） |
| 勾选框 / 单选框 | `.check`（一律**方的**，圆的单选框在这套语言里是异物） |
| 表单一行 | `.field-label` + `.field`，勾选类用 `.field-row` |
| 表格 | `.table`（外框 3px 实黑，行间用细线 `--line`） |
| 导航 | `.nav` + `.nav-item`，选中态加 `.is-active`（**黑底白字反白**） |
| 项目列表 | `.list`（3px 黑边小色块，不是浏览器小圆点）；变体 `.list-mist` / `.list-sage` |
| 编号列表 | `.list-num`（等宽数字 + 黑边方块） |
| 行内代码 | `code` / `kbd`（已全局接管，青绿底 + 黑边） |
| 代码块 | `.code-block` |
| 引用 | `blockquote` 或 `.quote`（左竖线 + 灰字，已全局接管） |
| 分隔线 | `hr` 或 `.divider`（3px 实黑，已全局接管） |
| 图片 | `.frame`（3px 黑边 + 硬阴影，**别用圆角 + 白色光晕**） |
| 提示条 | `.alert` + `.tone-ok` / `.tone-warn` / `.tone-err` |

```html
<!-- 表单 -->
<label class="field-label">你的名字</label>
<input class="field" type="text" placeholder="怎么称呼你">

<label class="field-label">经验</label>
<select class="field"><option>完全没写过代码</option><option>会一点</option></select>

<label class="field-row"><input class="check" type="checkbox" checked> 我会自带电脑</label>

<!-- 导航：选中态反白 -->
<nav class="nav">
  <a class="nav-item is-active" href="#">概览</a>
  <a class="nav-item" href="#">店铺</a>
</nav>

<!-- 列表：方块点，不是小圆点 -->
<ul class="list"><li>不讲理论</li><li>不留作业</li><li>当天出东西</li></ul>

<!-- 提示条：语义色，不是主按钮色 -->
<div class="alert tone-err"><b>✕ 提交失败</b><span>手机号格式不对。</span></div>
```

## 高密度界面（后台 / 表格 / 工具栏）

这套风格的 4px 硬阴影是给「大卡片、大留白」设计的。**后台页那种密集布局，成排的实心阴影会糊成一片，
按钮上再套 3px 边 + 4px 阴影更是比例失控。**

给容器加 `.dense`，作用域内的边框和阴影整体降一档（组件不用换，改的是 token）：

```html
<section class="dense">
  <!-- 边框 3px→2px、阴影 4px→2px，整片区域自动变轻 -->
  <div class="card card-flat">统计卡：密集网格里连阴影都不要，只留边框</div>

  <!-- 表格行内 / 工具栏的操作按钮 -->
  <button class="btn btn-sm">主操作</button>
  <button class="btn btn-quiet btn-sm">次要操作（平的，hover 才浮起来）</button>
</section>
```

| 类 | 用在哪 |
|----|--------|
| `.dense` | 容器级。后台、表格区、工具栏、侧边栏 |
| `.card-flat` | 去掉阴影只留边框。密集网格、卡中卡 |
| `.btn-sm` | 小号按钮：2px 边 + 2px 阴影 |
| `.btn-quiet` | 安静按钮：平的，hover 才浮起。**成排出现的操作按钮一律用它** |

> 还有一条硬约束：**元素间距别小于 16px**。间距小于阴影偏移的 3 倍时，阴影会压在邻居的边框上，看起来就是脏。

## 移动端

字号用 `clamp()` 已经自适应，`@media (max-width: 640px)` 里再降一次密度，**这些是 CSS 里自动生效的，不用你写**：

- 网格背景 32px → 22px（32px 的格子在 390px 屏上是粗糙的大格子）
- 边框 3px → 2px、阴影 4px → 3px（小屏上边框的视觉权重接近翻倍）
- `background-attachment` 关掉 `fixed`（iOS Safari 会强制降级，长页滚动还掉帧）
- 卡片 padding 收紧，正文取消限宽

另有 `@media (prefers-reduced-motion: reduce)`：用户在系统里关了动效，按压位移自动停用。

## 改造一个已有页面时

新加的类不会自动去掉页面上**已经存在**的圆角和模糊阴影。两步：

1. 在 `<body>`（或要改造的容器）上加 `class="vcs-takeover"` —— 作用域内所有 `border-radius` 被强制抹平。
   想连别人带 blur 的柔和阴影一起抹掉，再加 `vcs-takeover-hard`。
2. 搜一遍代码，删掉这些东西：`rounded-*` / `border-radius:` 非 0 的值 / 带 blur 的 `box-shadow` / 渐变按钮 / `bg-white` 的整页背景。

## ✅ Do / ❌ Don't

- ✅ 直角（`border-radius: 0`）、3px 黑边、实心无模糊阴影、米色底。
- ✅ 标题用 `.display` / `.headline`，卡片标题 `.subhead`，角标 `.label`。
- ✅ 换底色用 `.tone-*` 修饰类。
- ✅ 阴影颜色永远是黑（`--ink`），永远往右下偏移。
- ✅ coral 上的文字**一律白色**（但 coral 上别放小字，白字只在大字号上够对比度）。`.tone-coral` 会把整张卡的文字连同 `.note` 一起转白。
- ✅ coral 卡里的按钮自动转成白底黑字（`.tone-coral .btn`），不用手动改。
- ✅ 后台 / 表格 / 工具栏一律套 `.dense`，成排的按钮用 `.btn-quiet`。
- ✅ 次要文字用 `--muted`，不要一片死黑。
- ❌ 不要圆角、不要 `box-shadow` 带 blur、不要纯白背景。
- ❌ **按钮 / 卡片 / 标签上不要用渐变**（页面底纹那层绿→粉的横向渐变是唯一例外 —— 它是纸张感的一部分，属于品牌资产）。
- ❌ 不要自己现编输入框、表格、导航、列表 —— 上面「组件速查」里都有。
- ❌ 不要中文一套字、拉丁一套字。
- ❌ 不要给中文标题用 1.05 以下的行高（会挤在一起）。
- ❌ 不要新增字号 —— 只有那 5 个角色。
- ❌ 不要拿 `--coral` 当报错色（它是主按钮色），报错用 `--err`。
- ❌ **不要用 inline style 改 `.btn` 的底色** —— `.btn` 的白字是绑定在 coral 底上的，只改 background 会变成白底白字。换色用 `.btn-secondary`（白底）/ `.btn-quiet`（平的）/ `.btn-ghost`（无边）/ `.tone-*`。
- ❌ 自己写新组件时，**只要设了 `background` 就必须同时设 `color`** —— 否则它放进 `.tone-coral` 里会继承白字，变成白底白字。
- ❌ 不要在密集界面里用默认的 4px 阴影按钮 —— 那是给大卡片用的。
- ❌ 元素间距不要小于 16px（阴影会压在邻居边框上）。
- ❌ 点缀色不要大面积铺满，留白和米底是主角。

## 给 AI 的一句话用法

> 用 `vibe-coding-saturday-style` 这个 skill，把我的页面换成活动官网同款风格：珊瑚红做主按钮，卡片轮换雾蓝/粉/绿底。

AI 会：① 加字体 `<link>` ② 注入上面的 CSS 变量与基础类 ③ 把现有按钮/卡片/标题替换成 `.btn` `.card` `.display` 等类
④ 给 `<body>` 加 `.vcs-takeover` 并清掉残留的圆角与模糊阴影。

## v2 改了什么（相对 v1）

| | v1 | v2 |
|---|---|---|
| 标题字 | Anton（无中文，中文 fallback 系统字） | HarmonyOS Sans SC（中西文同族，真 900 字重） |
| `.display` 字重 | 900 打在只有 400 的 Anton 上 → 合成假粗 | 900 是真字重 |
| `.display` 行高 | `.95`，中文换行互相啃 | `1.3`；`.display-tight` 留给单行英文 |
| 角标字 | Audiowide（无中文，且是电竞调性） | IBM Plex Mono 等宽 |
| 主强调色 | `#DC5C5D` + 黑字（和官网 PPT 规范打架） | `#DC5C5D` 品牌色不变，**改配白字**，与官网 PPT 规范统一 |
| 次要文字色 | 没有 | `--muted #5a5a55` |
| 语义色 | 没有，coral 同时当按钮色和错误色 | `--ok` / `--warn` / `--err` |
| 字号 / 间距 | 没有，全靠 inline style 现编 | 5 个字号角色 + 8px 基准的 6 档间距 |
| 卡片换色 | 只能写 inline style | `.tone-*` 修饰类 |
| `.tag` | 没有底色，网格线穿过标签 | 默认白底 |
| 按钮 | 只有一种 | 主 / 次要 / 幽灵 / 小号 / 禁用态 |
| 键盘焦点 | 没有 | `:focus-visible` 珊瑚红描边 |
| 去圆角 | 只是口头承诺 | `.vcs-takeover` 接管层 |
| 「不要渐变」 | 规则禁渐变，自己的 body 却在用 | 口径写清：禁的是按钮/卡片/标签，页面底纹例外 |
| CSS 真源 | SKILL.md 和 theme.css 两份手抄 | theme.css 唯一真源，`python3 build.py` 注入 |
| 组件覆盖 | 只有 6 个类，表单/表格/导航/列表/代码全靠现编 | 补齐 `.field` `.check` `.table` `.nav` `.list` `.code-block` `.alert` `.frame` 等 |
| 高密度界面 | 没有，后台页按钮阴影比例失控 | `.dense` / `.card-flat` / `.btn-quiet` |
| 响应式 | 全文没有一个 `@media` / `clamp` | 字号 `clamp()` + 640px 断点降密度 + `prefers-reduced-motion` |
| sage / mint | 两个颜色肉眼分不出 | mint 拉开到 `#a9cfc4` |

体检报告的 15 条已全部处理完毕。可视化体检台：`/skill-design`（右下角可在 v1 / v2 之间切换对照）。

## 维护

`theme.css` 是唯一真源。改完它之后跑一次 `python3 build.py`，
SKILL.md 里的 CSS 代码块会自动重新生成，两者保证逐字一致。
