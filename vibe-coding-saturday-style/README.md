# vibe-coding-saturday-style

> 一个开源的 **Claude Code / Codex Skill**：一键把任意网页换成 **VIBE CODING SATURDAY** 活动官网同款视觉风格。
> neo-brutalism 新野兽派 —— 暖米色纸张底 · 橄榄绿网格 · 珊瑚红 / 雾蓝点缀 · 3px 纯黑硬边 · 实心偏移阴影 · 直角无圆角。
> 中西文同族的 HarmonyOS Sans SC + 等宽 IBM Plex Mono 角标。**当前版本 v2。**

零依赖、纯 CSS，**任何 HTML / React / Vue 项目都能用**，新手当天就能把丑页面变得有设计感。

覆盖排版（5 个字号角色 + note 说明层）、卡片 / 按钮 / 标签、表单、表格、导航、列表、代码块、提示条，
外加高密度界面降级（`.dense`）、移动端断点、键盘焦点态，以及改造已有页面用的去圆角接管层（`.vcs-takeover`）。

---

## 安装（30 秒）

这个 skill 收在 [`CookieSparkLab/skills`](https://github.com/CookieSparkLab/skills) 合集仓库里。

### 方式 A · clone 合集，拷一个 skill 进项目（推荐）

```bash
git clone https://github.com/CookieSparkLab/skills.git
cp -r skills/vibe-coding-saturday-style 你的项目/.claude/skills/
```

> Codex 用户拷到 `.agents/skills/` 或你的 skills 目录下同理。

### 方式 B · 直接下载

在仓库页点 **Code → Download ZIP**，解压后把 `vibe-coding-saturday-style` 文件夹丢进项目的 `.claude/skills/`。

---

## 怎么用

装好后，对 AI 说一句话：

> 用 `vibe-coding-saturday-style` 这个 skill，把我的页面换成活动官网同款风格：珊瑚红做主按钮，卡片轮换雾蓝 / 粉 / 绿底。

AI 会自动：① 在 `<head>` 加字体 → ② 注入 `theme.css` 的设计 token → ③ 把现有按钮 / 卡片 / 标题替换成 `.btn` `.card` `.display` 等类，并去掉圆角与模糊阴影。

**不想用 AI、想手动**？直接引 `theme.css`：

```html
<head>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://cdn.jsdelivr.net/npm/harmonyos-sans-sc-webfont-splitted@1.1.0/dist/index.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="theme.css">
</head>
<body>
  <span class="tag label tone-mist">PEOPLE · 一起来玩的人</span>
  <h1 class="display">把想法变成产品</h1>
  <div class="card card-lg tone-mist">
    <h3 class="subhead">今日 Demo</h3>
    <p class="body">一句话说清你要做什么，剩下交给 AI。</p>
    <p class="note">次要说明用 .note：同字号 + 灰 + 左竖线。</p>
    <button class="btn">开工 →</button>
    <button class="btn btn-secondary">再想想</button>
  </div>
</body>
```

---

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 给 AI 看的技能说明（含设计原则、完整 CSS、用法）。这是 skill 的本体。 |
| `theme.css` | **唯一真源**。抽出来的纯 CSS，想手动用就直接引这个。 |
| `build.py` | 把 `theme.css` 注入 SKILL.md 的代码块。改完 CSS 跑一次 `python3 build.py`。 |

## 配色

| 变量 | 颜色 | 用在哪 |
|------|------|--------|
| `--paper` `#f5f1e8` | 暖米 | 整页背景（别用纯白） |
| `--ink` `#0e0e0e` | 近黑 | 文字、**所有边框、所有阴影** |
| `--muted` `#5a5a55` | 灰 | 次要说明文字（别拿纯黑当说明文字） |
| `--coral` `#DC5C5D` | 珊瑚红 | 主按钮、最重要的标签（克制用）。**配白字**。白字 3.65:1 只过大字号档，coral 上别放小字 |
| `--mist` `#B6CEED` | 雾蓝 | 标签 / 卡片底 |
| `--pink` `#ffe9f8` · `--sage` `#d7e7d4` · `--mint` `#a9cfc4` | 粉 / 绿 / 青 | 卡片轮换，制造活泼感 |
| `--ok` `#c7e3ad` · `--warn` `#ffd9a8` · `--err` `#ffc2be` | 浅绿 / 浅橙 / 浅红 | 成功 / 警告 / 错误。语义色和主按钮色必须分开 |

换底色一律用修饰类 `.tone-coral` `.tone-mist` `.tone-pink` `.tone-sage` `.tone-mint` `.tone-ok` `.tone-warn` `.tone-err`，别写 inline style。

---

## 来源 & 致谢

提取自 **VIBE CODING SATURDAY**（精神饱满俱乐部 · 不工作坊系列）活动官网的真实设计系统。
拿去随便改、随便用，做出你自己的味道。

## License

[MIT](../LICENSE) —— 自由使用、修改、分发。
