# vibe-coding-saturday-style

> 一个开源的 **Claude Code / Codex Skill**：一键把任意网页换成 **VIBE CODING SATURDAY** 活动官网同款视觉风格。
> neo-brutalism 新野兽派 —— 暖米色纸张底 · 橄榄绿网格 · 珊瑚红 / 雾蓝点缀 · 3px 纯黑硬边 · 实心偏移阴影 · 直角无圆角。

零依赖、纯 CSS，**任何 HTML / React / Vue 项目都能用**，新手当天就能把丑页面变得有设计感。

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
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Audiowide&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="theme.css">
</head>
<body>
  <span class="tag" style="background:var(--mist)">PEOPLE · 一起来玩的人</span>
  <h1 class="display" style="font-size:3rem">把想法变成产品</h1>
  <div class="card card-lg">
    <h3 class="kicker">今日 Demo</h3>
    <p>一句话说清你要做什么，剩下交给 AI。</p>
    <button class="btn">开工 →</button>
  </div>
</body>
```

---

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 给 AI 看的技能说明（含设计原则、完整 CSS、用法）。这是 skill 的本体。 |
| `theme.css` | 抽出来的纯 CSS，想手动用就直接引这个。 |

## 配色

| 变量 | 颜色 | 用在哪 |
|------|------|--------|
| `--paper` `#f5f1e8` | 暖米 | 整页背景（别用纯白） |
| `--ink` `#0e0e0e` | 近黑 | 文字、**所有边框、所有阴影** |
| `--coral` `#DC5C5D` | 珊瑚红 | 主按钮、最重要的标签（克制用） |
| `--mist` `#B6CEED` | 雾蓝 | 标签 / 卡片底 |
| `--pink` `#ffe9f8` · `--sage` `#d7e7d4` · `--mint` `#cde2da` | 粉 / 绿 / 青 | 卡片轮换，制造活泼感 |

---

## 来源 & 致谢

提取自 **VIBE CODING SATURDAY**（精神饱满俱乐部 · 不工作坊系列）活动官网的真实设计系统。
拿去随便改、随便用，做出你自己的味道。

## License

[MIT](../LICENSE) —— 自由使用、修改、分发。
