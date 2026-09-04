# cookie-spark-ppt-skill-neo-brutal

> 一个开源的 **Claude Code / Codex Skill**：让 AI 做出一份 **暖纸野兽派风格的网页 PPT**。
> 暖米纸底 · 3px 黑边 · 实心硬阴影 · 全直角 · 按 → 卡片一张张蹦出来。

不是静态图片，是一个能放映的网页：定尺 1920×1080 自动适配任何屏幕，键盘翻页，
**卡片逐个出现、结论句压轴**，讲起来有节奏。做完直接投屏或者发链接。

---

## 安装（30 秒）

这个 skill 收在 [`CookieSparkLab/skills`](https://github.com/CookieSparkLab/skills) 合集仓库里。

### 方式 A · clone 合集，拷一个 skill 进项目（推荐）

```bash
git clone https://github.com/CookieSparkLab/skills.git
cp -r skills/cookie-spark-ppt-skill-neo-brutal 你的项目/.claude/skills/
```

> Codex 用户拷到 `.agents/skills/` 或你的 skills 目录下同理。

### 方式 B · 直接下载

仓库页点 **Code → Download ZIP**，解压后把 `cookie-spark-ppt-skill-neo-brutal`
整个文件夹丢进项目的 `.claude/skills/`。

---

## 怎么用

装好后，对 AI 说一句话：

> 用 `cookie-spark-ppt-skill-neo-brutal` 这个 skill，把这份大纲做成 PPT。

AI 会：① 先列一张页面清单给你确认 → ② 复制起手包 → ③ 一页页填内容 →
④ 跑溢出自检 → ⑤ 交给你一个 `deck.html`。

**触发词**：做 PPT / 做 slide / 做 deck / 做演示 / 做幻灯片 / 做分享用的 PPT /
工作坊 deck / 把这份大纲做成 PPT，或者直接点名要「野兽派 / neo-brutalism / 暖纸风」。

### 放映时的操作

| 按键 | 作用 |
|------|------|
| `→` `↓` `空格` | 前进（先点亮本页卡片，出完才翻页） |
| `←` `↑` | 后退 |
| 点画面 | 也是前进，方便用翻页笔 |
| `D` | 打开排版自检 |

---

## 排版自检

网址后面加 `?debug=1`，或者放映时按 `D`：

- 左下角告诉你**哪几页放不下**
- 塞爆的页会被标红
- 底部虚线是安全线，内容不许压上去

> 塞爆了就删内容，**不要缩字号**。字阶只有 9 个，加一个新字号整套就散了。

---

## 文件夹里有什么

```
cookie-spark-ppt-skill-neo-brutal/
├── SKILL.md                    AI 读的：工作流、容量预算、自检清单
├── assets/
│   └── deck-starter.html       起手包本体，单文件零依赖，含引擎和 5 页范例
└── references/
    ├── spec.md                 配色 + 9 级字阶 + 11 条排版法则（唯一权威版）
    └── layouts.md              7 种版式原型，附可直接抄的代码和容量数字
```

**核心是 `assets/deck-starter.html`。** 样式和放映引擎都在里面调好了，
AI（和你）只需要写 `<section class="slide">`，不用碰 CSS 和 JS。
想自己手改也完全可以，双击就能打开。

---

## 想换配色？

改 `deck-starter.html` 开头 `:root` 里那九个色值就行，其他都不用动。
但**别改形状规则** —— 直角、3px 黑边、无 blur 的实心阴影是这套风格的骨架，
改了就不是野兽派了。

---

## 相关

- [`vibe-coding-saturday-style`](../vibe-coding-saturday-style) —— 同一套视觉语言，但用来给**普通网页**换风格
- [`notion-bold-diagrams`](../notion-bold-diagrams) —— 做 PPT 配图、关系图、流程图

## License

[MIT](../LICENSE)
